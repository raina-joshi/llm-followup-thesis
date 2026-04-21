from __future__ import annotations

import re


DEFAULT_POLICY = "academic"


_CATEGORY_PATTERNS = {
    "explicit_content": [
        r"\bporn\b",
        r"\bpornography\b",
        r"\berotic\b",
        r"\bxxx\b",
        r"\bnsfw\b",
        r"\bsex\b",
        r"\badult\b",
        r"\bescort\b",
        r"\bfetish\b",
        r"\bsexual\b",
        r"\bstrip\b",
    ]
}


POLICY_CATEGORIES = {
    "off": set(),
    "basic": {"explicit_content"},
    "academic": {"explicit_content"},
}


def _patterns_for_policy(policy: str) -> list[str]:
    categories = POLICY_CATEGORIES.get(policy, POLICY_CATEGORIES[DEFAULT_POLICY])
    patterns: list[str] = []
    for category in categories:
        patterns.extend(_CATEGORY_PATTERNS.get(category, []))
    return patterns


def is_allowed_document(title: str, summary: str, policy: str = DEFAULT_POLICY) -> bool:
    patterns = _patterns_for_policy(policy)
    if not patterns:
        return True

    text = f"{title} {summary}".lower()
    return not any(re.search(pattern, text) for pattern in patterns)
