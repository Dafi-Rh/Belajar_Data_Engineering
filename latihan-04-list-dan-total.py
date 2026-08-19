total = 0

for angka in range(3, 26):
    total = total + angka

print("total =", total)


total = 0

for angka in range(3, 26):
    print(angka)
    total = total + angka

print("total =", total)


total = 0

for angka in range(7, 20):
    print(angka)
    total = total + angka

print("total =", total)


total = 0

for angka in range(4, 18):
    if angka % 2 == 0:
        print(angka)
        total = total + angka

print("total", total)


nama = ["dodit", "didi", "dudu"]

print(nama)
print(nama[2])
print(nama[0])

nama[0] = "bubu"
print(nama[0])

nama.append("jaja")
print(nama)

for orang in nama:
    print(orang)


angka = [10, 20, 30, 40, 50]

total = 0

for nilai in angka:
    print(nilai)
    total = total + nilai

print("total =", total)
