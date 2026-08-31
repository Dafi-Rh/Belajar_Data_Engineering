# Python Day 16 - Remedial Function, Loop, Condition, zip()
# Fokus:
# filtering, zip(), append(), counter, pencarian tertinggi/terendah,
# kondisi rentang, dan beberapa if dalam satu loop.

def siswa_gagal(nama, nilai):
    hasil = []
    for orang, angka in zip(nama, nilai):
        if angka < 75:
            hasil.append(orang)
    return hasil

print(siswa_gagal(
    ["A", "B", "C", "D", "E"],
    [80, 55, 90, 65, 100]
))


def siswa_lulus(nama, nilai):
    hasil = []
    for orang, angka in zip(nama, nilai):
        if angka >= 75:
            hasil.append((orang, angka))
    return hasil

print(siswa_lulus(
    ["A", "B", "C", "D", "E"],
    [80, 55, 90, 65, 100]
))


def siswa_90(nama, nilai):
    hasil = []
    for orang, angka in zip(nama, nilai):
        if angka == 90:
            hasil.append((orang, angka))
    return hasil

print(siswa_90(
    ["A", "B", "C", "D", "E"],
    [80, 90, 90, 65, 100]
))


def siswa90up(nama, nilai):
    hasil = []
    for orang, angka in zip(nama, nilai):
        if angka >= 90:
            hasil.append((orang, angka))
    return hasil

print(siswa90up(
    ["A", "B", "C", "D", "E"],
    [80, 90, 90, 65, 100]
))


def siswa_80_sampai_90(nama, nilai):
    hasil = []
    for orang, angka in zip(nama, nilai):
        if angka >= 80 and angka <= 90:
            hasil.append((orang, angka))
    return hasil

print(siswa_80_sampai_90(
    ["A", "B", "C", "D", "E"],
    [80, 90, 90, 65, 100]
))


def siswa_80_sampai_99(nama, nilai):
    hasil = []
    for orang, angka in zip(nama, nilai):
        if angka >= 80 and angka < 100:
            hasil.append((orang, angka))
    return hasil

print(siswa_80_sampai_99(
    ["A", "B", "C", "D", "E"],
    [80, 55, 90, 65, 100]
))


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
    [80, 55, 90, 65, 100]
))


def siswa_nilai_terendah(nama, nilai):
    terendah = 999999
    nama_terendah = ""

    for orang, angka in zip(nama, nilai):
        if angka < terendah:
            terendah = angka
            nama_terendah = orang

    return nama_terendah, terendah

print(siswa_nilai_terendah(
    ["A", "B", "C", "D", "E"],
    [80, 55, 90, 65, 100]
))


def ringkasan(nama, nilai):
    tertinggi = 0
    nama_tertinggi = ""
    jumlah = 0

    for orang, angka in zip(nama, nilai):
        if angka >= 75:
            jumlah = jumlah + 1

        if angka > tertinggi:
            tertinggi = angka
            nama_tertinggi = orang

    return jumlah, nama_tertinggi, tertinggi

print(ringkasan(
    ["A", "B", "C", "D", "E"],
    [80, 55, 90, 65, 100]
))


# Catatan:
# Dua if dapat digunakan dalam satu for ketika kedua kondisi
# merupakan pekerjaan yang terpisah.
#
# if:
#     dicek
# if:
#     dicek lagi
#
# Berbeda dengan if + elif, yang memakai cabang kondisi.
