import unittest

from backend.services.business_rules import (
    analyze_sentiment,
    determine_priority,
    extract_keywords,
    needs_human_review,
)


class BusinessRuleTests(unittest.TestCase):
    def test_high_priority_keywords(self):
        self.assertEqual(
            determine_priority("Critical outage. The VPN is not working."),
            "High",
        )

    def test_low_priority_keywords(self):
        self.assertEqual(
            determine_priority("I have a question about the documentation."),
            "Low",
        )

    def test_default_priority_is_medium(self):
        self.assertEqual(
            determine_priority("Please update the account contact name."),
            "Medium",
        )

    def test_negative_sentiment(self):
        self.assertEqual(
            analyze_sentiment("The service is broken and failed again"),
            "Negative",
        )

    def test_positive_sentiment(self):
        self.assertEqual(
            analyze_sentiment("Thank you. Everything is working great"),
            "Positive",
        )

    def test_keyword_extraction_is_normalized_and_ranked(self):
        keywords = extract_keywords("Payment failed. Payment error on payment gateway.")
        self.assertEqual(keywords[0], "payment")
        self.assertIn("failed", keywords)

    def test_low_confidence_is_flagged_for_review(self):
        self.assertTrue(needs_human_review(0.42))
        self.assertFalse(needs_human_review(0.85))


if __name__ == "__main__":
    unittest.main()
