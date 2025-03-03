import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Aplikasi
st.title("Analisis Penyewaan Sepeda")

# Load dataset
day_df = pd.read_csv("Data/day.csv")
hour_df = pd.read_csv("Data/hour.csv")

# Konversi kolom tanggal
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Sidebar untuk filter
date_range = st.sidebar.date_input("Pilih Rentang Tanggal", [day_df['dteday'].min(), day_df['dteday'].max()])

# Filter data berdasarkan rentang tanggal
if isinstance(date_range, list) and len(date_range) == 2:
    day_df = day_df[(day_df['dteday'] >= pd.Timestamp(date_range[0])) & (day_df['dteday'] <= pd.Timestamp(date_range[1]))]

# Analisis berdasarkan musim
st.subheader("Distribusi Penyewaan Sepeda Berdasarkan Musim")
season_labels = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
day_df['season_label'] = day_df['season'].map(season_labels)
season_counts = day_df.groupby('season_label')['cnt'].sum()
fig, ax = plt.subplots()
ax.pie(season_counts, labels=season_counts.index, autopct='%1.1f%%', colors=['lightblue', 'orange', 'green', 'red'])
ax.set_title("Distribusi Penyewaan Sepeda Berdasarkan Musim")
st.pyplot(fig)

# Rata-rata Penyewaan Sepeda Berdasarkan Jam
st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Jam dalam Sehari")
hourly_avg = hour_df.groupby('hr')['cnt'].mean()
fig, ax = plt.subplots()
ax.plot(hourly_avg.index, hourly_avg, marker='o', linestyle='-', color='purple')
ax.set_xlabel('Jam')
ax.set_ylabel('Rata-rata Penyewaan Sepeda')
ax.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Jam dalam Sehari')
ax.grid()
st.pyplot(fig)


# Tren Penyewaan Sepeda
st.subheader("Tren Penyewaan Sepeda Sepanjang Tahun")
fig, ax = plt.subplots()
ax.plot(day_df['dteday'], day_df['cnt'], label='Total Penyewaan', color='blue')
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Tren Penyewaan Sepeda Sepanjang Tahun")
ax.legend()
st.pyplot(fig)

st.write("Dashboard ini membantu memahami pola penyewaan sepeda berdasarkan musim, kondisi cuaca, dan tren tahunan.")
