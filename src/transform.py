# ============================= #
#         Import Library       #
# ============================= #
import pandas as pd
import numpy as np
import re
import string
import nltk
import os
import langid
import gensim
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from sklearn.preprocessing import LabelEncoder
from nltk.tokenize import word_tokenize
from nltk.corpus import words, stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# ============================= #
#        Download NLTK         #
# ============================= #
nltk.download("stopwords")
nltk.download("punkt_tab")
nltk.download("vader_lexicon")
nltk.download("words")

# ============================= #
#      Load Raw CSV File       #
# ============================= #
print("===== 1. Memuat File =====")
file_path = os.path.join("data", "raw_data_lgr.csv")
review_lgr = pd.read_csv(file_path)
print("✅ File berhasil dimuat\n")

# ============================= #
#        Preprocessing         #
# ============================= #


# Menghapus missing value, duplikat, dan baris kosong
def clean_missing_and_duplicates(df):
    df_clean = df.dropna()
    df_clean = df_clean.drop_duplicates()
    df_clean = df_clean.fillna("")
    return df_clean


# Menyaring ulasan berbahasa Inggris
def is_english(text):
    if not text:
        return False
    lang, _ = langid.classify(text)
    return lang == "en"


# Membersihkan karakter tak penting
def cleaningtext(review):
    review = re.sub(r"@[A-Za-z0-9]+", "", review)
    review = re.sub(r"#[A-Za-z0-9]+", "", review)
    review = re.sub(r"RT[\s]", "", review)
    review = re.sub(r"http\S+", "", review)
    review = re.sub(r"[0-9]+", "", review)
    review = re.sub(r"[^\w\s]", "", review)
    review = review.replace("\n", " ")
    review = review.translate(str.maketrans("", "", string.punctuation))
    return review.strip()


# Casefolding
def casefolding(review):
    return review.lower()


# Tokenisasi
def tokenizingtext(review):
    return word_tokenize(review)


# Filter token berbahasa Inggris
english_vocab = set(w.lower() for w in words.words())


def english(tokens):
    if not tokens or not isinstance(tokens, list):
        return False
    tokens = [token for token in tokens if token.isalpha()]
    return all(token in english_vocab for token in tokens)


# Stopwords removal
stop_words = set(stopwords.words("english"))


def remove_stopwords(tokens):
    return [token for token in tokens if token.lower() not in stop_words]


# Gabungkan token menjadi kalimat
def toSentence(list_words):
    return " ".join(word for word in list_words)


# Label Sentimen
analyzer = SentimentIntensityAnalyzer()


def sentiment_label(text):
    score = analyzer.polarity_scores(text)["compound"]
    if score >= 0.05:
        return "positive"
    elif score <= -0.05:
        return "negative"
    else:
        return "neutral"


# Proses semua tahapan cleaning
def process_reviews(df):
    print("===== 2. Preprocessing Data =====")
    df_clean = clean_missing_and_duplicates(df)
    df_clean = df_clean[df_clean["review"].apply(is_english)]
    df_clean["review_clean"] = df_clean["review"].apply(cleaningtext)
    df_clean["review_casefolding"] = df_clean["review_clean"].apply(casefolding)
    df_clean["review_token"] = df_clean["review_casefolding"].apply(tokenizingtext)
    df_clean = df_clean[df_clean["review_token"].apply(english)]
    df_clean["review_stopwords"] = df_clean["review_token"].apply(remove_stopwords)
    df_clean["review_final"] = df_clean["review_stopwords"].apply(toSentence)

    # Copy hasil final dan beri label sentimen
    data_sentiment = df_clean[["review_final"]].copy()
    data_sentiment["sentiment_label"] = data_sentiment["review_final"].apply(
        sentiment_label
    )
    print("Preprocessing selesai\n")
    return data_sentiment


# ============================= #
#     Labeling dan TF-IDF      #
# ============================= #
def transform_text_data(df):
    print("===== 3. Label Encoding & TF-IDF =====")
    le = LabelEncoder()
    df["sentiment_label"] = le.fit_transform(df["sentiment_label"])
    for i, label in enumerate(le.classes_):
        print(f"{i} -> {label}")

    x_1 = df["review_final"]
    y_1 = df["sentiment_label"]

    tfidf = TfidfVectorizer(max_features=1000, min_df=10, max_df=0.8)
    x_tfidf = tfidf.fit_transform(x_1).toarray()

    x_train, x_test, y_train, y_test = train_test_split(
        x_tfidf, y_1, test_size=0.2, random_state=42
    )
    print("Transformasi dan split selesai\n")
    return x_train, x_test, y_train, y_test, tfidf


# ============================= #
#         Eksekusi Main        #
# ============================= #


def get_transformed_data():
    df_sentiment = process_reviews(review_lgr)
    return transform_text_data(df_sentiment)


def run_transform():
    df_sentiment = process_reviews(review_lgr)
    x_train, x_test, y_train, y_test, tfidf = transform_text_data(df_sentiment)
    return x_train, x_test, y_train, y_test, tfidf


if __name__ == "__main__":
    df_sentiment = process_reviews(review_lgr)
    x_train, x_test, y_train, y_test, tfidf = transform_text_data(df_sentiment)
