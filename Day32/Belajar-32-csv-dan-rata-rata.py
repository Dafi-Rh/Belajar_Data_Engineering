# ==========================================
# Day 32 - Membaca CSV dan Menghitung Rata-Rata
# ==========================================

import csv

# 1. Pemanasan Nested Dictionary
siswa_dict = {
    "A": {"nama": "Wowo", "nilai": 90},
    "B": {"nama": "Joni", "nilai": 65}
}
print("Nilai Wowo dari nested dict:", siswa_dict["A"]["nilai"])

# 2. Membaca File siswa.csv
print("\n--- Membaca Data dari siswa.csv ---")
with open("siswa.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for baris in reader:
        # Konversi string nilai menjadi integer
        baris["nilai"] = int(baris["nilai"])
        print(baris)

# 3. Menghitung Rata-Rata Nilai Siswa dari CSV
print("\n--- Menghitung Rata-Rata Nilai ---")
jumlah = 0
total = 0

with open("siswa.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for data in reader:
        jumlah += 1
        total += int(data["nilai"])

hasil = total / jumlah
print(f"Jumlah siswa : {jumlah}")
print(f"Total nilai  : {total}")
print(f"Rata-rata    : {hasil}")
