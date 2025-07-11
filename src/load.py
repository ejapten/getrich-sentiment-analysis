def train_and_evaluate(x_train, x_test, y_train, y_test):
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, Dropout
    from tensorflow.keras.utils import to_categorical

    # One-hot encoding label
    y_train_encoded = to_categorical(y_train, num_classes=3)
    y_test_encoded = to_categorical(y_test, num_classes=3)

    # Bangun model
    model = Sequential(
        [
            Dense(512, activation="relu", input_dim=x_train.shape[1]),
            Dropout(0.5),
            Dense(256, activation="relu"),
            Dense(128, activation="relu"),
            Dense(3, activation="softmax"),
        ]
    )

    model.compile(
        loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"]
    )

    print("===== Melatih Model =====")
    model.fit(
        x_train,
        y_train_encoded,
        epochs=20,
        batch_size=64,
        validation_data=(x_test, y_test_encoded),
        verbose=1,
    )

    # Evaluasi
    loss, accuracy = model.evaluate(x_test, y_test_encoded)
    print(f"\nLoss: {loss:.4f}")
    print(f"Akurasi: {accuracy:.4%}")

    return model


if __name__ == "__main__":
    from transform import get_transformed_data

    x_train, x_test, y_train, y_test, tfidf = get_transformed_data()
    model = train_and_evaluate(x_train, x_test, y_train, y_test)
    model.save("model_sentiment.h5")
    print("Model telah disimpan sebagai 'model_sentiment.h5'")
