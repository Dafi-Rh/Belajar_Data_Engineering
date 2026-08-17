angka = 1
while angka <=10:
    print(angka)
    angka+=1

angka = 10
while angka >=9:
    print(angka)
    angka-=9

angka = 10
while angka >= 9:
    print(angka)
    angka -= 1

angka = 10
while angka >= 10:
    print(angka)
    angka -= 1

angka = 10
while angka >= 0:
    print(angka)
    angka -= 1

angka = int(input("angka = "))
while angka !=0:
    print("masukkan", angka)
    angka = int(input("masukkan angka lagi = "))

print("selesai")

# menghitung total

total = 0
angka = int(input("angka = "))

while angka != 0:
    total = total + angka
    angka = int(input("masukkan angka lagi = "))

print("total =", total)

# menghitung jumlah angka

jumlah = 0
angka = int(input("angka = "))

while angka != 0:
    jumlah = jumlah + 1
    angka = int(input("masukkan angka lagi = "))

print("jumlah angka =", jumlah)
