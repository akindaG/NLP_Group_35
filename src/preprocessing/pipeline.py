from src.preprocessing.cleaning import clean_text
from src.preprocessing.tokenization import tokenize_text
from src.preprocessing.stopwords import remove_stopwords
from src.preprocessing.lemmatization import lemmatize_tokens

def preprocess_text(text):
    text = clean_text(str(text))
    tokens = tokenize_text(text)
    tokens = remove_stopwords(tokens)
    tokens = lemmatize_tokens(tokens)
    return " ".join(tokens)