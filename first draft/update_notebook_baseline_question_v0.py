import json
from pathlib import Path


NOTEBOOK_PATH = Path("preliminary_experiments.ipynb")


def to_source(text: str) -> list[str]:
    return [line + "\n" for line in text.strip("\n").split("\n")]


nb = json.loads(NOTEBOOK_PATH.read_text(encoding="utf-8"))

nb["cells"][17]["source"] = to_source(
    """
# Baseline follow-up generation (plain prompting)

def ensure_question(text, query):
    text = str(text).strip()
    text = text.replace("Question:", "").replace("Follow-up", "").replace(":", "").strip()
    text = " ".join(text.split())

    if not text:
        return f"What specific information are you looking for about {query}?"

    if "?" in text:
        text = text.split("?")[0].strip() + "?"
        return text

    lowered = text.lower()
    if lowered.startswith(("what ", "which ", "who ", "where ", "when ", "why ", "how ", "are ", "is ", "do ", "does ", "did ", "can ", "could ", "would ", "should ")):
        return text.rstrip(".!") + "?"

    if lowered.endswith(" is") or lowered.endswith(" are"):
        return text.rstrip(".!") + "?"

    return f"What specific information are you looking for about {query}?"


def generate_baseline_followup(query):
    prompt = f\"\"\"
    Generate ONE useful follow-up question to clarify the query.

    Rules:
    - Ask about a specific missing detail (e.g., location, type, features, time, etc.)
    - Do NOT ask vague questions like "What do you want to know?"
    - The question must narrow down the query and be relevant to the original query and potential information needs.
    - Frame the output as a question.
    - The output must end with a question mark.
    - Do not answer the query.
    - Do not complete the sentence as a statement.

    Query: {query}

    Return ONLY the question.
    \"\"\"

    response = ollama.chat(
        model='llama3.2:3b',
        messages=[{'role': 'user', 'content': prompt}],
        options={'num_predict': 50, 'temperature': 0}
    )

    msg = response['message']
    text = msg.get('content', '').strip()

    return ensure_question(text, query)
"""
)

NOTEBOOK_PATH.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"Updated {NOTEBOOK_PATH}")
