import os
import pandas as pd
from gensim.models import Word2Vec
import numpy as np

# 1. Load Processed Dataset
df = pd.read_csv("data/processed/customer_support_en.csv")

# 2. Tokenize clean_text column
tokenized_sentences = [str(text).split() for text in df["clean_text"].fillna("")]

# 3. Train Word2Vec Model
w2v_model = Word2Vec(
    sentences=tokenized_sentences,
    vector_size=100,
    window=5,
    min_count=2,
    epochs=10,
    workers=4
)

# 4. Generate Sentence Embeddings
def get_sentence_vector(tokens, model):
    vectors = [model.wv[word] for word in tokens if word in model.wv]
    return np.mean(vectors, axis=0) if vectors else np.zeros(model.vector_size)

sentence_vectors = np.array([get_sentence_vector(tokens, w2v_model) for tokens in tokenized_sentences])

# 5. Save Model and Embeddings
os.makedirs("models/member2", exist_ok=True)
w2v_model.save("models/member2/word2vec.model")
np.save("models/member2/train_vectors.npy", sentence_vectors)

print("Word2Vec training complete and embeddings saved.")