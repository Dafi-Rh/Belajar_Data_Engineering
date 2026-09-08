# PYTHON DAY 24
# Materi: Dictionary, List of Dictionary, Filtering, Function, Statistik

# 1. Dictionary dasar
siswa = {"nama": "Owi", "nilai": 80, "grade": "B"}
print(siswa)
print(siswa["nama"])

# 2. List berisi dictionary
siswa = [
    {"nama": "owi", "nilai": 45, "grade": "D"},
    {"nama": "eko", "nilai": 80, "grade": "B"},
    {"nama": "wowo", "nilai": 30, "grade": "D"},
    {"nama": "didi", "nilai": 85, "grade": "B"},
    {"nama": "jefry", "nilai": 100, "grade": "A"}
]

print(siswa[1]["nilai"])
print(siswa[3]["grade"])

# 3. Filtering dengan for
for data in siswa:
    if data["nilai"] > 75:
        print(data)

for data in siswa:
    if data["grade"] == "B":
        print(data["nama"])

# 4. Membuat list hasil filtering
hasil = []
for data in siswa:
    if data["nilai"] >= 75:
        hasil.append(data)
print(hasil)

hasil = []
for data in siswa:
    if data["grade"] == "A" or data["grade"] == "B":
        hasil.append((data["nama"], data["nilai"]))
print(hasil)

# 5. Function dengan parameter batas
def lulus(siswa, batas):
    hasil = []
    for data in siswa:
        if data["nilai"] >= batas:
            hasil.append(data)
    return hasil

print(lulus(siswa, 80))

# 6. Menghitung jumlah berdasarkan grade
def hitung_grade(nama, grade):
    jumlah = 0
    for data in nama:
        if data["grade"] == grade:
            jumlah = jumlah + 1
    return jumlah

print(hitung_grade(siswa, "A"))
print(hitung_grade(siswa, "D"))

# 7. Rata-rata nilai berdasarkan grade
def avg_grade(siswa, grade):
    jumlah = 0
    total = 0

    for data in siswa:
        if data["grade"] == grade:
            jumlah = jumlah + 1
            total = total + data["nilai"]

    hasil = total / jumlah
    return hasil

print(avg_grade(siswa, "A"))
print(avg_grade(siswa, "B"))
print(avg_grade(siswa, "D"))

# 8. Statistik manual per grade
siswa_8 = [
    {"nama": "owi", "nilai": 45, "grade": "D"},
    {"nama": "eko", "nilai": 80, "grade": "B"},
    {"nama": "wowo", "nilai": 30, "grade": "D"},
    {"nama": "didi", "nilai": 85, "grade": "B"},
    {"nama": "jefry", "nilai": 100, "grade": "A"},
    {"nama": "budi", "nilai": 70, "grade": "C"},
    {"nama": "joni", "nilai": 65, "grade": "C"},
    {"nama": "tedi", "nilai": 90, "grade": "A"}
]

def statistik_semua_grade(data):
    jumlah1 = 0
    total1 = 0
    jumlah2 = 0
    total2 = 0
    jumlah3 = 0
    total3 = 0
    jumlah4 = 0
    total4 = 0

    hasil1 = 0
    hasil2 = 0
    hasil3 = 0
    hasil4 = 0

    for siswa_data in data:
        if siswa_data["grade"] == "A":
            jumlah1 = jumlah1 + 1
            total1 = total1 + siswa_data["nilai"]
            hasil1 = total1 / jumlah1

        elif siswa_data["grade"] == "B":
            jumlah2 = jumlah2 + 1
            total2 = total2 + siswa_data["nilai"]
            hasil2 = total2 / jumlah2

        elif siswa_data["grade"] == "C":
            jumlah3 = jumlah3 + 1
            total3 = total3 + siswa_data["nilai"]
            hasil3 = total3 / jumlah3

        elif siswa_data["grade"] == "D":
            jumlah4 = jumlah4 + 1
            total4 = total4 + siswa_data["nilai"]
            hasil4 = total4 / jumlah4

    return (
        jumlah1, hasil1,
        jumlah2, hasil2,
        jumlah3, hasil3,
        jumlah4, hasil4
    )

print(statistik_semua_grade(siswa_8))

# 9. Dictionary penghitung grade
def jumlah_grade(siswa):
    jumlah = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0
    }

    for data in siswa:
        jumlah[data["grade"]] = jumlah[data["grade"]] + 1

    return jumlah

print(jumlah_grade(siswa_8))

# 10. Nested dictionary: jumlah dan total nilai
def statistik_grade(siswa):
    hasil = {
        "A": {"jumlah": 0, "total": 0},
        "B": {"jumlah": 0, "total": 0},
        "C": {"jumlah": 0, "total": 0},
        "D": {"jumlah": 0, "total": 0}
    }

    for data in siswa:
        hasil[data["grade"]]["jumlah"] = (
            hasil[data["grade"]]["jumlah"] + 1
        )
        hasil[data["grade"]]["total"] = (
            hasil[data["grade"]]["total"] + data["nilai"]
        )

    return hasil

print(statistik_grade(siswa_8))

# Hasil akhir:
# A -> jumlah 2, total 190
# B -> jumlah 2, total 165
# C -> jumlah 2, total 135
# D -> jumlah 2, total 75

# Konsep penting Day 24:
# dictionary -> data["nama"], data["nilai"], data["grade"]
# list of dictionaries -> for data in siswa
# filtering -> for + if + append
# counter -> jumlah = jumlah + 1
# dictionary dinamis -> jumlah[data["grade"]]
# nested dictionary -> hasil[data["grade"]]["jumlah"]
# nested dictionary -> hasil[data["grade"]]["total"]
