# Latihan Python 02 - List, Loop, dan Sort
# Dokumentasi latihan berdasarkan percobaan asli di Python REPL.

angka = [5, 7, 2, 9]
print(angka)

# Percobaan for yang salah
# for total in range:
#     print(angka)
# Error: TypeError: 'type' object is not iterable

# Loop melalui isi list
for nilai in angka:
    print(angka)

print(len(angka))

total = 0
for nilai in angka:
    total = total + nilai
print(total)

print(max(angka))
print(min(angka))
print(sum(angka))

# Percobaan yang salah
# print(sum(len(angka)))
# Error: TypeError: 'int' object is not iterable

# Menghitung rata-rata
avg = sum(angka) / len(angka)
print(avg)

print(5 in angka)
print(1 in angka)

if 0 in angka:
    print("ada")
else:
    print("tidak ada")

print(5 not in angka)
print(1 not in angka)

# Menghapus berdasarkan nilai
angka.remove(7)
print(angka)

# Rata-rata setelah list berubah
avg = sum(angka) / len(angka)
print(avg)

# Menghapus berdasarkan index
angka.pop(1)
print(angka)

# pop() mengembalikan nilai yang dihapus
print(angka.pop(1))
print(angka)

# Menambahkan item pada index tertentu
angka.insert(6, 7)
print(angka)

# Percobaan index yang tidak ada
# angka.pop(6)
# Error: IndexError: pop index out of range

angka.pop(1)
print(angka)

# Membuat list angka baru
angka = [3, 5, 0, 9, 7]

# Urut dari kecil ke besar
angka.sort()
print(angka)

# Urut dari besar ke kecil
angka.sort(reverse=True)
print(angka)

# Sort nama dengan huruf kapital dan kecil
nama = ["Joko", "Joni", "apuy", "didi", "dudu"]
nama.sort()
print(nama)

nama = ["joko", "joni", "apuy", "didi", "dudu"]
nama.sort()
print(nama)

nama.sort(reverse=True)
print(nama)
