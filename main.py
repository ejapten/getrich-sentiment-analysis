from src.transform import run_transform
from src.load import train_and_evaluate


def main():
    print("Memulai Proses ETL dan Training Model")

    # 1. Jalankan ETL
    x_train, x_test, y_train, y_test, tfidf = run_transform()
    # 2. Training dan evaluasi model
    model = train_and_evaluate(x_train, x_test, y_train, y_test)
    # 3. Simpan model dan vectorizer
    model.save("model_sentiment.h5")
    import pickle

    with open("tfidf_vectorizer.pkl", "wb") as f:
        pickle.dump(tfidf, f)

    print("Semua proses selesai. Model dan TF-IDF disimpan.")


if __name__ == "__main__":
    main()
