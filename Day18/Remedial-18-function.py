# Python Day 18
# Latihan yang benar-benar dikerjakan hari ini.
# Fokus: list of dictionary.

def siswa_lulus(nama):
    hasil=[]
    for orang in (nama):
        orang["nama"]
        orang["nilai"]
        if orang["nilai"] >=75:
            hasil.append(orang["nama"])
    return hasil

print(siswa_lulus([
    {"nama": "Owi", "nilai": 80},
    {"nama": "Joni", "nilai": 65},
    {"nama": "Wowo", "nilai": 90},
    {"nama": "Didi", "nilai": 70},
    {"nama": "Eko", "nilai": 100}
]))
# ['Owi', 'Wowo', 'Eko']


def avg(nama):
    jumlah =0
    total=0
    for orang in nama:
        jumlah=jumlah+1
        total=total+orang["nilai"]
        hasil = total/jumlah
    return hasil

print(avg([
    {"nama": "Owi", "nilai": 80},
    {"nama": "Joni", "nilai": 65},
    {"nama": "Wowo", "nilai": 90},
    {"nama": "Didi", "nilai": 70},
    {"nama": "Eko", "nilai": 100}
]))
# 81.0


def tertinggi(nama):
    tertinggi=0
    for orang in nama:
        if orang["nilai"]>tertinggi:
            tertinggi = orang["nilai"]
    return tertinggi

print(tertinggi([
    {"nama": "Owi", "nilai": 80},
    {"nama": "Joni", "nilai": 65},
    {"nama": "Wowo", "nilai": 90},
    {"nama": "Didi", "nilai": 70},
    {"nama": "Eko", "nilai": 100}
]))
# 100


def siswa_tertinggi(nama):
    tertinggi=0
    nama_tertinggi=""
    for orang in nama:
        if orang["nilai"]>tertinggi:
            tertinggi = orang["nilai"]
            nama_tertinggi=orang["nama"]
    return nama_tertinggi, tertinggi

print(siswa_tertinggi([
    {"nama": "Owi", "nilai": 80},
    {"nama": "Joni", "nilai": 65},
    {"nama": "Wowo", "nilai": 90},
    {"nama": "Didi", "nilai": 70},
    {"nama": "Eko", "nilai": 100}
]))
# ('Eko', 100)


def avg_lulus(nama):
    jumlah=0
    total=0
    for siswa in nama:
        if siswa["nilai"]>=75:
            jumlah=jumlah+1
            total=total+siswa["nilai"]
            hasil=total/jumlah
    return hasil

print(avg_lulus([
    {"nama": "Owi", "nilai": 80},
    {"nama": "Joni", "nilai": 65},
    {"nama": "Wowo", "nilai": 90},
    {"nama": "Didi", "nilai": 70},
    {"nama": "Eko", "nilai": 100}
]))
# 90.0


def upavg(nama):
    jumlah=0
    total=0
    hasil=[]
    for siswa in (nama):
        jumlah=jumlah+1
        total=total+siswa["nilai"]
        rata_rata=total/jumlah
        if siswa["nilai"]>rata_rata:
            rata_rata=siswa["nilai"]
            hasil.append(siswa["nama"])
    return hasil

print(upavg([
    {"nama": "Owi", "nilai": 80},
    {"nama": "Joni", "nilai": 65},
    {"nama": "Wowo", "nilai": 90},
    {"nama": "Didi", "nilai": 70},
    {"nama": "Eko", "nilai": 100}
]))
# ['Wowo', 'Eko']
