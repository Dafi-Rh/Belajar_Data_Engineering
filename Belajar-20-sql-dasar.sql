-- ==========================================
-- LATIHAN SQL - DAY 20
-- ==========================================

-- 1. Membuat tabel siswa
CREATE TABLE siswa (
    id INTEGER,
    nama VARCHAR(50),
    nilai INTEGER
);

-- 2. Memasukkan data awal siswa
INSERT INTO siswa (id, nama, nilai) VALUES
(1, 'Owi', 80),
(2, 'Joni', 65),
(3, 'Wowo', 90),
(4, 'Didi', 70),
(5, 'Eko', 100);

-- 3. Menampilkan semua data siswa
SELECT * FROM siswa;

-- 4. Menyaring siswa yang nilainya >= 75
SELECT nama, nilai 
FROM siswa 
WHERE nilai >= 75;

-- 5. Mengurutkan siswa berdasarkan nilai tertinggi ke terendah
SELECT nama, nilai 
FROM siswa 
ORDER BY nilai DESC;

-- 6. Menggabungkan WHERE dan ORDER BY (Saring nilai >= 75 lalu urutkan)
SELECT nama, nilai 
FROM siswa 
WHERE nilai >= 75 
ORDER BY nilai DESC;
