# Python Day 14 - Remedial Function + List
# Fokus: menguatkan logika, for, if, zip(), append(), counter, return.

# 1. Jumlah nilai lulus
def jumlah_lulus(nilai):
    total = 0
    for angka in nilai:
        if angka >= 75:
            total = total + 1
    return total

print(jumlah_lulus([70, 85, 60, 90, 75, 65]))


# 2. Jumlah nilai gagal
def jumlah_gagal(nilai):
    total = 0
    for angka in nilai:
        if angka < 75:
            total = total + 1
    return total

print(jumlah_gagal([70, 85, 60, 90, 75, 65]))


# 3. Memasangkan nama dan nilai dengan zip()
nama = ["Owi", "Joni", "Wowo", "Didi", "Eko"]
nilai = [70, 85, 60, 90, 75]

print(list(zip(nama, nilai)))


# 4. Mencari nama siswa yang lulus
hasil = []

for orang, angka in zip(nama, nilai):
    if angka >= 75:
        hasil.append(orang)

print(hasil)


# 5. Membungkus logika menjadi function
def siswa_lulus(nama, nilai):
    hasil = []
    for orang, angka in zip(nama, nilai):
        if angka >= 75:
            hasil.append(orang)
    return hasil

hasil = siswa_lulus(nama, nilai)
print(hasil)


# 6. Statistik sederhana
def statistik(angka):
    jumlah = 0
    total = 0
    terbesar = angka[0]
    terkecil = angka[0]

    for nilai in angka:
        jumlah = jumlah + 1
        total = total + nilai

        if nilai > terbesar:
            terbesar = nilai

        if nilai < terkecil:
            terkecil = nilai

    rata_rata = total / jumlah
    return jumlah, total, terbesar, terkecil, rata_rata

data_nilai = [70, 85, 90, 65, 80]
jumlah, total, terbesar, terkecil, rata_rata = statistik(data_nilai)

print("jumlah =", jumlah)
print("total =", total)
print("terbesar =", terbesar)
print("terkecil =", terkecil)
print("rata-rata =", rata_rata)


# 7. Pola penting
# Counter:
jumlah = 0
jumlah = jumlah + 1

# Accumulator:
total = 0
total = total + nilai

# List penampung:
hasil = []
hasil.append(data)


# 8. Latihan remedial mandiri
# A. Buat function jumlah_nilai(nilai) untuk menjumlahkan semua nilai.
# B. Buat function nilai_lulus(nilai) untuk mengembalikan nilai >= 75.
# C. Buat function siswa_gagal(nama, nilai) untuk mengembalikan
#    nama siswa dengan nilai < 75.
# D. Buat function rata_rata_lulus(nilai) untuk menghitung
#    rata-rata nilai yang >= 75.
