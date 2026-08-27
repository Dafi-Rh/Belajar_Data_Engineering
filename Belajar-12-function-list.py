# Belajar Python Day 12 - Function + List
# Materi hari ini:
# function yang menerima list, for di dalam function, counter,
# accumulator, max(), mencari terbesar/terkecil manual,
# rata-rata, return, dan unpacking.

def jumlahkan(angka):
    total = 0
    for nilai in angka:
        total = total + nilai
    return total

hasil = jumlahkan([5, 3, 7, 2])
print(hasil)

hasil2 = jumlahkan([hasil, 3])
print(hasil2)


def terbesar(angka):
    return max(angka)

hasil = terbesar([4, 2, 5, 6, 8])
print(hasil)


def terbesar(angka):
    terbesar = angka[0]
    for nilai in angka:
        if nilai > terbesar:
            terbesar = nilai
    return terbesar

hasil = terbesar([4, 2, 5, 6, 8])
print(hasil)


def terkecil(angka):
    terkecil = angka[0]
    for nilai in angka:
        if nilai < terkecil:
            terkecil = nilai
    return terkecil

hasil = terkecil([4, 2, 5, 6, 8])
print(hasil)


def ratarata(angka):
    total = 0
    for nilai in angka:
        total = total + nilai
    return total / len(angka)

hasil = ratarata([4, 2, 5, 6, 8])
print(hasil)


angka = [4, 2, 5, 6, 8]

print("rata-rata =", ratarata(angka))
print("terbesar =", terbesar(angka))
print("terkecil =", terkecil(angka))


def jumlah(angka):
    jumlah = 0
    for nilai in angka:
        jumlah = jumlah + 1
    return jumlah

hasil = jumlah([4, 2, 5, 6, 8])
print(hasil)


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


hasil = statistik([4, 2, 5, 6, 8])
print(hasil)


jumlah, total, terbesar, terkecil, rata_rata = statistik([4, 2, 5, 6, 8])

print("jumlah -", jumlah)
print("total -", total)
print("terbesar -", terbesar)
print("terkecil -", terkecil)
print("rata-rata -", rata_rata)


data_nilai = [70, 85, 90, 65, 80]

jumlah, total, terbesar, terkecil, rata_rata = statistik(data_nilai)

print("jumlah -", jumlah)
print("total -", total)
print("terbesar -", terbesar)
print("terkecil -", terkecil)
print("rata-rata -", rata_rata)
