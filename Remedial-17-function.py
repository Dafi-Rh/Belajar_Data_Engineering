# Day17-latihan.py
# Latihan fungsi pengelolaan data siswa dan statistik nilai

def siswa_lulus(nama, nilai):
    hasil = []
    for orang, angka in zip(nama, nilai):
        if angka >= 75:
            hasil.append((orang, angka))
    return hasil

def ringkasan(nama, nilai):
    siswa = 0
    total = 0
    avg = 0
    for orang, angka in zip(nama, nilai):
        siswa = siswa + 1
        total = total + angka
        avg = total / siswa
    return siswa, total, avg

def statistik(nama, nilai):
    tertinggi = 0
    terendah = 999999
    jumlah = 0
    total = 0
    avg = 0
    for orang, angka in zip(nama, nilai):
        total = total + angka
        jumlah = jumlah + 1
        avg = total / jumlah
        if angka > tertinggi:
            tertinggi = angka
        if angka < terendah:
            terendah = angka
    return tertinggi, terendah, avg

if __name__ == "__main__":
    daftar_nama = ["Owi", "Joni", "Wowo", "Didi", "Eko"]
    daftar_nilai = [80, 65, 90, 70, 100]

    print("--- Siswa Lulus (Nilai >= 75) ---")
    print(siswa_lulus(daftar_nama, daftar_nilai))

    print("
--- Ringkasan (Jumlah Siswa, Total Nilai, Rata-rata) ---")
    print(ringkasan(daftar_nama, daftar_nilai))

    print("
--- Statistik (Nilai Tertinggi, Nilai Terendah, Rata-rata) ---")
    print(statistik(daftar_nama, daftar_nilai))
