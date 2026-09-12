# PYTHON DAY 28
# Materi: Dictionary, Counter, Accumulator, Dictionary Dinamis

siswa = [
    {"nama": "owi", "nilai": 80, "grade": "B"},
    {"nama": "joni", "nilai": 65, "grade": "C"},
    {"nama": "wowo", "nilai": 90, "grade": "A"},
    {"nama": "didi", "nilai": 70, "grade": "C"},
    {"nama": "eko", "nilai": 100, "grade": "A"},
    {"nama": "jefry", "nilai": 70, "grade": "C"},
    {"nama": "tedy", "nilai": 70, "grade": "C"}
]


# 1. Menghitung jumlah siswa berdasarkan grade

def jumlah_grade(siswa):
    jumlaha = 0
    jumlahb = 0
    jumlahc = 0
    hasil = {}

    for data in siswa:
        if data["grade"] == "A":
            jumlaha = jumlaha + 1
        elif data["grade"] == "B":
            jumlahb = jumlahb + 1
        else:
            jumlahc = jumlahc + 1

    hasil = {
        "A": jumlaha,
        "B": jumlahb,
        "C": jumlahc
    }

    return hasil


print(jumlah_grade(siswa))
# {'A': 2, 'B': 1, 'C': 4}


# 2. Menghitung total nilai berdasarkan grade

def total_nilai_manual(siswa):
    totala = 0
    totalb = 0
    totalc = 0
    totallain = 0
    hasil = {}

    for data in siswa:
        if data["grade"] == "A":
            totala = totala + data["nilai"]
        elif data["grade"] == "B":
            totalb = totalb + data["nilai"]
        elif data["grade"] == "C":
            totalc = totalc + data["nilai"]
        else:
            totallain = totallain + data["nilai"]

    hasil = {
        "A": totala,
        "B": totalb,
        "C": totalc,
        "Lainnya": totallain
    }

    return hasil


print(total_nilai_manual(siswa))
# {'A': 190, 'B': 80, 'C': 275, 'Lainnya': 0}


# 3. Percobaan accumulator yang salah:
#    satu total dipakai untuk semua grade

def total_salah(siswa):
    total = 0

    for data in siswa:
        if data["grade"] == "A":
            hasil = total = total + data["nilai"]
        elif data["grade"] == "B":
            hasil = total = total + data["nilai"]

    return hasil


# Satu `total` membuat nilai antar-grade tercampur.


# 4. Dictionary dinamis:
#    total nilai otomatis berdasarkan grade

def total_nilai(siswa):
    hasil = {}

    for data in siswa:
        grade = data["grade"]

        if grade not in hasil:
            hasil[grade] = 0

        hasil[grade] = hasil[grade] + data["nilai"]

    return hasil


print(total_nilai(siswa))
# {'B': 80, 'C': 275, 'A': 190}


# 5. Grade baru dapat muncul otomatis

siswa_tambah = [
    {"nama": "owi", "nilai": 80, "grade": "B"},
    {"nama": "joni", "nilai": 65, "grade": "C"},
    {"nama": "wowo", "nilai": 90, "grade": "A"},
    {"nama": "andi", "nilai": 50, "grade": "D"}
]

print(total_nilai(siswa_tambah))
# {'B': 80, 'C': 65, 'A': 90, 'D': 50}


# KONSEP DAY 28
#
# Counter:
# jumlah = jumlah + 1
#
# Accumulator:
# total = total + data["nilai"]
#
# Dictionary dinamis:
# hasil = {}
#
# grade = data["grade"]
#
# if grade not in hasil:
#     hasil[grade] = 0
#
# hasil[grade] = hasil[grade] + data["nilai"]
#
# `if grade not in hasil` berarti:
# kalau key grade belum ada, buat key tersebut
# dan beri nilai awal 0.
#
# Setelah itu accumulator menambahkan nilai.
