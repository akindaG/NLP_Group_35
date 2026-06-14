from nltk.corpus import stopwords

STOP_WORDS = set(stopwords.words("english"))


def remove_stopwords(tokens):
    return [
        word
        for word in tokens
        if word not in STOP_WORDS
    ]