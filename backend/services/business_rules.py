def determine_priority(text):
    
    urgent_words = [
        "not working",
        "failed",
        "cannot",
        "unable",
        "blocked",
        "error",
        "payment failed"
    ]


    for word in urgent_words:
        if word in text.lower():
            return "High"


    return "Medium"




def determine_department(category):


    mapping = {


        "Billing":
        "Billing Support Team",


        "Technical Support":
        "Technical Support Team",


        "Account":
        "Account Support Team",


        "Other":
        "General Support Team"

    }


    return mapping.get(
        category,
        "General Support Team"
    )