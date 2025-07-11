# getrich-sentiment-analysis

## Tujuan :
<p align="justify"> 
Di balik popularitas game 'Let's Get Rich', terdapat ribuan ulasan pemain di Google Play Store yang terus bertambah. Proyek  ini bertujuan untuk membangun sebuah model Machine Learning yang berfungsi sebagai sistem prediksi sentimen yang siap pakai. Setelah dilatih menggunakan data historis, model ini mampu:
<p align="justify"> 
  
<p align="justify"> 
  
**1. Menganalisis: Memahami pola bahasa dan konteks dari ribuan ulasan yang ada.**
<p align="justify"> 
  
**2. Memprediksi: Ketika sebuah komentar baru dimasukkan, sistem akan secara instan memprediksi klasifikasi sentimennya—apakah itu positif, negatif, atau netral.**
<p align="justify"> 
  
<p align="justify"> 
Tujuan akhirnya adalah menyediakan sebuah alat praktis yang dapat digunakan untuk menyaring dan memahami feedback pemain
<p align="justify"> 

## Proses
<img width="1482" height="181" alt="Diagram Tanpa Judul drawio" src="https://github.com/user-attachments/assets/390a126c-56cc-4fe9-a178-fe58c6a43bfa" />

Proyek analisis sentimen ini dilakukan berbagai tahapan, yaitu:
<p align="justify"> 
    
**1. Tujuan** : Tujuan proyek ini adalah mengetahui sebuah wawasan dari reviews game getrich. Apakah wawasan tersebut reviewsnya terdapat banyak negative, neutral atau positive. Selain itu, mengetahui kata apa saja yang paling banyak muncul dalam kategori negative, neutral, dan positive. Lalu proyek ini juga membuat sebuah sistem prediksi untuk klasifikasi sentimenya apakah positif, negatif, atau netral. 
<p align="justify"> 


<p align="justify"> 
  
**2. Scraping :** Setelah menentukan tujuan, selanjutnya mengumpulkan data yang dibutuhhkan dengan cara scraping atau mengambil data review/ulasan dari play store
  <p align="justify"> 
    
    <p align="justify"> 
      
**3. Reviews Data :** Ini adalah file csv hasil dari proses scraping. Hasil ini akan disimpan pada folder data untuk proses selanjutnya
  <p align="justify"> 
    
**4. Transform Data:** Pada tahap ini, hasil dari scraping berupa reviews data digunakan. Lalu dilakukan pembersihan data, transformasi data, dan labelisasi agar data siap dilakukan untuk proses EDA dan Training lalu evaluasi. selain itu, hasil dari tahap Transform data adalah data sudah di labelisasi yaitu sebuah reviews/ulasan diberi kategori, apakah ulasan terebut negative, neutral, atau positive
    <p align="justify"> 
      
**5. Pada tahap setelah transformasi** dilakukan dua proses yaitu EDA dan Training & Evaluasi:
      
   **a. EDA :** Setelah Transform dilakukan Explaratory Data Analyst (EDA) untuk mengetahui insight dari sebuah data yang sudah di labelisasi
   
  **b. Training dan Evaluasi :** Pada tahap ini, data latih digunakan untuk membangun sebuah model klasifikasi sentimen. Setelah training, model dievaluasi performanya menggunakan data uji untuk mengukur akurasi dan metrik lainnya sebelum disimpan.
      <p align="justify"> 
        
**6. save model (h5 dan pkl)**: Model dan vectorizer yang telah terbukti memiliki performa baik setelah dievaluasi kemudian disimpan ke dalam file .h5 dan .pkl. Hal ini berfungsi agar model dapat digunakan kembali untuk prediksi di masa depan tanpa perlu melakukan proses training ulang.

 <p align="justify"> 
   
**7. predict**: Pada tahap ini, model yang sudah disimpan (.h5) dan vectorizer (.pkl) dimuat kembali. Model kemudian digunakan untuk menebak atau memprediksi sentimen dari sebuah komentar baru yang belum pernah dilihat sebelumnya.
          <p align="justify"> 
            
**8. output :** Hasil akhir dari proses prediksi, yaitu label klasifikasi sentimen seperti 'Positif', 'Negatif', atau 'Netral' yang ditampilkan kepada pengguna.

## Result 
<p align="justify"> 
Tahap Analisis Data Eksplorasi (EDA) dilakukan untuk mendapatkan pemahaman awal mengenai karakteristik dataset ulasan. 
<p align="justify"> 
  
**1. Data Imbalanced**
<img width="450" height="350" alt="image" src="https://github.com/user-attachments/assets/cfd6a380-f256-4bf9-ada9-2d0d856ecf3c" />

<p align="justify"> 
Gambar diatas menjelaskan bahwa reviews Getrich imbalanced atau reviews nya tidak seimbang, di mana jumlah ulasan positif jauh melampaui jumlah ulasan netral dan negatif. Maka, pemain yang memberikan ulasan cenderung memiliki pengalaman yang positif dengan game "Let's Get Rich".
<p align="justify"> 

**2. Kata Terbanyak dalam reviews berkategori Positive**
<img width="850" height="364" alt="image" src="https://github.com/user-attachments/assets/94574ddc-8d91-4da8-8fdc-53135a3000bc" />

