biodata = {
    "nama": "dodit",
    "umur": 14,
    "alamat": "manhattan"
}

print(biodata)
print(biodata["nama"])
print(biodata["umur"])
print(biodata["alamat"])

biodata["umur"] = 17
print(biodata)

biodata["pekerjaan"] = "kuli"
print(biodata)

del biodata["alamat"]
print(biodata)

for key in biodata:
    print(key)

for value in biodata.values():
    print(value)

for key, value in biodata.items():
    print(key, value)

if biodata["umur"] == 17:
    print("asisten kuli")
elif biodata["umur"] >= 20:
    print("kuli pro")

biodata["umur"] = 20

if biodata["umur"] == 17:
    print("asisten kuli")
elif biodata["umur"] >= 20:
    print("kuli pro")

orang = {
    "Owi": 17,
    "Joni": 20,
    "Wowo": 16
}

for nama, umur in orang.items():
    print(nama, umur)

for nama, umur in orang.items():
    if umur <= 20:
        print(nama, "kuli lv1")

for nama, umur in orang.items():
    if umur <= 19:
        print(nama, "kuli lv1")
