# Belajar Python Day 30
# Materi: function, dictionary, loop, pengelompokan berdasarkan grade,
# total nilai, jumlah siswa, dan rata-rata nilai.

def rata_grade(siswa):
    total = {}
    jumlah = {}
    hasil = {}
    hasil_akhir = {}

    for data in siswa:
        grade = data["grade"]
        if grade not in jumlah:
            jumlah[grade] = 0
        jumlah[grade] = jumlah[grade] + 1

    for daftar in siswa:
        grade = daftar["grade"]
        if grade not in total:
            total[grade] = 0
        total[grade] = total[grade] + daftar["nilai"]

    for rapor in siswa:
        grade = rapor["grade"]
        if grade not in hasil:
            hasil[grade] = 0
        hasil[grade] = total[grade] / jumlah[grade]

    for grade in total:
        hasil_akhir[grade] = {
            "total": total[grade],
            "jumlah": jumlah[grade],
            "rata_rata": hasil[grade]
        }

    return hasil_akhir


print(rata_grade([
    {"nama": "owi", "nilai": 80, "grade": "B"},
    {"nama": "joni", "nilai": 65, "grade": "C"},
    {"nama": "wowo", "nilai": 90, "grade": "A"},
    {"nama": "didi", "nilai": 70, "grade": "C"},
    {"nama": "eko", "nilai": 100, "grade": "A"},
    {"nama": "jefry", "nilai": 70, "grade": "C"},
    {"nama": "tedy", "nilai": 70, "grade": "C"}
]))

# Output:
# {'B': {'total': 80, 'jumlah': 1, 'rata_rata': 80.0},
#  'C': {'total': 275, 'jumlah': 4, 'rata_rata': 68.75},
#  'A': {'total': 190, 'jumlah': 2, 'rata_rata': 95.0}}
