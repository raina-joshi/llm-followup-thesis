import json
from pathlib import Path


NOTEBOOK_PATH = Path("preliminary_experiments.ipynb")


def to_source(text: str) -> list[str]:
    return [line + "\n" for line in text.strip("\n").split("\n")]


nb = json.loads(NOTEBOOK_PATH.read_text(encoding="utf-8"))

nb["cells"][1]["source"] = to_source(
    """
import ollama
import json
import pandas as pd

from iterative_eval_utils import (
    compute_bertscore_batched,
    prepare_final_eval_df,
    run_resumable_evaluation,
)
from retrieval_guardrails import DEFAULT_POLICY, is_allowed_document
"""
)

nb["cells"][8]["source"] = to_source(
    """
# get wikipedia docs for a query
import wikipedia

def get_wiki_docs(query, top_k=5, policy=DEFAULT_POLICY):
    docs = []

    try:
        titles = wikipedia.search(query, results=top_k * 3)

        for title in titles:
            try:
                page = wikipedia.page(title, auto_suggest=False)
                if not is_allowed_document(page.title, page.summary, policy=policy):
                    continue
                docs.append({
                    "title": page.title,
                    "summary": page.summary
                })
                if len(docs) >= top_k:
                    break
            except:
                continue

    except:
        pass

    return docs
"""
)

nb["cells"][12]["source"] = to_source(
    """
def filter_relevant_docs(query, docs, policy=DEFAULT_POLICY):
    import re

    def normalize(text):
        text = text.lower()
        text = re.sub(r'[^a-z0-9\\s]', ' ', text)
        text = re.sub(r'\\s+', ' ', text).strip()
        return text

    query_norm = normalize(query)
    query_words = [
        w for w in query_norm.split()
        if w not in {"the", "and", "of", "to", "in", "for", "on", "a", "an"}
        and len(w) > 2
    ]

    generic_query = len(query_words) <= 2
    scored_docs = []

    for doc in docs:
        if isinstance(doc, dict):
            title = doc.get("title", "")
            summary = doc.get("summary", "")
        else:
            title = ""
            summary = str(doc)

        if not is_allowed_document(title, summary, policy=policy):
            continue

        title_norm = normalize(title)
        doc_norm = normalize(summary)

        lexical_score = sum(1 for w in query_words if w in doc_norm)
        title_score = sum(2 for w in query_words if w in title_norm)
        score = lexical_score + title_score

        if generic_query and (" in " in title_norm or " list of " in title_norm):
            score -= 2

        prompt = f\"\"\"
        Query: {query}

        Document title:
        {title}

        Document:
        {summary[:1200]}

        Task:
        Is this document directly relevant to answering the query?

        Rules:
        - Prefer documents about the exact entity or topic in the query.
        - For generic queries, prefer broad topic pages over location-specific pages.
        - Reject documents that only match one common word.
        - Reject policy-disallowed or academically unsuitable documents.
        - Answer YES only if the document is clearly about the same topic.

        Answer ONLY:
        YES or NO
        \"\"\"

        response = ollama.chat(
            model='llama3.2:3b',
            messages=[{'role': 'user', 'content': prompt}],
            options={'num_predict': 5, 'temperature': 0}
        )

        ans = response['message']['content'].strip().upper()

        if "YES" in ans and score > 0:
            scored_docs.append((score, summary))

    scored_docs = sorted(scored_docs, key=lambda x: x[0], reverse=True)
    filtered = [doc for _, doc in scored_docs[:3]]

    if filtered:
        return filtered

    lexical_fallback = []
    for doc in docs:
        if isinstance(doc, dict):
            title = doc.get("title", "")
            summary = doc.get("summary", "")
        else:
            title = ""
            summary = str(doc)

        if not is_allowed_document(title, summary, policy=policy):
            continue

        title_norm = normalize(title)
        doc_norm = normalize(summary)
        score = sum(1 for w in query_words if w in doc_norm) + sum(2 for w in query_words if w in title_norm)
        if generic_query and (" in " in title_norm or " list of " in title_norm):
            score -= 2
        if score > 0:
            lexical_fallback.append((score, summary))

    lexical_fallback = sorted(lexical_fallback, key=lambda x: x[0], reverse=True)
    if lexical_fallback:
        return [doc for _, doc in lexical_fallback[:2]]

    if docs:
        first_doc = docs[0]
        if isinstance(first_doc, dict) and is_allowed_document(first_doc.get("title", ""), first_doc.get("summary", ""), policy=policy):
            return [first_doc.get("summary", "")]
        if not isinstance(first_doc, dict) and is_allowed_document("", str(first_doc), policy=policy):
            return [str(first_doc)]

    return []
"""
)

nb["cells"][13]["source"] = to_source(
    """
# detect ambiguity BEFORE answer generation
def detect_ambiguity(query):
    query = query.strip()

    # well-formed named entities usually do not need intent clarification
    if len(query.split()) >= 3 and query.replace(" ", "").isalpha():
        return False

    prompt = f\"\"\"
    Query: {query}

    Does this query have multiple meanings or interpretations,
    or is it missing the intent needed to answer it correctly?

    Answer only: YES or NO
    \"\"\"

    response = ollama.chat(
        model='llama3.2:3b',
        messages=[{'role': 'user', 'content': prompt}],
        options={'num_predict': 5, 'temperature': 0}
    )

    return "YES" in response['message']['content'].upper()
"""
)

NOTEBOOK_PATH.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"Updated {NOTEBOOK_PATH}")
