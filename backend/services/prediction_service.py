from backend.services.model_loader import (
    models,
    get_xgb_model
)

from backend.services.preprocessing import clean_text



# ==================================================
# Keyword extraction
# ==================================================

def extract_keywords(text):
    
    stop_words = [
        "the",
        "is",
        "not",
        "my",
        "and",
        "this",
        "that",
        "with",
        "from",
        "for"
    ]


    words = text.lower().split()


    keywords = []


    for word in words:

        if word not in stop_words and len(word) > 2:
            keywords.append(word)


    return keywords[:5]



# ==================================================
# Priority prediction
# ==================================================

def predict_priority(text):

    high_priority_words = [

        "failed",
        "cannot",
        "unable",
        "blocked",
        "urgent",
        "error",
        "not working",
        "issue"

    ]


    text = text.lower()


    for word in high_priority_words:

        if word in text:

            return "High"


    return "Medium"




# ==================================================
# Sentiment analysis
# ==================================================

def analyze_sentiment(text):

    negative_words = [

        "failed",
        "problem",
        "issue",
        "error",
        "not working",
        "cannot",
        "unable",
        "wrong"

    ]


    text = text.lower()


    for word in negative_words:

        if word in text:

            return "Negative"


    return "Neutral"




# ==================================================
# Department routing
# ==================================================

def assign_department(category):


    departments = {


        "Technical Support":
            "Technical Support Team",


        "Billing Issue":
            "Finance Support",


        "Account Access":
            "Account Management",


        "Login":
            "Authentication Team"


    }


    return departments.get(
        category,
        "Customer Support Team"
    )




# ==================================================
# Ticket prediction pipeline
# ==================================================

def predict_ticket(text):


    print("📝 Starting prediction")



    print("1️⃣ Cleaning text")


    cleaned = clean_text(text)




    print("2️⃣ Applying TF-IDF")


    vector = models["vectorizer"].transform(
        [cleaned]
    )




    print("3️⃣ Loading XGBoost")


    xgb_model = get_xgb_model()




    print("4️⃣ Running prediction")


    prediction = xgb_model.predict(
        vector
    )


    probabilities = xgb_model.predict_proba(
        vector
    )





    print("5️⃣ Decoding category")


    label = models["encoder"].inverse_transform(
        prediction
    )[0]





    confidence = round(
        float(probabilities.max()),
        3
    )





    keywords = extract_keywords(
        cleaned
    )




    priority = predict_priority(
        cleaned
    )


    sentiment = analyze_sentiment(
        cleaned
    )


    department = assign_department(
        label
    )





    print("✅ Prediction completed")





    from backend.services.business_rules import (
    determine_priority,
    determine_department
    )

    priority = determine_priority(cleaned)

    department = determine_department(label)

    return {


"category": label,


"confidence": confidence,


"priority": priority,


"department": department,


"sentiment": "Negative",


"model_used":
"TF-IDF + XGBoost",


"keywords": keywords,


"cleaned_text": cleaned

}