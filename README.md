```markdown
# 📚 Sistem Manajemen Perpustakaan (MVC - Python CustomTkinter)

Aplikasi desktop **Sistem Manajemen Perpustakaan** berbasis Python yang dibangun mengimplementasikan arsitektur **Model-View-Controller (MVC)**, pustaka antarmuka pengguna **CustomTkinter**, serta basis data **MySQL**[cite: 3]. Proyek ini dikembangkan dengan menerapkan praktik DevOps terkini, termasuk pengujian otomatis (*Continuous Integration*) via GitHub Actions dan pemaketkan aplikasi mandiri (*executable*) via PyInstaller[cite: 1, 3].

---

## 🛠️ Fitur Utama

* **Autentikasi & Otorisasi (RBAC)**: Sistem *login* aman dengan enkripsi kata sandi berbasis `SHA-256` (`hashlib`) serta pembagian hak akses (*Role-Based Access Control*) antara **Admin** (akses CRUD penuh) dan **Anggota** (*read-only*)[cite: 1, 2].
* **Manajemen Katalog Buku**: Operasi Tambah, Baca, Edit, dan Hapus (CRUD) data buku yang terhubung secara *real-time* ke basis data MySQL[cite: 1, 2].
* **Automated CI/CD Pipeline**: Terintegrasi otomatis dengan **GitHub Actions** untuk menjalankan pemeriksaan *linter* (`flake8`) dan pengujian unit (`pytest`) setiap kali terdapat aktivitas *push* atau *pull request*[cite: 1, 2, 6].
* **Standalone Executable Packaging**: Dapat dijalankan secara langsung di OS Windows tanpa memerlukan instalasi interpreter Python atau pustaka tambahan melalui berkas `.exe` hasil kompilasi **PyInstaller**[cite: 3].

---

## 📁 Struktur Direktori Proyek (MVC Architecture)

```text
TugasModul3_RPL/
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml     # Konfigurasi GitHub Actions CI Pipeline
├── config/
│   └── database.py             # Konektor dan konfigurasi basis data MySQL
├── controllers/                # Pengendali logika bisnis aplikasi
│   ├── auth_controller.py
│   └── buku_controller.py
├── models/                     # Modul kueri dan interaksi data MySQL
│   ├── user_model.py
│   └── buku_model.py
├── views/                      # Antarmuka pengguna (CustomTkinter & Tkinter TTK)
│   ├── login_view.py
│   └── buku_view.py
├── tests/                      # Skrip pengujian unit (Pytest)
│   ├── test_auth.py
│   └── test_buku.py
├── dist/                       # Artefak kompilasi executable
│   └── AplikasiPerpustakaan.exe
├── main.py                     # Entry point utama aplikasi
├── requirements.txt            # Daftar dependensi pustaka Python
├── .gitignore                  # Konfigurasi pengabaian file Git
└── README.md                   # Dokumentasi teknis proyek

```

---

## ⚙️ Prasyarat & Instalasi

### 1. Persyaratan Sistem

* **Python**: Versi 3.11 atau lebih baru.


* **Database Server**: Laragon / XAMPP (MySQL Service).


* **Git**: Terinstal di sistem lokal.



### 2. Konfigurasi Basis Data MySQL

1. Jalankan *service* **MySQL** di Laragon atau XAMPP.


2. Buka alat manajemen database (HeidiSQL / phpMyAdmin / MySQL CLI) lalu buat basis data baru bernama:
```sql
CREATE DATABASE db_perpustakaan;

```


3. Import atau atur skema tabel `users` dan `buku` sesuai konfigurasi pada folder `config/database.py`.

### 3. Kloning Repositori & Instalasi Dependensi

Buka terminal / PowerShell, lalu jalankan perintah berikut:

```bash
# 1. Kloning repositori dari GitHub
git clone [https://github.com/MuhFikriFachrezziF5212520056/TugasModul3_RPL.git](https://github.com/MuhFikriFachrezziF5212520056/TugasModul3_RPL.git)
cd TugasModul3_RPL

# 2. Buat dan aktifkan lingkungan virtual (Virtual Environment)
python -m venv env
.\env\Scripts\activate

# 3. Instal seluruh dependensi pustaka yang dibutuhkan
pip install -r requirements.txt

```

---

## 🚀 Cara Menjalankan Aplikasi

### Menjalankan Kode Sumber (Source Code)

Dalam kondisi virtual environment aktif, eksekusi file utama:

```bash
python main.py

```

### Menjalankan Aplikasi Executable (.exe)

Kamu juga dapat langsung menjalankan aplikasi tanpa Python melalui file eksekusi yang telah dikompilasi:

* Buka folder `dist/`.


* Klik ganda pada berkas **`AplikasiPerpustakaan.exe`**.



---

## 🧪 Pengujian Kode & Linting (DevOps)

Proyek ini telah dilengkapi dengan pengujian otomatis (*automated testing*):

* **Jalankan Unit Testing (Pytest)**:
```bash
python -m pytest -v

```


* **Jalankan Code Style Check (Flake8 Linter)**:
```bash
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

```



---

## 👨‍💻 Penulis / Pengembang

* **Nama**: Muh. Fikri Fachrezzi
* **NIM / Author ID**: Fikri_056 / MuhFikriFachrezziF5212520056
* **Program Studi**: S1 Sistem Informasi / Teknologi Informasi - Universitas Tadulako

```

```