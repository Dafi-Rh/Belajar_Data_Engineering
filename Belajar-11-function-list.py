# Belajar Python Day 11 - Function dan List
# Materi hari ini: function yang menerima list, loop di dalam function,
# counter/total, return hasil, max(), dan mencari nilai terbesar/terkecil.

# 1. Function untuk menjumlahkan isi list
def jumlahkan(angka):
    total = 0

    for nilai in angka:
        total = total + nilai

    return total

hasil = jumlahkan([5, 3, 7, 2])
print(hasil)

hasil2 = jumlahkan([hasil, 3])
print(hasil2)


# 2. Function mencari nilai terbesar dengan max()
def terbesar(angka):
    return max(angka)

hasil = terbesar([4, 2, 5, 6, 8])
print(hasil)


# 3. Function mencari nilai terbesar tanpa max()
def terbesar(angka):
    terbesar = angka[0]

    for nilai in angka:
        if nilai > terbesar:
            terbesar = nilai

    return terbesar

hasil = terbesar([4, 2, 5, 6, 8])
print(hasil)


# 4. Function mencari nilai terkecil tanpa min()
def terkecil(angka):
    terkecil = angka[0]

    for nilai in angka:
        if nilai < terkecil:
            terkecil = nilai

    return terkecil

hasil = terkecil([4, 2, 5, 6, 8])
print(hasil)
