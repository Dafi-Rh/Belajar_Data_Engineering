# PYTHON DAY 29
# Materi: Agregasi Dictionary, Counter, Accumulator, Total per Grade
# Catatan: latihan rata-rata per grade belum selesai.

siswa = [
    {"nama": "owi", "nilai": 80, "grade": "B"},
    {"nama": "joni", "nilai": 65, "grade": "C"},
    {"nama": "wowo", "nilai": 90, "grade": "A"},
    {"nama": "didi", "nilai": 70, "grade": "C"},
    {"nama": "eko", "nilai": 100, "grade": "A"},
    {"nama": "jefry", "nilai": 70, "grade": "C"},
    {"nama": "tedy", "nilai": 70, "grade": "C"}
]

# Percobaan pertama: total nilai berdasarkan grade

def rata_grade(siswa):
    hasil = {}
    for data in siswa:
        grade = data["grade"]
        if grade not in hasil:
            hasil[grade] = 0
        hasil[grade] = hasil[grade] + data["nilai"]
    return hasil

print(rata_grade(siswa))
# {'B': 80, 'C': 275, 'A': 190}

# Percobaan menambahkan jumlah siswa ke dictionary yang sama

def rata_grade_salah(siswa):
    hasil = {}
    for data in siswa:
        grade = data["grade"]
        if grade not in hasil:
            hasil[grade] = 0
        hasil[grade] = hasil[grade] + data["nilai"]
        hasil[grade] = hasil[grade] + 1
    return hasil

print(rata_grade_salah(siswa))
# {'B': 81, 'C': 279, 'A': 192}
# Salah karena total nilai dan jumlah siswa bercampur.

# Percobaan dengan total dan jumlah terpisah masih belum selesai.
# Konsep yang dibutuhkan:
# hasil_total  -> total nilai per grade
# hasil_jumlah -> jumlah siswa per grade
# hasil_rata   -> hasil_total / hasil_jumlah

# Contoh target:
# A = 190 / 2 = 95.0
# B = 80 / 1 = 80.0
# C = 275 / 4 = 68.75

# Konsep penting:
# Counter:
# jumlah = jumlah + 1
#
# Accumulator:
# total = total + data["nilai"]
#
# Dictionary dinamis:
# if grade not in hasil:
#     hasil[grade] = 0
#
# lalu accumulator:
# hasil[grade] = hasil[grade] + data["nilai"]
