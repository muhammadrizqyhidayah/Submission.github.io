import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Load Data
day_df = pd.read_csv("data/data_1.csv")
hour_df = pd.read_csv("data/data_2.csv")

# Convert date column to datetime format
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Inisialisasi session state untuk mode terang/gelap
if "theme" not in st.session_state:
    st.session_state["theme"] = "light"

# Pilihan tema di sidebar
theme_choice = st.sidebar.radio("🌗 Pilih Tema", ["Light", "Dark"])

# Update session state berdasarkan pilihan
st.session_state["theme"] = "dark" if theme_choice == "Dark" else "light"

# Terapkan CSS untuk tema
custom_css = """
    <style>
        body {{
            background-color: {bg_color};
            color: {text_color};
        }}
        .stApp {{
            background-color: {bg_color};
            color: {text_color};
        }}
    </style>
"""

if st.session_state["theme"] == "dark":
    bg_color = "#0e1117"
    text_color = "#ffffff"
else:
    bg_color = "#ffffff"
    text_color = "#000000"

st.markdown(custom_css.format(bg_color=bg_color, text_color=text_color), unsafe_allow_html=True)

# Judul Aplikasi
st.title("📊 Analisis Data Penyewaan Sepeda")
st.write("Aplikasi ini menyajikan analisis data penyewaan sepeda berdasarkan berbagai faktor seperti tren waktu, musim, dan jam dalam sehari.")

# Sidebar Menu
menu = st.sidebar.radio("Pilih Analisis:", ["Ringkasan Data", "Tren Penyewaan", "Penyewaan Berdasarkan Musim", "Penyewaan Berdasarkan Jam"])

# Date Picker
st.sidebar.subheader("📅 Pilih Rentang Tanggal")

# Konversi min dan max date ke tipe date
min_date = day_df['dteday'].min().date()
max_date = day_df['dteday'].max().date()

start_date = st.sidebar.date_input("Tanggal Mulai", min_date, min_value=min_date, max_value=max_date)
end_date = st.sidebar.date_input("Tanggal Akhir", max_date, min_value=min_date, max_value=max_date)

# Pastikan end_date tidak lebih kecil dari start_date
if start_date > end_date:
    st.sidebar.error("⚠️ Tanggal Akhir harus setelah Tanggal Mulai!")

# Konversi ke datetime64 untuk filter data
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter data berdasarkan tanggal yang dipilih
filtered_day_df = day_df[(day_df['dteday'] >= start_date) & (day_df['dteday'] <= end_date)]
filtered_hour_df = hour_df[(hour_df['dteday'] >= start_date) & (hour_df['dteday'] <= end_date)]

if menu == "Ringkasan Data":
    st.header("📋 Ringkasan Data")
    st.write("### Data Harian (Setelah Filter Tanggal)")
    st.dataframe(filtered_day_df.head())
    st.write("### Data Per Jam (Setelah Filter Tanggal)")
    st.dataframe(filtered_hour_df.head())
    st.write("### Statistik Deskriptif")
    st.write(filtered_day_df.describe())

elif menu == "Tren Penyewaan":
    st.header("📈 Tren Penyewaan Sepeda Sepanjang Tahun")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(filtered_day_df['dteday'], filtered_day_df['cnt'], label='Total Penyewaan', color='blue')
    ax.set_xlabel("Tanggal")
    ax.set_ylabel("Jumlah Penyewaan")
    ax.set_title("Tren Penyewaan Sepeda")
    ax.legend()
    st.pyplot(fig)

elif menu == "Penyewaan Berdasarkan Musim":
    st.header("🌤️ Penyewaan Sepeda Berdasarkan Musim")
    season_labels = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    filtered_day_df['season_label'] = filtered_day_df['season'].map(season_labels)
    season_counts = filtered_day_df.groupby('season_label')['cnt'].sum()
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(season_counts, labels=season_counts.index, autopct='%1.1f%%', colors=['lightblue', 'orange', 'green', 'red'], startangle=140)
    ax.set_title("Distribusi Penyewaan Sepeda Berdasarkan Musim")
    st.pyplot(fig)

elif menu == "Penyewaan Berdasarkan Jam":
    st.header("⏰ Rata-rata Penyewaan Sepeda Berdasarkan Jam")
    hourly_avg = filtered_hour_df.groupby('hr')['cnt'].mean()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(hourly_avg.index, hourly_avg, marker='o', linestyle='-', color='purple')
    ax.set_xlabel("Jam")
    ax.set_ylabel("Rata-rata Penyewaan Sepeda")
    ax.set_title("Penyewaan Sepeda per Jam")
    ax.set_xticks(range(0, 24))
    ax.grid()
    st.pyplot(fig)