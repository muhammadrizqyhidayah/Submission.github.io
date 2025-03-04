import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load Data
day_df = pd.read_csv("data/data_1.csv")
hour_df = pd.read_csv("data/data_2.csv")

# Convert date column to datetime format
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Mapping season numbers to labels
season_labels = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
day_df["season_label"] = day_df["season"].map(season_labels)

# Inisialisasi session state untuk mode terang/gelap
if "theme" not in st.session_state:
    st.session_state["theme"] = "light"

# Pilihan tema di sidebar
theme_choice = st.sidebar.radio("\U0001F317 Pilih Tema", ["Light", "Dark"])
st.session_state["theme"] = "dark" if theme_choice == "Dark" else "light"

# Terapkan CSS untuk tema
bg_color, text_color = ("#0e1117", "#ffffff") if st.session_state["theme"] == "dark" else ("#ffffff", "#000000")
st.markdown(
    f"""
    <style>
        body, .stApp {{
            background-color: {bg_color};
            color: {text_color};
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: {text_color};
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Judul Aplikasi
st.title("\U0001F4CA Analisis Data Penyewaan Sepeda")
st.write("Aplikasi ini menyajikan analisis data penyewaan sepeda berdasarkan berbagai faktor seperti tren waktu, musim, dan jam dalam sehari.")

# Sidebar Menu
menu = st.sidebar.radio("Pilih Analisis:", ["Ringkasan Data", "Tren Penyewaan", "Penyewaan Berdasarkan Musim", "Penyewaan Berdasarkan Jam", "Clustering Penyewaan", "RFM Analysis"])

# Date Picker
st.sidebar.subheader("\U0001F4C5 Pilih Rentang Tanggal")
min_date = day_df['dteday'].min().date()
max_date = day_df['dteday'].max().date()

start_date = st.sidebar.date_input("Tanggal Mulai", min_date, min_value=min_date, max_value=max_date)
end_date = st.sidebar.date_input("Tanggal Akhir", max_date, min_value=min_date, max_value=max_date)

if start_date > end_date:
    st.sidebar.error("\u26A0\uFE0F Tanggal Akhir harus setelah Tanggal Mulai!")

start_date, end_date = pd.to_datetime(start_date), pd.to_datetime(end_date)

# Filter data berdasarkan tanggal
filtered_day_df = day_df[(day_df['dteday'] >= start_date) & (day_df['dteday'] <= end_date)].copy()
filtered_hour_df = hour_df[(hour_df['dteday'] >= start_date) & (hour_df['dteday'] <= end_date)].copy()

# Set seaborn theme
sns.set_theme(style="darkgrid" if st.session_state["theme"] == "dark" else "whitegrid")

# Analisis Clustering Penyewaan
if menu == "Clustering Penyewaan":
    st.header("Clustering Penyewaan Sepeda")
    
    # Menggunakan KMeans untuk clustering berdasarkan jumlah penyewaan per jam
    hourly_avg = filtered_hour_df.groupby('hr')['cnt'].mean().reset_index()
    hourly_avg_scaled = StandardScaler().fit_transform(hourly_avg[['cnt']])
    
    # Fit KMeans
    kmeans = KMeans(n_clusters=3, random_state=42)
    hourly_avg['Cluster'] = kmeans.fit_predict(hourly_avg_scaled)
    
    # Visualisasi clustering
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.scatterplot(data=hourly_avg, x='hr', y='cnt', hue='Cluster', palette='viridis', ax=ax)
    ax.set_title("Clustering Penyewaan Sepeda Berdasarkan Jam")
    ax.set_xlabel("Jam")
    ax.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig)
    
    st.subheader("📌 Kesimpulan")
    st.write("Clustering berdasarkan jam menunjukkan kelompok waktu dengan penyewaan sepeda tinggi dan rendah.")

# Analisis RFM (Recency, Frequency, Monetary)
elif menu == "RFM Analysis":
    st.header("Analisis RFM (Recency, Frequency, Monetary)")
    
    # Recency: Tanggal terakhir penyewaan
    recent_date = filtered_day_df['dteday'].max()
    filtered_day_df['Recency'] = (recent_date - filtered_day_df['dteday']).dt.days
    
    # Frequency: Jumlah penyewaan per pengguna (misalnya, berdasarkan 'instant' sebagai ID)
    frequency = filtered_day_df.groupby('instant')['cnt'].count().reset_index(name='Frequency')
    
    # Monetary: Total penyewaan yang dilakukan oleh setiap pengguna
    monetary = filtered_day_df.groupby('instant')['cnt'].sum().reset_index(name='Monetary')
    
    # Gabungkan data RFM
    rfm = pd.merge(frequency, monetary, on='instant')
    rfm = pd.merge(rfm, filtered_day_df[['instant', 'Recency']].drop_duplicates(), on='instant')
    
    st.write(rfm.head())
    
    st.subheader("📌 Kesimpulan")
    st.write("Analisis RFM membantu untuk mengidentifikasi pengguna yang lebih aktif dan berpotensi lebih berharga.")

# Analisis lainnya
elif menu == "Ringkasan Data":
    st.header("\U0001F4CB Ringkasan Data")
    st.write("### Data Harian (Setelah Filter Tanggal)")
    st.dataframe(filtered_day_df.head())
    st.write("### Data Per Jam (Setelah Filter Tanggal)")
    st.dataframe(filtered_hour_df.head())
    st.write("### Statistik Deskriptif")
    st.write(filtered_day_df.describe())

elif menu == "Tren Penyewaan":
    st.header("\U0001F4C8 Tren Penyewaan Sepeda Sepanjang Tahun")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(filtered_day_df['dteday'], filtered_day_df['cnt'], label='Total Penyewaan', color='blue')
    ax.set_xlabel("Tanggal")
    ax.set_ylabel("Jumlah Penyewaan")
    ax.set_title("Tren Penyewaan Sepeda")
    ax.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig)
    
    st.subheader("\U0001F4CC Kesimpulan")
    st.write("Tren penyewaan sepeda menunjukkan pola musiman dengan lonjakan pada bulan tertentu.")

elif menu == "Penyewaan Berdasarkan Musim":
    st.header("\U0001F324 Penyewaan Sepeda Berdasarkan Musim")
    season_counts = filtered_day_df.groupby('season_label')['cnt'].sum()
    
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(season_counts, labels=season_counts.index, autopct='%1.1f%%', 
           colors=['lightblue', 'orange', 'green', 'red'], startangle=140)
    ax.set_title("Distribusi Penyewaan Sepeda Berdasarkan Musim")
    plt.axis('equal')
    st.pyplot(fig)
    
    st.subheader("\U0001F4CC Kesimpulan")
    st.write("Penyewaan lebih tinggi pada musim panas dan gugur.")

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
    
    st.subheader("\U0001F4CC Kesimpulan")
    st.write("Peningkatan signifikan terjadi pada jam sibuk pagi dan sore hari.")
