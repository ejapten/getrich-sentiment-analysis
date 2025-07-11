# Import Library google playstore, pandas, dan csv
from google_play_scraper import reviews_all, Sort
import csv
import os


def main():
    try:
        print("Mulai scraping ulasan dari Google Play Store.....")

        # Ambil ulasan aplikasi
        scrapreview = reviews_all(
            "com.linecorp.LGGRTHN", lang="en", sort=Sort.MOST_RELEVANT, count=1000
        )

        # Cek apakah data berhasil diambil
        if not scrapreview:
            print("Tidak ada ulasan yang berhasil diambil.")
            return

        # Buat folder data/
        os.makedirs("data", exist_ok=True)

        # Simpan hasil ke CSV
        with open(
            "data/raw_data_lgr.csv", mode="w", newline="", encoding="utf-8"
        ) as file:
            writer = csv.writer(file)
            writer.writerow(["review"])
            for review in scrapreview:
                writer.writerow([review["content"]])

        print(f"Berhasil menyimpan {len(scrapreview)} ulasan ke data/raw_data_lgr.csv")

    except Exception as e:
        print("Terjadi kesalahan saat scraping atau menyimpan data.")
        print("Detail error:", str(e))


if __name__ == "__main__":
    main()
