from __future__ import annotations

import math
import time
from pathlib import Path

import pandas as pd


RESULT_COLUMNS = [
    "topic_id",
    "topic",
    "Baseline",
    "OneStep",
    "Iterative_First",
    "Iterative_Final",
    "Iterative_Steps",
    "Iterative_NumFollowups",
]


def _format_duration(seconds: float) -> str:
    seconds = max(0, int(seconds))
    hours, remainder = divmod(seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    if hours:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def _print_progress(label: str, completed: int, total: int, start_time: float) -> None:
    total = max(total, 1)
    width = 30
    ratio = min(max(completed / total, 0), 1)
    filled = math.floor(width * ratio)
    bar = "#" * filled + "-" * (width - filled)

    elapsed = time.time() - start_time
    rate = completed / elapsed if elapsed > 0 else 0
    remaining = (total - completed) / rate if rate > 0 else 0

    print(
        f"\r{label}: [{bar}] {completed}/{total} "
        f"({ratio * 100:5.1f}%) | elapsed {_format_duration(elapsed)} "
        f"| eta {_format_duration(remaining)}",
        end="",
        flush=True,
    )
    if completed >= total:
        print()


def _normalize_checkpoint(checkpoint_df: pd.DataFrame) -> pd.DataFrame:
    available_columns = [col for col in RESULT_COLUMNS if col in checkpoint_df.columns]
    normalized = checkpoint_df[available_columns].copy()
    missing_columns = [col for col in RESULT_COLUMNS if col not in normalized.columns]
    for col in missing_columns:
        normalized[col] = pd.NA
    return normalized[RESULT_COLUMNS]


def run_resumable_evaluation(
    unique_queries: pd.DataFrame,
    generate_baseline_followup,
    generate_one_step_followup,
    get_iterative_outputs,
    checkpoint_path: str | Path = "iterative_eval_checkpoint.csv",
    save_every: int = 10,
    restart: bool = False,
) -> pd.DataFrame:
    checkpoint_path = Path(checkpoint_path)
    work_df = unique_queries[["topic_id", "topic"]].drop_duplicates().copy()
    total = len(work_df)

    completed_df = pd.DataFrame(columns=RESULT_COLUMNS)
    completed_ids: set[int] = set()

    if checkpoint_path.exists() and not restart:
        checkpoint_df = pd.read_csv(checkpoint_path)
        completed_df = _normalize_checkpoint(checkpoint_df)
        completed_ids = set(completed_df["topic_id"].dropna().astype(int).tolist())
        print(f"Loaded checkpoint with {len(completed_ids)} completed queries from {checkpoint_path}.")

    pending_df = work_df[~work_df["topic_id"].isin(completed_ids)].copy()
    pending_total = len(pending_df)
    print(f"Running evaluation for {pending_total} pending queries out of {total} total.")

    rows = completed_df.to_dict("records")
    start_time = time.time()
    processed_since_save = 0
    completed_count = len(rows)
    _print_progress("Evaluation", completed_count, total, start_time)

    for _, row in pending_df.iterrows():
        query = row["topic"]
        iterative = get_iterative_outputs(query)
        followups = iterative.get("history", [])

        rows.append(
            {
                "topic_id": row["topic_id"],
                "topic": query,
                "Baseline": generate_baseline_followup(query),
                "OneStep": generate_one_step_followup(query),
                "Iterative_First": iterative.get("first_followup"),
                "Iterative_Final": iterative.get("final_followup"),
                "Iterative_Steps": iterative.get("num_steps", len(followups)),
                "Iterative_NumFollowups": iterative.get("num_followups"),
            }
        )

        completed_count += 1
        processed_since_save += 1
        _print_progress("Evaluation", completed_count, total, start_time)

        if processed_since_save >= save_every:
            partial_df = pd.DataFrame(rows)
            partial_df = (
                work_df.merge(partial_df, on=["topic_id", "topic"], how="left")[RESULT_COLUMNS]
            )
            partial_df.to_csv(checkpoint_path, index=False)
            print(f"Saved checkpoint at {completed_count}/{total} to {checkpoint_path}.")
            processed_since_save = 0

    full_df = pd.DataFrame(rows)
    full_df = work_df.merge(full_df, on=["topic_id", "topic"], how="left")[RESULT_COLUMNS]
    full_df.to_csv(checkpoint_path, index=False)
    print(f"Saved final checkpoint to {checkpoint_path}.")
    return full_df


def prepare_final_eval_df(full_df: pd.DataFrame, source_df: pd.DataFrame) -> pd.DataFrame:
    ref_df = source_df.drop_duplicates(subset=["topic_id"])[["topic_id", "question"]]
    final_df = full_df.merge(ref_df, on="topic_id")
    final_df = final_df.dropna(subset=["question"]).copy()

    metric_cols = ["Baseline", "OneStep", "Iterative_First", "Iterative_Final"]
    for col in metric_cols:
        final_df[col] = final_df[col].fillna("")

    return final_df


def compute_bertscore_batched(preds, refs, batch_size: int = 64, label: str = "BERTScore") -> float:
    from bert_score import score

    total = len(preds)
    if total != len(refs):
        raise ValueError("preds and refs must have the same length")
    if total == 0:
        return float("nan")

    total_f1 = 0.0
    processed = 0
    start_time = time.time()
    _print_progress(label, processed, total, start_time)

    for start in range(0, total, batch_size):
        end = min(start + batch_size, total)
        _, _, f1 = score(preds[start:end], refs[start:end], lang="en", verbose=False)
        total_f1 += float(f1.sum().item())
        processed = end
        _print_progress(label, processed, total, start_time)

    return total_f1 / total
