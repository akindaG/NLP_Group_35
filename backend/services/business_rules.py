"""SupportIQ decision-support rules.

The deployed XGBoost model predicts the support queue. Priority, sentiment,
keywords, and review recommendations are lightweight transparent rules that
supplement the model output. They are intentionally kept separate from the
trained classifier so the UI can explain which outputs are model-based and
which are rule-based.
"""

from collections import Counter
import re

HIGH_PRIORITY_TERMS = (
    "urgent",
    "critical",
    "security breach",
    "data breach",
    "outage",
    "cannot",
    "unable",
    "failed",
    "not working",
    "blocked",
    "error",
)

LOW_PRIORITY_TERMS = (
    "information",
    "inquiry",
    "documentation",
    "guidance",
    "question",
)

POSITIVE_WORDS = {
    "good",
    "great",
    "excellent",
    "happy",
    "thanks",
    "thank",
    "resolved",
    "working",
    "satisfied",
}

NEGATIVE_WORDS = {
    "failed",
    "failure",
    "problem",
    "issue",
    "error",
    "unable",
    "cannot",
    "wrong",
    "slow",
    "outage",
    "broken",
    "malfunction",
    "disruption",
    "breach",
}

STOP_WORDS = {
    "the", "is", "are", "a", "an", "and", "this", "that", "with",
    "from", "for", "my", "our", "to", "of", "in", "on", "it", "i",
    "we", "you", "your", "was", "were", "be", "been", "have", "has",
}


def _tokens(text: str) -> list[str]:
    """Return normalized alphabetic tokens while keeping contractions simple."""
    return re.findall(r"[a-zA-Z][a-zA-Z'-]*", text.lower())


def determine_priority(text: str) -> str:
    """Recommend High, Medium, or Low priority using transparent keywords."""
    normalized = text.lower()

    if any(term in normalized for term in HIGH_PRIORITY_TERMS):
        return "High"
    if any(term in normalized for term in LOW_PRIORITY_TERMS):
        return "Low"
    return "Medium"


def analyze_sentiment(text: str) -> str:
    """Provide a lightweight lexicon-based sentiment recommendation."""
    words = _tokens(text)
    positive_score = sum(word in POSITIVE_WORDS for word in words)
    negative_score = sum(word in NEGATIVE_WORDS for word in words)

    if negative_score > positive_score:
        return "Negative"
    if positive_score > negative_score:
        return "Positive"
    return "Neutral"


def extract_keywords(text: str, limit: int = 5) -> list[str]:
    """Extract frequent informative words for a compact explanation panel."""
    candidates = [
        word
        for word in _tokens(text)
        if word not in STOP_WORDS and len(word) > 3
    ]
    counts = Counter(candidates)
    return [word for word, _ in counts.most_common(limit)]


def needs_human_review(confidence: float, threshold: float = 0.60) -> bool:
    """Flag low-confidence predictions for human review."""
    return confidence < threshold
