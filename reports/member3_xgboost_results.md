# XGBoost Queue Classification Results

## Member
CIT-24-01-0125

## Model
XGBoost Classifier

## Dataset
Multilingual Customer Support Tickets Dataset (English Subset)

## Objective
Predict the support queue from ticket text.

## Feature Engineering
- Text Cleaning
- Lowercasing
- TF-IDF Vectorization
- Maximum Features: 5000

## Train/Test Split
80% Training
20% Testing

## Classes
- Technical Support
- Product Support
- Customer Service
- IT Support
- Billing and Payments
- Returns and Exchanges
- Service Outages and Maintenance
- Sales and Pre-Sales
- Human Resources
- General Inquiry

## Performance

Accuracy: INSERT_YOUR_ACCURACY_HERE

Classification Report:

PASTE CLASSIFICATION REPORT HERE

## Observations

- XGBoost successfully learned patterns from ticket text.
- Technical Support and Product Support had the highest representation.
- Queue distribution is imbalanced.
- Some smaller classes may have lower recall.

## Conclusion

XGBoost provides a strong baseline model for ticket routing and will be compared against DistilBERT in later phases.