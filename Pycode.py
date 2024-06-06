import pandas as pd

# Membuat data dummy
data = {
    "Bulan": ["Januari", "Februari", "Maret", "April", "Mei", "Juni"],
    "Anggaran": [10000, 15000, 20000, 25000, 30000, 35000],
    "Aktual": [9000, 16000, 19000, 26000, 31000, 34000]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menambahkan kolom perbedaan
df["Perbedaan"] = df["Aktual"] - df["Anggaran"]

# Menyimpan DataFrame ke file CSV
df.to_csv("C:/Users/DELL/AppData/Local/anggaran_vs_aktual.csv", index=False)

# Membaca data dari file CSV
df = pd.read_csv("C:/Users/DELL/AppData/Local/anggaran_vs_aktual.csv")

# Menampilkan data
print(df)

# Melakukan analisis sederhana
total_anggaran = df["Anggaran"].sum()
total_aktual = df["Aktual"].sum()
total_perbedaan = df["Perbedaan"].sum()

print(f"Total Anggaran: {total_anggaran}")
print(f"Total Aktual: {total_aktual}")
print(f"Total Perbedaan: {total_perbedaan}")

import matplotlib.pyplot as plt

# Plot Anggaran vs Aktual
plt.figure(figsize=(10, 6))
plt.plot(df["Bulan"], df["Anggaran"], marker='o', label="Anggaran")
plt.plot(df["Bulan"], df["Aktual"], marker='o', label="Aktual")
plt.xlabel("Bulan")
plt.ylabel("Nilai")
plt.title("Perbandingan Anggaran vs Aktual")
plt.legend()
plt.grid(True)
plt.show()

# Plot Perbedaan
plt.figure(figsize=(10, 6))
plt.bar(df["Bulan"], df["Perbedaan"], color='orange')
plt.xlabel("Bulan")
plt.ylabel("Perbedaan")
plt.title("Perbedaan antara Anggaran dan Aktual")
plt.grid(True)
plt.show()

# Menambahkan kolom perbedaan
df["Perbedaan"] = df["Aktual"] - df["Anggaran"]

# Menyimpan DataFrame ke file CSV
df.to_csv("C:/Users/DELL/AppData/Local/anggaran_vs_aktual.csv", index=False)

# Membaca data dari file CSV
df = pd.read_csv("C:/Users/DELL/AppData/Local/anggaran_vs_aktual.csv")

# Plot Column Chart untuk Anggaran dan Aktual
plt.figure(figsize=(10, 6))
width = 0.4  # Lebar dari setiap bar
x = range(len(df["Bulan"]))  # Lokasi untuk setiap bar

# Membuat bar untuk Anggaran dan Aktual
plt.bar(x, df["Anggaran"], width=width, label="Anggaran", align='center')
plt.bar([p + width for p in x], df["Aktual"], width=width, label="Aktual", align='center')

# Mengatur posisi x-ticks
plt.xticks([p + width / 2 for p in x], df["Bulan"])

# Menambahkan label dan judul
plt.xlabel("Bulan")
plt.ylabel("Nilai")
plt.title("Perbandingan Anggaran dan Aktual")
plt.legend()

# Menampilkan grid
plt.grid(axis='y')

# Menampilkan chart
plt.show()

# Plot Column Chart untuk Perbedaan
plt.figure(figsize=(10, 6))
plt.bar(df["Bulan"], df["Perbedaan"], color='orange', width=0.4)
plt.xlabel("Bulan")
plt.ylabel("Perbedaan")
plt.title("Perbedaan antara Anggaran dan Aktual")
plt.grid(axis='y')

# Menampilkan chart
plt.show()

# Menampilkan data dalam bentuk tabel menggunakan Matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('tight')
ax.axis('off')

# Membuat tabel
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

# Menampilkan tabel
plt.title("Tabel Anggaran vs Aktual")
plt.show()

# Membuat area chart
plt.figure(figsize=(10, 6))

# Plot area untuk Anggaran
plt.fill_between(df["Bulan"], df["Anggaran"], alpha=0.5, label='Anggaran')

# Plot area untuk Aktual
plt.fill_between(df["Bulan"], df["Aktual"], alpha=0.5, label='Aktual')

# Menambahkan judul dan label
plt.title("Area Chart Anggaran vs Aktual")
plt.xlabel("Bulan")
plt.ylabel("Nilai")
plt.legend()

# Menampilkan grid
plt.grid(True)

# Menampilkan plot
plt.show()