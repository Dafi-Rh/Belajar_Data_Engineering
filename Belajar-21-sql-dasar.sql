-- SQL Day 21
-- PostgreSQL 18 / pgAdmin
-- Penguatan dasar SQL
--
-- Data latihan:
-- siswa
-- id | nama | nilai
-- 1  | owi  | 80
-- 2  | joni | 65
-- 3  | wowo | 90
-- 4  | didi | 70
-- 5  | eko  | 100

-- ============================================================
-- SELECT dan FROM
-- ============================================================

SELECT * FROM siswa;

SELECT nama, nilai
FROM siswa;


-- ============================================================
-- WHERE
-- ============================================================

SELECT nama, nilai
FROM siswa
WHERE nilai >= 75;


-- ============================================================
-- ORDER BY
-- ============================================================

-- ASC = ascending = kecil -> besar
SELECT nama, nilai
FROM siswa
ORDER BY nilai ASC;

-- DESC = descending = besar -> kecil
SELECT nama, nilai
FROM siswa
ORDER BY nilai DESC;


-- ============================================================
-- LIMIT
-- ============================================================

SELECT nama, nilai
FROM siswa
ORDER BY nilai DESC
LIMIT 3;

-- 2 siswa dengan nilai terendah
SELECT nama, nilai
FROM siswa
ORDER BY nilai ASC
LIMIT 2;


-- ============================================================
-- AND
-- ============================================================

SELECT nama, nilai
FROM siswa
WHERE nilai >= 70 AND nilai <= 90
ORDER BY nilai DESC;


-- ============================================================
-- BETWEEN
-- ============================================================

-- BETWEEN termasuk kedua batasnya
SELECT nama, nilai
FROM siswa
WHERE nilai BETWEEN 70 AND 90
ORDER BY nilai DESC;


-- ============================================================
-- IN dan NOT IN
-- ============================================================

SELECT nama, nilai
FROM siswa
WHERE nilai IN (65, 100);

SELECT nama, nilai
FROM siswa
WHERE nilai NOT IN (65, 100);


-- ============================================================
-- OR
-- ============================================================

SELECT nama, nilai
FROM siswa
WHERE nilai < 70 OR nilai > 90;


-- IN + OR + BETWEEN
SELECT nama, nilai
FROM siswa
WHERE nilai IN (65, 100)
   OR nilai BETWEEN 80 AND 90;


-- ============================================================
-- Membandingkan kolom dengan nilai
-- ============================================================

SELECT nama, nilai
FROM siswa
WHERE nilai IN (70, 80)
   OR nama = 'eko';


-- NOT dan <>
SELECT nama, nilai
FROM siswa
WHERE nilai BETWEEN 70 AND 100
  AND NOT nama = 'owi'
ORDER BY nilai DESC;

-- Bentuk lain:
SELECT nama, nilai
FROM siswa
WHERE nama <> 'owi';


-- ============================================================
-- Latihan Day 21 yang dikerjakan
-- ============================================================

-- 1. Nilai kurang dari 80
SELECT nama, nilai
FROM siswa
WHERE nilai < 80
ORDER BY nilai DESC;

-- 2. Nilai 80 atau 90
SELECT nama, nilai
FROM siswa
WHERE nilai IN (80, 90);

-- 3. Nilai 65 sampai 90, urut turun, maksimal 3
SELECT nama, nilai
FROM siswa
WHERE nilai BETWEEN 65 AND 90
ORDER BY nilai DESC
LIMIT 3;

-- 4. Bukan 65 dan 70, minimal 70, urut turun
SELECT nama, nilai
FROM siswa
WHERE nilai NOT IN (65, 70)
  AND nilai >= 70
ORDER BY nilai DESC;

-- 5. Nilai 65 atau 90
SELECT nama, nilai
FROM siswa
WHERE nilai IN (65, 90);

-- 6. Nilai kurang dari 70 atau lebih dari 90
SELECT nama, nilai
FROM siswa
WHERE nilai < 70 OR nilai > 90;

-- 7. Nilai 65 atau 100, atau 80 sampai 90
SELECT nama, nilai
FROM siswa
WHERE nilai IN (65, 100)
   OR nilai BETWEEN 80 AND 90;

-- 8. Nilai 70 atau 80, atau nama eko
SELECT nama, nilai
FROM siswa
WHERE nilai IN (70, 80)
   OR nama = 'eko';

-- 9. Nilai 70-100 tetapi bukan Owi, terbesar ke terkecil
SELECT nama, nilai
FROM siswa
WHERE nilai BETWEEN 70 AND 100
  AND NOT nama = 'owi'
ORDER BY nilai DESC;


-- ============================================================
-- Catatan:
-- Day 21 fokus pada fondasi SQL.
-- GROUP BY dan materi lanjutan belum dilanjutkan agar konsep dasar
-- benar-benar kuat terlebih dahulu.
