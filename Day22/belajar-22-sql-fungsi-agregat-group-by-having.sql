-- SQL DAY 22
-- PostgreSQL 18 / pgAdmin
-- Fokus: COUNT, SUM, AVG, MAX, MIN, GROUP BY, HAVING

-- Data latihan:
-- id | nama | nilai | kalas
-- 1  | owi  | 80    | A
-- 2  | joni | 65    | B
-- 3  | wowo | 90    | A
-- 4  | didi | 70    | B
-- 5  | eko  | 100   | A

-- COUNT
SELECT COUNT(*) AS jumlah_siswa
FROM siswa;

SELECT COUNT(*) AS lulus
FROM siswa
WHERE nilai >= 75;

-- SUM
SELECT SUM(nilai) AS total_nilai
FROM siswa;

SELECT SUM(nilai) AS total_lulus
FROM siswa
WHERE nilai >= 75;

-- AVG
SELECT AVG(nilai) AS rata_rata_lulus
FROM siswa
WHERE nilai >= 75;

-- Semua fungsi agregat sekaligus
SELECT
    COUNT(*) AS jumlah,
    SUM(nilai) AS total,
    AVG(nilai) AS rata_rata,
    MAX(nilai) AS tertinggi,
    MIN(nilai) AS terendah
FROM siswa;

-- Agregat untuk siswa lulus
SELECT
    COUNT(*) AS jumlah,
    SUM(nilai) AS total,
    AVG(nilai) AS rata_rata,
    MAX(nilai) AS tertinggi,
    MIN(nilai) AS terendah
FROM siswa
WHERE nilai >= 75;

-- GROUP BY
SELECT kalas, COUNT(*) AS jumlah
FROM siswa
GROUP BY kalas;

SELECT kalas, COUNT(*) AS jumlah, SUM(nilai) AS total
FROM siswa
GROUP BY kalas
ORDER BY kalas ASC;

SELECT kalas, COUNT(*) AS jumlah, AVG(nilai) AS rata_rata
FROM siswa
GROUP BY kalas
ORDER BY kalas ASC;

SELECT
    kalas,
    COUNT(*) AS jumlah,
    SUM(nilai) AS total,
    AVG(nilai) AS rata_rata,
    MAX(nilai) AS tertinggi,
    MIN(nilai) AS terendah
FROM siswa
GROUP BY kalas
ORDER BY kalas ASC;

-- HAVING
SELECT kalas, COUNT(*) AS jumlah
FROM siswa
GROUP BY kalas
HAVING COUNT(*) > 2
ORDER BY kalas ASC;

SELECT kalas, AVG(nilai) AS rata_rata
FROM siswa
GROUP BY kalas
HAVING AVG(nilai) >= 80
ORDER BY kalas ASC;

SELECT kalas, SUM(nilai) AS total
FROM siswa
GROUP BY kalas
HAVING SUM(nilai) > 200
ORDER BY kalas ASC;

-- WHERE + GROUP BY + HAVING
SELECT kalas, COUNT(*) AS jumlah
FROM siswa
WHERE nilai >= 70
GROUP BY kalas
HAVING COUNT(*) >= 2
ORDER BY kalas ASC;

SELECT kalas, SUM(nilai) AS total
FROM siswa
WHERE nilai >= 70
GROUP BY kalas
HAVING SUM(nilai) > 200
ORDER BY kalas ASC;

SELECT kalas, AVG(nilai) AS rata_rata
FROM siswa
WHERE nilai >= 70
GROUP BY kalas
HAVING AVG(nilai) >= 80
ORDER BY kalas ASC;

SELECT kalas, COUNT(*) AS jumlah, AVG(nilai) AS rata_rata
FROM siswa
WHERE nilai >= 65
GROUP BY kalas
HAVING COUNT(*) >= 2 AND AVG(nilai) >= 70
ORDER BY AVG(nilai) DESC;

SELECT
    kalas,
    COUNT(*) AS jumlah,
    SUM(nilai) AS total,
    MAX(nilai) AS tertinggi
FROM siswa
WHERE nilai >= 65
GROUP BY kalas
HAVING SUM(nilai) > 100
ORDER BY SUM(nilai) DESC;

-- Catatan:
-- WHERE = filter baris sebelum GROUP BY
-- GROUP BY = mengelompokkan data
-- HAVING = filter hasil kelompok
-- COUNT = jumlah
-- SUM = total
-- AVG = rata-rata
-- MAX = terbesar
-- MIN = terkecil
-- AS = alias
