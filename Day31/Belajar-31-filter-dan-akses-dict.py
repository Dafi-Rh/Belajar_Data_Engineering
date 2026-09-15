# Belajar Python 31 - Filter List of Dictionary & Akses Nested Dictionary
# Dokumentasi hasil akhir yang sukses berdasarkan percobaan di Python REPL.

# CARA 1: Menghitung rata-rata khusus grade A langsung dari data mentah (list of dict)
def rata_a(siswa):
    jumlah = 0
    total = 0
    
    for data in siswa:
        # Perbaikan: gunakan variabel iterasi 'data', bukan list 'siswa'
        if data["grade"] == "A": 
            jumlah = jumlah + 1
            total = total + data["nilai"]
            
    # Mencegah error pembagian dengan nol jika tidak ada grade A
    if jumlah > 0:
        hasil = total / jumlah
    else:
        hasil = 0
        
    return hasil

# Data Testing Cara 1
data_siswa = [
    {"nama": "owi", "nilai": 80, "grade": "B"},
    {"nama": "joni", "nilai": 65, "grade": "C"},
    {"nama": "wowo", "nilai": 90, "grade": "A"},
    {"nama": "didi", "nilai": 70, "grade": "C"},
    {"nama": "eko", "nilai": 100, "grade": "A"},
    {"nama": "jefry", "nilai": 70, "grade": "C"},
    {"nama": "tedy", "nilai": 70, "grade": "C"}
]

print("Rata-rata Grade A (dari data mentah):", rata_a(data_siswa))


# =====================================================================


# CARA 2: Mengambil rata-rata grade A dari hasil rekapitulasi (Nested Dictionary)
hasil_rekap = {
    "B": {"total": 80, "jumlah": 1, "rata_rata": 80.0},
    "C": {"total": 275, "jumlah": 4, "rata_rata": 68.75},
    "A": {"total": 190, "jumlah": 2, "rata_rata": 95.0}
}

# Cara mengakses value yang berada di dalam dictionary berlapis
rata_rata_A = hasil_rekap["A"]["rata_rata"]
print("Rata-rata Grade A (dari nested dictionary):", rata_rata_A)
