# Belajar Python 10 - Function
# Dokumentasi latihan berdasarkan percobaan asli di Python REPL.

# 1. Function sederhana

def sapa(nama):
    print("halo", nama)

sapa("wowo")
sapa("owi")


# 2. Function dengan dua parameter

def data(nama, umur):
    print("nama saya", nama)
    print("umur saya", umur, "tahun")

data("owi", 19)
data("wowo", 21)


# 3. Function untuk menjumlahkan dua angka

def tambah(a, b):
    print(a + b)

tambah(8, 9)
tambah(5, 7)


# 4. Function dengan return

def tambah(a, b):
    return a + b

hasil = tambah(5, 7)
print(hasil)

hasil2 = tambah(hasil, 8)
print(hasil2)


# 5. Function perkalian

def kali(a, b):
    return a * b

Lpersegi = kali(4, 4)
print(Lpersegi)

volume = kali(Lpersegi, 2)
print(volume)
print(volume, "m3")


# 6. Function dengan if/else

def cek_nilai(nama, nilai):
    if nilai >= 75:
        print(nama, nilai, "tuntas")
    else:
        print(nama, nilai, "remedial")

cek_nilai("budi", 90)
cek_nilai("owi", 25)
cek_nilai("wowo", 75)


# 7. Function yang mengembalikan status

def cek_nilai(nama, nilai):
    if nilai >= 75:
        return "tuntas"
    else:
        return "remedial"

hasil = cek_nilai("budi", 90)
print(hasil)

absen7 = cek_nilai("owi", 50)
print(absen7)


# 8. Default parameter

def sapa(nama="teman"):
    print("halo", nama)

sapa()
sapa("joni")


# 9. Default parameter untuk pangkat

def pangkat(a, b=2):
    print(a ** b)

pangkat(9)
pangkat(2, 3)


# 10. Pangkat dengan return

def pangkat(a, b=2):
    return a ** b

pangkat(2)
pangkat(4, 4)

hasil = pangkat(2, 4)
print(hasil)

pangkat(hasil, 2)

hasil2 = pangkat(hasil, 2)
print(hasil2)

hasil3 = pangkat(hasil2, hasil)
print(hasil3)


# 11. Function grade

def grade(nama, nilai):
    if nilai >= 90:
        return "A"
    elif nilai >= 80:
        return "B"
    elif nilai >= 70:
        return "C"
    else:
        return "D"

print(grade("owi", 70))
hasil = grade("wowo", 45)
print(hasil)


# 12. Function mengembalikan beberapa nilai sekaligus

def grade(nama, nilai):
    if nilai >= 90:
        return nama, nilai, "A"
    elif nilai >= 80:
        return nama, nilai, "B"
    elif nilai >= 70:
        return nama, nilai, "C"
    else:
        return nama, nilai, "D"

hasil = grade("owi", 60)
print(hasil)

hasil = grade("wowo", 20)
nama, nilai, status = hasil
print(nama)
print(nilai)
print(status)


# Contoh hasil lain
hasil = grade("Owi", 72)
nama, nilai, status = hasil

print(nama)
print(nilai)
print(status)

print(nama, "\n", nilai, "\n", status)


# 13. Scope variable sederhana
nama = "owi"

def sapa():
    nama = "wowo"
    print(nama)

sapa()

nama = "joni"
print(nama)
