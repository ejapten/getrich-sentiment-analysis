import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.cm as cm
import sys
import os

sys.path.append(os.path.abspath(".."))
from src.transform import process_reviews, review_lgr


def distribusi_label(df):
    """Visualisasi distribusi label sentimen."""
    sns.countplot(
        data=df, x="sentiment_label", order=["positive", "neutral", "negative"]
    )
    plt.title("Distribusi Sentimen")
    plt.xlabel("Label Sentimen")
    plt.ylabel("Jumlah Review")
    plt.tight_layout()
    plt.show()


def kata_terbanyak(text_series, title, n=30):
    """Menampilkan n kata terbanyak dari kumpulan teks."""
    vector = CountVectorizer()
    model_kata = vector.fit_transform(text_series)
    jumlah_kata = model_kata.toarray().sum(axis=0)
    vocab = vector.get_feature_names_out()

    kata_freq = pd.Series(jumlah_kata, index=vocab).sort_values(ascending=False)[:n]

    plt.figure(figsize=(12, 3))
    warna = cm.viridis(np.linspace(0, 1, n))
    kata_freq.plot(kind="bar", color=warna)
    plt.title(f"Top {n} Kata - {title}")
    plt.xlabel("Kata")
    plt.ylabel("Jumlah Frekuensi")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def run_eda(df):
    print("\n===== EDA Dimulai =====")
    distribusi_label(df)

    positive_reviews = df[df["sentiment_label"] == "positive"]["review_final"]
    negative_reviews = df[df["sentiment_label"] == "negative"]["review_final"]
    neutral_reviews = df[df["sentiment_label"] == "neutral"]["review_final"]

    if not positive_reviews.empty:
        kata_terbanyak(positive_reviews, "Positive")
    if not negative_reviews.empty:
        kata_terbanyak(negative_reviews, "Negative")
    if not neutral_reviews.empty:
        kata_terbanyak(neutral_reviews, "Neutral")

    print("===== EDA Selesai =====\n")


# RUN
if __name__ == "__main__":
    df_sentiment = process_reviews(review_lgr)
    run_eda(df_sentiment)
