import pickle
import numpy as np
from tensorflow.keras.models import load_model
from transform import (
    cleaningtext,
    casefolding,
    tokenizingtext,
    remove_stopwords,
    toSentence,
)
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download("punkt")

# Load model dan vectorizer
model = load_model("model_sentiment.h5")

with open("tfidf_vectorizer.pkl", "rb") as f:
    tfidf = pickle.load(f)

# Kode label: (pastikan sesuai dengan label encoding sebelumnya)
label_map = {0: "negative", 1: "neutral", 2: "positive"}


def preprocess_input(text):
    text = cleaningtext(text)
    text = casefolding(text)
    tokens = tokenizingtext(text)
    tokens = remove_stopwords(tokens)
    final_text = toSentence(tokens)
    return final_text


def predict_sentiment(text):
    preprocessed = preprocess_input(text)
    vector = tfidf.transform([preprocessed]).toarray()
    prediction = model.predict(vector)
    label_index = np.argmax(prediction)
    confidence = np.max(prediction)
    return label_map[label_index], confidence


# Contoh penggunaan
if __name__ == "__main__":
    user_text = input("Masukkan review/game komentar: ")
    print("\n" + "=" * 40)
    print("Hasil Prediksi Sentimen".center(40))
    print("=" * 40)

    label, conf = predict_sentiment(user_text)
    print(f"Teks       : {user_text}")
    print(f"Sentimen   : {label}")
    print(f"Keyakinan  : {conf:.2%}")
    print("=" * 40 + "\n")
