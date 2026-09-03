# Python Day 19 - Remedial / Uji Kesiapan
# Fokus: list of dictionary, filtering, counter, accumulator,
# grouping berdasarkan kelas, dictionary bertingkat, dan problem solving.

def siswa_top(nama):
    tertinggi = 0
    nama_tertinggi = ""

    for orang in nama:
        if orang["nilai"] >= 75 and orang["nilai"] > tertinggi:
            tertinggi = orang["nilai"]
            nama_tertinggi = orang["nama"]

    return nama_tertinggi, tertinggi

print(siswa_top([
    {"nama": "Owi", "nilai": 80},
    {"nama": "Joni", "nilai": 65},
    {"nama": "Wowo", "nilai": 90},
    {"nama": "Didi", "nilai": 70},
    {"nama": "Eko", "nilai": 100}
]))
# ('Eko', 100)

print(siswa_top([
    {"nama": "A", "nilai": 60},
    {"nama": "B", "nilai": 70},
    {"nama": "C", "nilai": 65}
]))
# ('', 0)


def lulus(nama):
    jumlah = 0

    for siswa in nama:
        if siswa["nilai"] >= 75:
            jumlah = jumlah + 1

    return jumlah

print(lulus([
    {"nama": "Owi", "nilai": 80},
    {"nama": "Joni", "nilai": 65},
    {"nama": "Wowo", "nilai": 90},
    {"nama": "Didi", "nilai": 70},
    {"nama": "Eko", "nilai": 100}
]))
# 3


def statistik(nama):
    jumlah = 0
    total = 0
    tertinggi = 0

    for siswa in nama:
        if siswa["nilai"] >= 75:
            jumlah = jumlah + 1
            total = total + siswa["nilai"]

        if siswa["nilai"] >= tertinggi:
            tertinggi = siswa["nilai"]

    return jumlah, total / jumlah, tertinggi

print(statistik([
    {"nama": "A", "nilai": 40},
    {"nama": "B", "nilai": 60},
    {"nama": "C", "nilai": 80}
]))
# (1, 80.0, 80)

print(statistik([
    {"nama": "Owi", "nilai": 80},
    {"nama": "Joni", "nilai": 65},
    {"nama": "Wowo", "nilai": 90},
    {"nama": "Didi", "nilai": 70},
    {"nama": "Eko", "nilai": 100}
]))
# (3, 90.0, 100)


def data(kelas):
    total_a = 0
    jumlah_a = 0
    tertinggi_a = 0
    total_b = 0
    jumlah_b = 0
    tertinggi_b = 0

    for siswa in kelas:
        if siswa["kelas"] == "A":
            jumlah_a = jumlah_a + 1
            total_a = total_a + siswa["nilai"]

        if siswa["kelas"] == "A" and siswa["nilai"] > tertinggi_a:
            tertinggi_a = siswa["nilai"]

        if siswa["kelas"] == "B":
            jumlah_b = jumlah_b + 1
            total_b = total_b + siswa["nilai"]

        if siswa["kelas"] == "B" and siswa["nilai"] > tertinggi_b:
            tertinggi_b = siswa["nilai"]

    hasil = {
        "A": {
            "jumlah": jumlah_a,
            "tertinggi": tertinggi_a,
            "rata-rata": round(total_a / jumlah_a, 2)
        },
        "B": {
            "jumlah": jumlah_b,
            "tertinggi": tertinggi_b,
            "rata-rata": round(total_b / jumlah_b, 2)
        }
    }

    return hasil

print(data([
    {"nama": "Owi", "kelas": "A", "nilai": 80},
    {"nama": "Joni", "kelas": "B", "nilai": 65},
    {"nama": "Wowo", "kelas": "A", "nilai": 90},
    {"nama": "Didi", "kelas": "B", "nilai": 70},
    {"nama": "Eko", "kelas": "A", "nilai": 100}
]))
# {'A': {'jumlah': 3, 'tertinggi': 100, 'rata-rata': 90.0},
#  'B': {'jumlah': 2, 'tertinggi': 70, 'rata-rata': 67.5}}

print(data([
    {"nama": "Owi", "kelas": "A", "nilai": 80},
    {"nama": "Joni", "kelas": "B", "nilai": 65},
    {"nama": "Wowo", "kelas": "A", "nilai": 90},
    {"nama": "Didi", "kelas": "B", "nilai": 70},
    {"nama": "Eko", "kelas": "A", "nilai": 100},
    {"nama": "Rudi", "kelas": "B", "nilai": 85}
]))
# {'A': {'jumlah': 3, 'tertinggi': 100, 'rata-rata': 90.0},
#  'B': {'jumlah': 3, 'tertinggi': 85, 'rata-rata': 73.33}}


def lulusan(nama):
    hasil_a = []
    hasil_b = []

    for siswa in nama:
        if siswa["kelas"] == "A" and siswa["nilai"] >= 75:
            hasil_a.append(siswa["nama"])

        if siswa["kelas"] == "B" and siswa["nilai"] >= 75:
            hasil_b.append(siswa["nama"])

    hasil_akhir = {
        "A": hasil_a,
        "B": hasil_b
    }

    return hasil_akhir

print(lulusan([
    {"nama": "Owi", "kelas": "A", "nilai": 80},
    {"nama": "Joni", "kelas": "B", "nilai": 65},
    {"nama": "Wowo", "kelas": "A", "nilai": 90},
    {"nama": "Didi", "kelas": "B", "nilai": 70},
    {"nama": "Eko", "kelas": "A", "nilai": 100}
]))
# {'A': ['Owi', 'Wowo', 'Eko'], 'B': []}