<p align="justify"> 
Gambar diatas, terdapat kata "game, fun, good, play, love, nice, like, great, awesome, cool, enjoy, easy" Para pemain mennyatakan bahwa game ini menyenangkan dan mudah dinikmati. Lalu terdapat "win" dimana pemain jika merasakan kemenangan akan membuat reviews yang positive. Ada juga "card, diamond" sistem reward ini adalah membbuat pemain senang. Lalu terdapat "friend" dimana menunjukan bahwa elemen sosial dan berman bersama teman adalah hal positive.
<p align="justify"> 
  
**3. Kata Terbanyak dalam reviews berkategori Negative**
<img width="850" height="364" alt="image" src="https://github.com/user-attachments/assets/e2446b09-fe5c-4a1d-9b5e-863bf31aabe9" />

<p align="justify"> 
Gambar diatas terdapat kata "error, login, connection, fix, update, cant" menunjukan bahwa pemain kesulitan masuk kedalam game atau gangguan koneksi, update seringkali menimbulkan eror. lalu "card, diamond, reward, pendant, get, suck." dapat memperlihatkan pemain tidak mendapatkan reward (card, pendant, diamond) yang seharusnya pemain terima, ini kemungkinan sistem yang tidak adil."
<p align="justify"> 

**4. Kata Terbanyak dalam reviews berkategori Neutral**
<img width="850" height="364" alt="image" src="https://github.com/user-attachments/assets/ebbd3654-ec5c-4b2b-aaa0-c2de9b645a1f" />

<p align="justify"> 
Gambar diatas terdapat "cant, login, server, connect, fix, bug, force (close), log (in), maintenance." pemain sering melaporkan masalah yang dihadapi tanpa emosi positive atau negative. Terdapat "update, new, need, fix, card, gold, pendant." Pemain memberikan reviews untuk menyampaikan apa yang mereka butuhkan dari game.
<p align="justify"> 
  
5. Hasl score dari training model
<p align="justify"> 
Model yang telah dilatih berhasil mencapai performa yang sangat memuaskan dengan tingkat Akurasi sebesar 93.64% dan nilai Loss sebesar 0.3295 pada data uji. Hasil ini menunjukkan bahwa model mampu mengklasifikasikan sentimen ulasan dengan tingkat kesalahan yang sangat rendah.
<p align="justify"> 
  
## Solusi
<p align="justify"> 
Berdasarkan hasil analisis dan performa model yang telah dibangun, berikut adalah solusi  yang ditawarkan untuk tim "Let's Get Rich"
1. Analisis sentimen negatif dan netral secara konsisten menunjuk pada masalah teknis. Upaya yang harus diperbaiki difokuskan pada masalah login, koneksi, dan kualitas update
2. Kembangkan lebih banyak fitur yang mendorong interaksi antar teman, karena ini adalah pendorong sentimen positif.
3. Kata card, diamond, dan reward muncul di kategori positif dan negatif. Oleh karenanya, Pastikan sistemnya adil, transparan, dan tidak ada bug yang membuat pemain merasa tidak mendapatkan hadiah yang seharusnya.
4. pada saat kampanye marketing dapat menonjolkan kata kunci positif seperti fun, easy to play, dan play with friends untuk menarik pengguna baru yang mencari hiburan ringan.
<p align="justify"> 

## Struktur Folder
- `data/`                 : menyimpan dataset mentah yang digunakan dalam proyek
   - `raw_data_lgr.csv`
- `eda/`                  : melakukan Analisis Data Eksplorasi (EDA)
   - `eda.py`
- `saved_model/` : Menyimpan hasil akhir dari proses training  
   - `model_sentimen.h5`
   - `tfidf_vectorizer.pkl`
- `src/` :  memproses data dan model diletakkan di sini.
   - `__init__.py`
   - `extract.py` : Mengambil data dari playstore
   - `load.py` : Proses Training, evaluasi, dan menyimpanan model
   - `predict.py` : melakukan prediksi pada data baru menggunakan model yang sudah disimpan.
   - `transform.py` : mengambil data menta dari file .csv,  memproses data, mulai dari pembersihan teks, pra-pemrosesan, dan labelisasi
- `main.py` :  menjalankan keseluruhan alur kerja atau pipeline proyek.
- `requirements.txt` : package Python yang dibutuhkan agar proyek ini bisa berjalan.
- `Readme.md` : File dokumentasi utama yang menjelaskan proyek ini 

## Cara Menjalankan Proyek
### 1. Menyiapkan Environment
<p align="justify"> 
Sebelum memulai, gunakan virtual environment  agar dependensi proyek terisolasi dengan baik. Untuk membuat dan mengaktifkan lingkungan virtual, jalankan perintah berikut di terminal:
<p align="justify"> 
  
- **Untuk Windows:**
  ```bash
  python -m venv venv
  .\venv\Scripts\activate

  
- **Untuk Linux/mac:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate

### 2. Instalasi Dependensi
 pip install -r requirements.txt

 ### 3. Jalankan proyek
 1. Jalankan main.py
 2. Jika ingin melakukan predksi jalankan predict.py
 3. Jika ingin melihat pola data jalankan eda.py
  
