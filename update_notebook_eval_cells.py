import json
from pathlib import Path


NOTEBOOK_PATH = Path("preliminary_experiments.ipynb")


def to_source(text: str) -> list[str]:
    return [line + "\n" for line in text.strip("\n").split("\n")]


nb = json.loads(NOTEBOOK_PATH.read_text(encoding="utf-8"))

cell_updates = {
    1: """
import ollama
import json
import pandas as pd

from iterative_eval_utils import (
    compute_bertscore_batched,
    prepare_final_eval_df,
    run_resumable_evaluation,
)
""",
    31: """
# compute outputs on the full evaluation set with resume support
CHECKPOINT_PATH = "iterative_eval_checkpoint.csv"
SAVE_EVERY = 10

full_df = run_resumable_evaluation(
    unique_queries=unique_queries,
    generate_baseline_followup=generate_baseline_followup,
    generate_one_step_followup=generate_one_step_followup,
    get_iterative_outputs=get_iterative_outputs,
    checkpoint_path=CHECKPOINT_PATH,
    save_every=SAVE_EVERY,
    restart=False,
)

display(full_df.head())
""",
    32: """
# attach one reference question per topic
final_df = prepare_final_eval_df(full_df, df)
""",
    33: """
# remove broken rows only where the reference is missing
print(len(final_df))
""",
    34: """
# Evaluation using BERTScore
# Uses batching so progress stays visible and memory usage is steadier.
""",
    35: """
refs = final_df['question'].tolist()

metric_results = {
    'Baseline': compute_bertscore_batched(final_df['Baseline'].tolist(), refs, batch_size=64, label='Baseline BERTScore'),
    'OneStep': compute_bertscore_batched(final_df['OneStep'].tolist(), refs, batch_size=64, label='OneStep BERTScore'),
    'Iterative_First': compute_bertscore_batched(final_df['Iterative_First'].tolist(), refs, batch_size=64, label='Iterative_First BERTScore'),
    'Iterative_Final': compute_bertscore_batched(final_df['Iterative_Final'].tolist(), refs, batch_size=64, label='Iterative_Final BERTScore'),
}

for name, value in metric_results.items():
    print(f"{name}: {value:.4f}")

print("Average iterative steps:", round(final_df['Iterative_Steps'].mean(), 3))
print("Average iterative followups:", round(final_df['Iterative_NumFollowups'].mean(), 3))
""",
    36: """
final_df.to_csv("final_results_iterative_eval.csv", index=False)
print("Saved final results to final_results_iterative_eval.csv")
""",
}

for idx, source in cell_updates.items():
    nb["cells"][idx]["source"] = to_source(source)

NOTEBOOK_PATH.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"Updated {NOTEBOOK_PATH}")
