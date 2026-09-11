# PYTHON DAY 27
# Materi: Function, List of Dictionary, Filtering,
# Algoritma Mencari Nilai Tertinggi

# =========================================================
# DATA LATIHAN
# =========================================================

siswa = [
    {"nama": "owi", "nilai": 80, "grade": "B"},
    {"nama": "joni", "nilai": 65, "grade": "C"},
    {"nama": "wowo", "nilai": 90, "grade": "A"},
    {"nama": "didi", "nilai": 70, "grade": "C"},
    {"nama": "eko", "nilai": 100, "grade": "A"},
    {"nama": "jefry", "nilai": 70, "grade": "C"},
    {"nama": "tedy", "nilai": 70, "grade": "C"}
]


# =========================================================
# 1. Function filtering siswa lulus
# =========================================================

def lulus(siswa):
    hasil = []

    for data in siswa:
        if data["nilai"] >= 75:
            hasil.append((data["nama"], data["nilai"]))

    return hasil


print(lulus(siswa))

# Hasil:
# [('owi', 80), ('wowo', 90), ('eko', 100)]


# =========================================================
# 2. Function mencari satu siswa dengan nilai tertinggi
# =========================================================

def top(siswa):
    hasil = {}
    tertinggi = 0

    for data in siswa:
        if data["nilai"] >= tertinggi:
            tertinggi = data["nilai"]

            hasil = {
                "nama": data["nama"],
                "nilai": data["nilai"],
                "grade": data["grade"]
            }

    return hasil


print(top(siswa))

# Hasil:
# {'nama': 'eko', 'nilai': 100, 'grade': 'A'}


# =========================================================
# 3. Percobaan awal dengan list
#    Menyimpan setiap siswa yang memecahkan rekor
# =========================================================

def top_rekor(siswa):
    hasil = []
    tertinggi = 0

    for data in siswa:
        if data["nilai"] >= tertinggi:
            tertinggi = data["nilai"]
            hasil.append(
                (data["nama"], tertinggi, data["grade"])
            )

    return hasil


print(top_rekor(siswa))

# Hasil:
# [('owi', 80, 'B'), ('wowo', 90, 'A'), ('eko', 100, 'A')]

# Catatan:
# Ini bukan semua siswa dengan nilai tertinggi.
# Ini adalah siswa yang setiap kali memecahkan rekor nilai sebelumnya.


# =========================================================
# 4. Algoritma dua tahap:
#    mencari semua siswa dengan nilai tertinggi
# =========================================================

def top_semua(siswa):
    tertinggi = 0
    hasil = []

    # Tahap 1: cari nilai tertinggi
    for data in siswa:
        if data["nilai"] > tertinggi:
            tertinggi = data["nilai"]

    # Tahap 2: cari semua siswa dengan nilai tersebut
    for data in siswa:
        if data["nilai"] == tertinggi:
            hasil.append(data)

    return hasil


# Pemanggilan function yang benar:
print(top_semua(siswa))


# =========================================================
# 5. Menguji kondisi nilai tertinggi yang sama (tie)
# =========================================================

siswa_tie = [
    {"nama": "owi", "nilai": 80, "grade": "B"},
    {"nama": "eko", "nilai": 100, "grade": "A"},
    {"nama": "jefry", "nilai": 100, "grade": "A"},
    {"nama": "didi", "nilai": 70, "grade": "C"}
]

print(top_semua(siswa_tie))

# Hasil:
# [
#     {'nama': 'eko', 'nilai': 100, 'grade': 'A'},
#     {'nama': 'jefry', 'nilai': 100, 'grade': 'A'}
# ]


# =========================================================
# KONSEP UTAMA DAY 27
# =========================================================

# 1. List kosong:
#    hasil = []
#    Cocok ketika hasil bisa berisi banyak data.
#
# 2. Dictionary kosong:
#    hasil = {}
#    Cocok ketika ingin menyimpan satu data berbentuk key-value.
#
# 3. Filtering:
#    for data in siswa:
#        if kondisi:
#            hasil.append(...)
#
# 4. Mencari nilai maksimum secara manual:
#    tertinggi = 0
#    for data in siswa:
#        if data["nilai"] > tertinggi:
#            tertinggi = data["nilai"]
#
# 5. Algoritma dua tahap:
#    tahap 1 -> cari nilai terbaik
#    tahap 2 -> cari semua data yang nilainya sama dengan nilai terbaik
#
# 6. `>=` dan `>`
#    >= dapat mengganti hasil ketika ada nilai yang sama.
#    > mempertahankan hasil pertama saat menemukan nilai maksimum.
#
# 7. Nama function harus sama saat dipanggil:
#    def top_semua(siswa):
#    top_semua(siswa)
