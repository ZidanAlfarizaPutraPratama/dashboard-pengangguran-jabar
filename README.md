# 📊 Dashboard Tingkat Pengangguran Terbuka (TPT) Jawa Barat

[![Streamlit](https://img.shields.io/badge/Streamlit-1.35.0-red?logo=streamlit)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Dashboard ini menyajikan data **Tingkat Pengangguran Terbuka (TPT)** di Provinsi **Jawa Barat** dari tahun ke tahun berdasarkan data resmi dari [data.jabarprov.go.id](https://data.jabarprov.go.id). Dibangun dengan **Streamlit**, **Pandas**, dan **Altair**, dashboard ini memungkinkan pengguna melihat tren pengangguran secara interaktif dan informatif.

---

## 📁 Struktur Proyek

```
📦tpt-jabar-dashboard/
├── 📄 app.py # Aplikasi utama Streamlit
├── 📁 data.jabarprov.go.id/ # Folder data
│ └── bps-od_20206_tingkat_pengangguran_terbuka__prov_di_indonesia_data.csv
├── 📄 requirements.txt # Daftar dependensi Python
├── 📄 LICENSE # Lisensi MIT
└── 📄 README.md # Dokumentasi proyek
```

---

## ✨ Fitur Utama

- 📅 Menampilkan daftar tahun dengan data tersedia
- 📈 Statistik deskriptif (mean, std, min, max)
- 📉 Grafik tren pengangguran interaktif per tahun
- 📊 Tabel ringkasan TPT tahunan

---

## ▶️ Cara Menjalankan Aplikasi

### 1. Kloning repositori
```
git clone https://github.com/ZidanAlfarizaPutraPratama/dashboard-pengangguran-jabar.git
cd tpt-jabar-dashboard
2. Buat dan aktifkan virtual environment (opsional tapi disarankan)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate     # Windows
3. Install dependensi
bash
Copy
Edit
pip install -r requirements.txt
```

4. Jalankan aplikasi
```
streamlit run app.py
```
💾 Sumber Data
Data diambil dari portal resmi Pemerintah Provinsi Jawa Barat:

📎 Tingkat Pengangguran Terbuka (TPT) - data.jabarprov.go.id

📃 Lisensi
Proyek ini dilisensikan di bawah MIT License. Silakan gunakan, modifikasi, dan distribusikan proyek ini dengan tetap mencantumkan atribusi.

📸 Tampilan Dashboard
![image](https://github.com/user-attachments/assets/37cec99f-c4a0-425f-964f-686db9b15c4d)
![image](https://github.com/user-attachments/assets/e88fcc21-d9d1-4077-b169-4ada1981462b)
![image](https://github.com/user-attachments/assets/5c946882-b400-4c9d-948b-7f332676b3da)





🙋‍♀️ Kontribusi
Kontribusi sangat terbuka! Silakan ajukan issue atau pull request untuk menambahkan fitur atau perbaikan.
