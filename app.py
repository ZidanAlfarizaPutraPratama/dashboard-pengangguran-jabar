import streamlit as st
import pandas as pd
import altair as alt
import os

# === BACA DAN SIAPKAN DATA ===
csv_path = "./data.jabarprov.go.id/bps-od_20206_tingkat_pengangguran_terbuka__prov_di_indonesia_data.csv"
if not os.path.exists(csv_path):
    st.error(f"File CSV tidak ditemukan di path: {csv_path}")
    st.stop()

# Nama kolom manual karena tidak ada header
cols = ['kode_provinsi', 'kode_lain', 'nama_provinsi', 'indeks_tpt', 'satuan', 'tahun']
df = pd.read_csv(csv_path, names=cols, header=None)

# Filter hanya provinsi JAWA BARAT dan rapikan format
df['nama_provinsi'] = df['nama_provinsi'].str.strip().str.upper()
df = df[df['nama_provinsi'] == 'JAWA BARAT']

# Pastikan kolom tahun & indeks numerik
df['tahun'] = pd.to_numeric(df['tahun'], errors='coerce').astype('Int64')
df['indeks_tpt'] = pd.to_numeric(df['indeks_tpt'], errors='coerce')
df.dropna(subset=['tahun', 'indeks_tpt'], inplace=True)

# === DASHBOARD ===
st.title("📊 Dashboard Tingkat Pengangguran Jawa Barat")

# Daftar Tahun Tersedia
st.subheader("📅 Tahun Data Tersedia")
tahun_tersedia = df['tahun'].dropna().astype(int).unique().tolist()
tahun_tersedia.sort()
st.write(tahun_tersedia)  # Contoh output: [2018, 2019, 2020, 2021, 2022, 2023, 2024]

# Statistik Deskriptif
st.subheader("📈 Statistik Deskriptif Tingkat Pengangguran (%)")
st.dataframe(df[['tahun', 'indeks_tpt']].describe().round(2), use_container_width=True)

# Grafik Tren per Tahun
st.subheader("📉 Tren Pengangguran Jawa Barat")
chart = alt.Chart(df).mark_line(point=True).encode(
    x=alt.X('tahun:O', title='Tahun'),
    y=alt.Y('indeks_tpt:Q', title='Tingkat Pengangguran (%)'),
    tooltip=['tahun', alt.Tooltip('indeks_tpt', format=".2f")]
).properties(
    width=700,
    height=400
)
st.altair_chart(chart, use_container_width=True)

# Rata-rata per Tahun (optional)
st.subheader("📊 Tabel Ringkasan per Tahun")
df_tahun = df[['tahun', 'indeks_tpt']].sort_values(by='tahun').reset_index(drop=True)
df_tahun['tahun'] = df_tahun['tahun'].astype(int)
st.table(df_tahun)
