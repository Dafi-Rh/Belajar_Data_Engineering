# Belajar Python Day 8 - Dictionary dan List

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
    if bio_data["umur"][i] <= 18:
        print(bio_data["nama"][i])

for i in range(len(bio_data["nama"])):
    if bio_data["umur"][i] >= 18:
        print(bio_data["nama"][i], "dewasa")
    else:
        print(bio_data["nama"][i], "belum dewasa")
