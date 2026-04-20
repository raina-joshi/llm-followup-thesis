import json
from pathlib import Path


NOTEBOOK_PATH = Path("preliminary_experiments.ipynb")


def to_source(text: str) -> list[str]:
    return [line + "\n" for line in text.strip("\n").split("\n")]


nb = json.loads(NOTEBOOK_PATH.read_text(encoding="utf-8"))

nb["cells"][19]["source"] = to_source(
    """
# Aspect extraction
def extract_aspects(query):
    import re

    query_clean = str(query).strip()
    query_lower = query_clean.lower()
    words = [w for w in re.findall(r"[a-zA-Z0-9]+", query_clean) if len(w) > 1]

    def has_any(phrases):
        return any(p in query_lower for p in phrases)

    def classify_query_type(text):
        text_lower = text.lower().strip()
        tokens = [w for w in re.findall(r"[a-zA-Z0-9]+", text_lower) if len(w) > 1]

        if len(tokens) <= 2:
            return "ambiguous_short_query"

        if has_any(["family tree", "ancestry", "genealogy"]):
            return "family_relationship"

        if has_any(["hotel", "resort", "inn", "airport", "terminal", "airlines"]):
            return "place_or_facility"

        if has_any(["restaurant", "museum", "university", "company", "organization", "school", "farm"]):
            return "organization_or_place"

        if has_any(["cheap", "best", "budget", "affordable", "price", "pricing", "cost", "provider", "plan"]):
            return "service_or_product"

        if has_any(["map", "located", "location", "address", "directions", "where is"]):
            return "place_or_location"

        if has_any(["who won", "biography", "born", "died", "who is", "who was"]):
            return "person"

        # Broad person-name heuristic without memorizing topic-specific exceptions.
        title_cased = [part for part in re.split(r"\\s+", text.strip()) if part]
        if 2 <= len(title_cased) <= 4 and all(part[:1].isalpha() for part in title_cased):
            non_person_markers = {
                "airport", "hotel", "resort", "museum", "restaurant", "company",
                "university", "school", "farm", "lake", "park", "internet",
                "family", "tree", "map", "disease", "county", "tourism"
            }
            if not any(token in non_person_markers for token in tokens):
                return "person"

        if has_any(["disease", "symptoms", "treatment", "causes"]):
            return "topic_or_condition"

        if has_any(["album", "movie", "film", "book", "song", "game"]):
            return "work_or_media"

        return "generic"

    query_type = classify_query_type(query_clean)

    aspect_priors = {
        "family_relationship": ["family members", "ancestry", "relationships"],
        "service_or_product": ["type or option", "pricing or availability", "features or providers"],
        "place_or_facility": ["location", "services or amenities", "current status"],
        "place_or_location": ["location", "key features", "relevance or use"],
        "organization_or_place": ["main purpose or type", "location", "notable features"],
        "person": ["identity", "role or career", "notable contribution"],
        "topic_or_condition": ["definition or type", "causes or features", "diagnosis or treatment"],
        "work_or_media": ["work identity", "content or subject", "notable significance"],
        "ambiguous_short_query": ["intended meaning", "context", "specific need"],
    }

    if query_type in aspect_priors:
        return aspect_priors[query_type]

    prompt = f\"\"\"
    Identify 3 key aspects needed to answer this query well.

    An aspect is a dimension of information required to satisfy the query,
    including implicit missing information when relevant.

    Rules:
    - exactly 3 aspects
    - short phrases only
    - 2 to 5 words each
    - no full sentences
    - avoid generic items like "details", "information", "major achievements", or "historical significance"
    - prefer aspects that help generate useful follow-up questions for this specific query type
    - if the query is about a person, use person-style aspects only when appropriate
    - if the query is about a place, organization, service, or object, do NOT use person-style aspects

    Query: {query_clean}

    Aspects:
    \"\"\"
    response = ollama.chat(
        model='llama3.2:3b',
        messages=[{'role': 'user', 'content': prompt}],
        options={'num_predict': 80, 'temperature': 0}
    )

    def clean_aspects(text):
        lines = text.split("\\n")
        cleaned = []
        banned = {
            "details", "information", "general information", "overview", "background",
            "major achievements", "historical significance"
        }

        for line in lines:
            line = line.strip()
            line = line.lstrip("1234567890.-) ").strip()
            line = re.sub(r'[^a-zA-Z0-9\\s/&-]', '', line).strip()

            if not line:
                continue
            if len(line.split()) < 1 or len(line.split()) > 6:
                continue
            if line.lower() in banned:
                continue
            if any(x in line.lower() for x in ["part", "definition", "usage"]):
                continue

            cleaned.append(line)

        deduped = []
        seen = set()
        for item in cleaned:
            key = item.lower()
            if key not in seen:
                seen.add(key)
                deduped.append(item)

        return deduped[:3]

    raw = response['message']['content']
    aspects = clean_aspects(raw)

    if len(aspects) < 3:
        fallback = ["main topic", "key facts", "context"]
        for item in fallback:
            if len(aspects) < 3 and item.lower() not in {a.lower() for a in aspects}:
                aspects.append(item)

    return aspects[:3]
"""
)

NOTEBOOK_PATH.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"Updated {NOTEBOOK_PATH}")
