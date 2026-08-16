"""
SupportIQ Business Rules

These rules provide decision-support recommendations
for ticket priority.

The machine-learning model itself predicts the
support queue.
"""


def determine_priority(text):

    text = text.lower()

    high_priority_terms = [

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
        "error"

    ]

    low_priority_terms = [

        "information",
        "inquiry",
        "documentation",
        "guidance",
        "question"

    ]


    if any(
        term in text
        for term in high_priority_terms
    ):

        return "High"


    if any(
        term in text
        for term in low_priority_terms
    ):

        return "Low"


    return "Medium"