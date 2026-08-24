# Belajar Python Day 8 - Dictionary, List, zip(), dan Counter

bio_data = {
    "nama": ["Owi", "Joni", "Wowo"],
    "umur": [17, 20, 16]
}

print(bio_data["nama"])
print(bio_data["nama"][2])
print(bio_data["nama"][1])
print(bio_data["nama"][0])
print(bio_data["nama"][0], bio_data["umur"][0])

for nama in bio_data["nama"]:
    print(nama)

for i in range(len(bio_data["nama"])):
    print(bio_data["nama"][i], bio_data["umur"][i])

for i in range(len(bio_data["nama"])):
    if bio_data["umur"][i] >= 18:
        print(bio_data["nama"][i])

for i in range(len(bio_data["nama"])):
    if bio_data["umur"][i] < 18:
        print(bio_data["nama"][i])

for i in range(len(bio_data["nama"])):
    if bio_data["umur"][i] >= 18:
        print(bio_data["nama"][i], "dewasa")
    else:
        print(bio_data["nama"][i], "belum dewasa")


# zip() dengan 2 list
nama = ["Owi", "Joni", "Wowo"]
umur = [17, 20, 16]

for orang, usia in zip(nama, umur):
    print(orang, usia)

for orang, usia in zip(nama, umur):
    if usia >= 18:
        print(orang, usia, "dewasa")
    else:
        print(orang, usia, "bocil")

for orang, usia in zip(nama, umur):
    if usia >= 18:
        print(orang, usia, "dewasa")


# zip() dengan 3 list
nama = ["Owi", "Joni", "Wowo"]
umur = [17, 20, 16]
kota = ["Jakarta", "Bandung", "Surabaya"]

for orang, usia, daerah in zip(nama, umur, kota):
    print(orang, usia, daerah)


# zip() dengan panjang list berbeda
nama = ["Owi", "Joni", "Wowo"]
umur = [17, 20, 16, 25]

for orang, usia in zip(nama, umur):
    print(orang, usia)


# Filter orang dewasa
nama = ["Owi", "Joni", "Wowo", "Didi"]
umur = [17, 20, 16, 21]

for orang, usia in zip(nama, umur):
    if usia >= 18:
        print(orang, usia)


# Menghitung jumlah orang dewasa
jumlah = 0

for orang, usia in zip(nama, umur):
    if usia >= 18:
        jumlah = jumlah + 1

print(jumlah, "orang")


# Menghitung jumlah belum dewasa
jumlah = 0

for orang, usia in zip(nama, umur):
    if usia < 18:
        jumlah = jumlah + 1

print(jumlah, "orang")


# Menghitung dewasa dan belum dewasa sekaligus
dewasa = 0
belum = 0

for orang, usia in zip(nama, umur):
    if usia >= 18:
        dewasa = dewasa + 1
    else:
        belum = belum + 1

print("dewasa =", dewasa, "orang")
print("belum =", belum, "orang")
