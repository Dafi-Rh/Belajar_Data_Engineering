# PYTHON DAY 23
# Materi: List, Tuple, Function, Filtering, Parameter, Sorting

def rapor(nama, nilai):
    hasil = []
    for siswa, angka in zip(nama, nilai):
        if angka >= 90:
            hasil.append((siswa, angka, "A"))
        elif angka >= 75:
            hasil.append((siswa, angka, "B"))
        elif angka >= 60:
            hasil.append((siswa, angka, "C"))
        else:
            hasil.append((siswa, angka, "D"))
    return hasil

data = rapor(
    ["Owi", "Joni", "Wowo", "Didi", "Eko"],
    [80, 65, 90, 70, 100]
)

print(data)

# Index tuple:
# siswa[0] = nama
# siswa[1] = nilai
# siswa[2] = grade

# Mencari nilai tertinggi
tertinggi = 0
for siswa in data:
    if siswa[1] > tertinggi:
        tertinggi = siswa[1]
print(tertinggi)

# Mencari nama dan nilai tertinggi
tertinggi = 0
nama_tertinggi = ""
for siswa in data:
    if siswa[1] > tertinggi:
        tertinggi = siswa[1]
        nama_tertinggi = siswa[0]
print(nama_tertinggi, tertinggi)

# Mencari nilai terendah
terendah = 999999
nama_terendah = ""
for siswa in data:
    if siswa[1] < terendah:
        terendah = siswa[1]
        nama_terendah = siswa[0]
print(nama_terendah, terendah)

# Filter nilai >= 80
hasil = []
for siswa in data:
    if siswa[1] >= 80:
        print(siswa)

hasil = []
for siswa in data:
    if siswa[1] >= 80:
        hasil.append((siswa[0], siswa[1]))
print(hasil)

# Nama siswa grade A
hasil = []
for siswa in data:
    if siswa[2] == "A":
        hasil.append(siswa[0])
print(hasil)

# Nama dan nilai siswa nilai >= 75
hasil = []
for siswa in data:
    if siswa[1] >= 75:
        hasil.append((siswa[0], siswa[1]))
print(hasil)

# Nama dan grade siswa nilai < 75
hasil = []
for siswa in data:
    if siswa[1] < 75:
        hasil.append((siswa[0], siswa[2]))
print(hasil)

# Nama siswa nilai >= 80
hasil = []
for siswa in data:
    if siswa[1] >= 80:
        hasil.append(siswa[0])
print(hasil)

# Grade B atau C
hasil = []
for siswa in data:
    if siswa[2] == "B" or siswa[2] == "C":
        hasil.append((siswa[0], siswa[1]))
print(hasil)

# sorted()
angka = [6, 9, 3, 5, 2]
print(sorted(angka))
print(sorted(angka, reverse=True))
print(angka)

# Sorting data siswa berdasarkan nilai terbesar -> terkecil
hasil = []
for siswa in data:
    if siswa[1] < 80:
        hasil.append(siswa)

hasil = sorted(hasil, key=lambda siswa: siswa[1], reverse=True)
print(hasil)

def urutkan_nilai(data):
    hasil = sorted(data, key=lambda siswa: siswa[1], reverse=True)
    return hasil

print(urutkan_nilai(data))

def cari_b(data):
    hasil = []
    for daftar in data:
        if daftar[2] == "B":
            hasil.append(daftar[0])
    return hasil

print(cari_b(data))

def cari_grade(data, grade):
    hasil = []
    for daftar in data:
        if daftar[2] == grade:
            hasil.append(daftar[0])
    return hasil

print(cari_grade(data, "A"))
print(cari_grade(data, "C"))

def cari_nilai(data, batas):
    hasil = []
    for daftar in data:
        if daftar[1] >= batas:
            hasil.append(daftar[0])
    return hasil

print(cari_nilai(data, 80))
print(cari_nilai(data, 60))
print(cari_nilai(data, 75))

def cari_siswa(data, batas, grade):
    hasil = []
    for daftar in data:
        if daftar[1] >= batas and daftar[2] == grade:
            hasil.append(daftar[0])
    return hasil

print(cari_siswa(data, 90, "A"))
print(cari_siswa(data, 100, "A"))

# Konsep Day 23:
# list dapat menampung banyak elemen
# tuple menyimpan beberapa data dalam satu elemen
# siswa[0], siswa[1], siswa[2] = indexing tuple
# for + if untuk filtering
# append() untuk mengumpulkan hasil
# function dengan parameter
# sorted() membuat hasil baru
# reverse=True = besar -> kecil
# key menentukan dasar pengurutan
# lambda = fungsi kecil/sekali pakai
