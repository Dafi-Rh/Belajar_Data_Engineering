import csv

# Membaca 1 file siswa.csv dan menyaring siswa yang tidak lulus (< 75)
with open("siswa.csv", mode="r") as file:
    reader = csv.reader(file)
    next(reader)  # Melewati baris header ('id', 'nama', 'nilai', 'kelas')

    for daftar in reader:
        if int(daftar[2]) < 75:
            print(f"{daftar[1]} tidak lulus dengan nilai {daftar[2]}")
