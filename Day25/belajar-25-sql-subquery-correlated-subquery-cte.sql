-- =========================================================
-- SQL DAY 25
-- Materi: Subquery, Correlated Subquery, CTE
-- =========================================================

-- Data latihan:
-- nama | nilai | kalas
-- Owi   | 80    | A
-- Joni  | 65    | B
-- Wowo  | 90    | A
-- Didi  | 70    | B
-- Eko   | 100   | A


-- 1. Siswa di atas rata-rata seluruh siswa
SELECT nama, nilai
FROM siswa
WHERE nilai > (
    SELECT AVG(nilai)
    FROM siswa
)
ORDER BY nilai DESC;


-- 2. Siswa dengan nilai tertinggi
SELECT nama, nilai, kalas
FROM siswa
WHERE nilai = (
    SELECT MAX(nilai)
    FROM siswa
);


-- 3. Correlated subquery:
--    siswa di bawah rata-rata kelasnya sendiri
SELECT nama, nilai, kalas
FROM siswa
WHERE nilai < (
    SELECT AVG(nilai)
    FROM siswa AS siswa2
    WHERE siswa2.kalas = siswa.kalas
);


-- 4. Correlated subquery:
--    siswa di atas rata-rata kelasnya sendiri
SELECT nama, nilai, kalas
FROM siswa
WHERE nilai > (
    SELECT AVG(nilai)
    FROM siswa AS siswa2
    WHERE siswa2.kalas = siswa.kalas
)
ORDER BY nilai DESC;


-- 5. Rata-rata kelas di samping setiap siswa
SELECT
    nama,
    nilai,
    kalas,
    (
        SELECT AVG(nilai)
        FROM siswa AS siswa2
        WHERE siswa2.kalas = siswa.kalas
    ) AS rata_rata
FROM siswa;


-- 6. Selisih nilai siswa dengan rata-rata kelas
SELECT
    nama,
    nilai,
    kalas,
    (
        SELECT AVG(nilai)
        FROM siswa AS siswa2
        WHERE siswa2.kalas = siswa.kalas
    ) AS rata_rata,
    nilai - (
        SELECT AVG(nilai)
        FROM siswa AS siswa2
        WHERE siswa2.kalas = siswa.kalas
    ) AS selisih
FROM siswa;


-- 7. Siswa di bawah rata-rata kelas + rata-rata kelas
SELECT
    nama,
    nilai,
    kalas,
    (
        SELECT AVG(nilai)
        FROM siswa AS siswa2
        WHERE siswa2.kalas = siswa.kalas
    ) AS rata_rata
FROM siswa
WHERE nilai < (
    SELECT AVG(nilai)
    FROM siswa AS siswa2
    WHERE siswa2.kalas = siswa.kalas
);


-- 8. CTE: rata-rata setiap kelas
WITH rata_kelas AS (
    SELECT kalas, AVG(nilai) AS rata_rata
    FROM siswa
    GROUP BY kalas
)
SELECT *
FROM rata_kelas;


-- =========================================================
-- CATATAN KONSEP
-- =========================================================

-- siswa       = patokan pada query luar
-- siswa2      = pencari pada query dalam
--
-- siswa.kalas = kelas dari baris query luar yang sedang diperiksa
-- siswa2.kalas = kelas dari baris query dalam
--
-- WHERE siswa2.kalas = siswa.kalas
-- artinya: cari baris siswa2 yang kelasnya sama dengan kelas siswa
-- yang sedang menjadi patokan.


-- Langkah berikutnya:
-- JOIN antara siswa dan CTE rata_kelas.
