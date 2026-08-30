# Python Day 15 - Remedial Function + List + zip()

# 1. Counter: menghitung jumlah nilai lulus
def jumlah_lulus(nilai):
    total = 0
    for angka in nilai:
        if angka >= 75:
            total = total + 1
    return total

print(jumlah_lulus([80, 60, 90, 55, 75, 65]))

# 2. Filtering nilai lulus
def nilai_lulus(nilai):
    hasil = []
    for angka in nilai:
        if angka >= 75:
            hasil.append(angka)
    return hasil

print(nilai_lulus([80, 60, 90, 55, 75, 65]))

# 3. Filtering nilai gagal
def nilai_gagal(nilai):
    hasil = []
    for angka in nilai:
        if angka < 75:
            hasil.append(angka)
    return hasil

print(nilai_gagal([80, 60, 90, 55, 75, 65]))

# 4. zip() memasangkan dua list
nama = ["Owi", "Joni", "Wowo", "Didi", "Eko"]
nilai = [70, 85, 60, 90, 75]
print(list(zip(nama, nilai)))

# 5. Mengambil nama siswa lulus
hasil = []
for orang, angka in zip(nama, nilai):
    if angka >= 75:
        hasil.append(orang)
print(hasil)

# 6. Function siswa_lulus()
def siswa_lulus(nama, nilai):
    hasil = []
    for orang, angka in zip(nama, nilai):
        if angka >= 75:
            hasil.append(orang)
    return hasil

print(siswa_lulus(nama, nilai))

# 7. Rata-rata siswa lulus
def rata_rata_lulus(nama, nilai):
    jumlah = 0
    total = []
    for orang, angka in zip(nama, nilai):
        if angka >= 75:
            jumlah = jumlah + angka
            total.append(angka)
    return jumlah / len(total)

print(rata_rata_lulus(
    ["A", "B", "C", "D", "E"],
    [60, 80, 90, 70, 100]
))

# 8. Nilai tertinggi
def nilai_tertinggi(nilai):
    tertinggi = 0
    for angka in nilai:
        if angka > tertinggi:
            tertinggi = angka
    return tertinggi

print(nilai_tertinggi([40, 70, 85, 90, 55, 100]))

# 9. Nilai terendah
def nilai_terendah(nilai):
    terendah = 9999
    for angka in nilai:
        if angka < terendah:
            terendah = angka
    return terendah

print(nilai_terendah([40, 70, 85, 90, 55, 100]))

# 10. Nama + nilai tertinggi
def siswa_nilai_tertinggi(nama, nilai):
    tertinggi = 0
    nama_tertinggi = ""
    for orang, angka in zip(nama, nilai):
        if angka > tertinggi:
            tertinggi = angka
            nama_tertinggi = orang
    return nama_tertinggi, tertinggi

print(siswa_nilai_tertinggi(
    ["A", "B", "C", "D", "E"],
    [60, 80, 90, 70, 100]
))

# 11. Nama + nilai terendah
def siswa_nilai_terendah(nama, nilai):
    terendah = 9999
    nama_terendah = ""
    for orang, angka in zip(nama, nilai):
        if angka < terendah:
            terendah = angka
            nama_terendah = orang
    return nama_terendah, terendah

print(siswa_nilai_terendah(
    ["A", "B", "C", "D", "E"],
    [80, 60, 95, 70, 90]
))

# Pola berpikir:
# menghitung -> counter
# menjumlahkan -> accumulator
# menyimpan -> list + append()
# memasangkan -> zip()
# memilih -> if
# mengulang -> for
# mengembalikan -> return

# Latihan remedial mandiri:
# A. jumlah_gagal(nilai)
# B. siswa_gagal(nama, nilai)
# C. rata_rata_gagal(nama, nilai)
# D. siswa_nilai_tertinggi(nama, nilai)
# E. siswa_nilai_terendah(nama, nilai)
