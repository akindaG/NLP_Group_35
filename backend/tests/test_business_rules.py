from backend.services.business_rules import (
    analyze_sentiment,
    determine_priority,
    extract_keywords,
    needs_human_review,
)


def test_high_priority_keywords():
    assert determine_priority("Critical outage. The VPN is not working.") == "High"


def test_low_priority_keywords():
    assert determine_priority("I have a question about the documentation.") == "Low"


def test_default_priority_is_medium():
    assert determine_priority("Please update the account contact name.") == "Medium"


def test_negative_sentiment():
    assert analyze_sentiment("The service is broken and failed again") == "Negative"


def test_positive_sentiment():
    assert analyze_sentiment("Thank you. Everything is working great") == "Positive"


def test_keyword_extraction_is_normalized_and_ranked():
    keywords = extract_keywords("Payment failed. Payment error on payment gateway.")
    assert keywords[0] == "payment"
    assert "failed" in keywords


def test_low_confidence_is_flagged_for_review():
    assert needs_human_review(0.42) is True
    assert needs_human_review(0.85) is False
