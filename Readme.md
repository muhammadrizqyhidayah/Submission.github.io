# Bike Sharing Dataset

## Author
**Hadi Fanaee-T**  
Laboratory of Artificial Intelligence and Decision Support (LIAAD), University of Porto  
INESC Porto, Campus da FEUP  
Rua Dr. Roberto Frias, 378  
4200 - 465 Porto, Portugal  

---

## 📌 Background
Bike-sharing systems adalah generasi baru dari penyewaan sepeda tradisional di mana seluruh proses mulai dari keanggotaan, penyewaan, hingga pengembalian dilakukan secara otomatis. 

Saat ini, lebih dari **500 program bike-sharing** di seluruh dunia dengan total lebih dari **500 ribu sepeda** digunakan. Sistem ini memiliki dampak besar pada **lalu lintas, lingkungan, dan kesehatan masyarakat**.

Keunikan dari sistem ini adalah pencatatan data perjalanan, termasuk **durasi perjalanan, lokasi keberangkatan, dan lokasi tujuan**, yang membuatnya menarik untuk penelitian. Dengan demikian, sistem bike-sharing dapat berfungsi sebagai **jaringan sensor virtual** yang memantau mobilitas kota dan mendeteksi peristiwa penting.

---

## 📊 Dataset
Dataset ini mencatat penyewaan sepeda berdasarkan berbagai faktor seperti **musim, kondisi cuaca, hari dalam seminggu, dan jam dalam sehari**. 

Data ini dikumpulkan dari sistem **Capital Bikeshare di Washington D.C., USA** untuk periode **2011-2012** dan diperkaya dengan data cuaca dari [freemeteo.com](http://www.freemeteo.com).

### 📂 Files:
- **`hour.csv`** → Data penyewaan sepeda dalam skala **jam** (17,379 records)
- **`day.csv`** → Data penyewaan sepeda dalam skala **hari** (731 records)

### 🔍 Kolom Data:
| Kolom | Deskripsi |
|--------|------------|
| `instant` | Indeks data |
| `dteday` | Tanggal |
| `season` | Musim (1: Spring, 2: Summer, 3: Fall, 4: Winter) |
| `yr` | Tahun (0: 2011, 1: 2012) |
| `mnth` | Bulan (1-12) |
| `hr` | Jam (0-23, hanya untuk `hour.csv`) |
| `holiday` | Hari libur atau bukan (1: Ya, 0: Tidak) |
| `weekday` | Hari dalam seminggu |
| `workingday` | Hari kerja atau bukan (1: Ya, 0: Tidak) |
| `weathersit` | Kondisi cuaca: <br> 1️⃣ Cerah/berawan ringan <br> 2️⃣ Kabut/berawan <br> 3️⃣ Hujan ringan/salju ringan <br> 4️⃣ Hujan deras/salju tebal |
| `temp` | Suhu (dinormalisasi ke skala 0-1) |
| `atemp` | Suhu terasa (dinormalisasi) |
| `hum` | Kelembapan udara (dinormalisasi) |
| `windspeed` | Kecepatan angin (dinormalisasi) |
| `casual` | Jumlah pengguna tidak terdaftar |
| `registered` | Jumlah pengguna terdaftar |
| `cnt` | **Total penyewaan sepeda** (casual + registered) |

---

## 🔥 Tugas Terkait
### 1️⃣ **Regression**
Prediksi jumlah penyewaan sepeda berdasarkan faktor lingkungan dan musim.

### 2️⃣ **Event & Anomaly Detection**
Analisis bagaimana jumlah penyewaan sepeda terkait dengan **kejadian besar di kota** seperti **badai, festival, atau liburan**.

📌 Contoh: Query **"2012-10-30 washington d.c."** di Google mengarah pada kejadian **Hurricane Sandy**, yang berdampak signifikan pada jumlah penyewaan sepeda.

---

## ⚖️ Lisensi & Sitasi
Jika Anda menggunakan dataset ini dalam publikasi, mohon kutip referensi berikut:

> **Fanaee-T, Hadi, and Gama, Joao**. *"Event labeling combining ensemble detectors and background knowledge"*, Progress in Artificial Intelligence (2013): 1-15, Springer Berlin Heidelberg. [DOI:10.1007/s13748-013-0040-3](http://dx.doi.org/10.1007/s13748-013-0040-3)

```bibtex
@article{
  year={2013},
  journal={Progress in Artificial Intelligence},
  title={Event labeling combining ensemble detectors and background knowledge},
  publisher={Springer Berlin Heidelberg},
  author={Fanaee-T, Hadi and Gama, Joao},
  pages={1-15}
}
```

---

## 📬 Kontak
📧 Untuk informasi lebih lanjut tentang dataset ini, silakan hubungi **Hadi Fanaee-T**  
✉️ [hadi.fanaee@fe.up.pt](mailto:hadi.fanaee@fe.up.pt)

🚀 **Selamat menganalisis!**