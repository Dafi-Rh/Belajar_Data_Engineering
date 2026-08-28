# Belajar Python Day 13 - Function + List + Filtering

# 1. Function untuk mengambil nilai lulus
def nilai_lulus(nilai):
    hasil = []
    for angka in nilai:
        if angka >= 75:
            hasil.append(angka)
    return hasil

print(nilai_lulus([50, 80, 65, 90, 75, 60]))


# 2. Function untuk mengambil nilai gagal
def nilai_gagal(nilai):
    hasil = []
    for angka in nilai:
        if angka < 75:
            hasil.append(angka)
    return hasil

print(nilai_gagal([50, 80, 65, 90, 75, 60]))


# 3. Menggunakan dua function pada data yang sama
data = [50, 80, 65, 90, 75, 60]

print("lulus =", nilai_lulus(data))
print("gagal =", nilai_gagal(data))


# 4. Function menghitung jumlah siswa yang lulus
def jumlah_lulus(nilai):
    total = 0
    for angka in nilai:
        if angka >= 75:
            total = total + 1
    return total

print(jumlah_lulus([50, 80, 65, 90, 75, 60]))
