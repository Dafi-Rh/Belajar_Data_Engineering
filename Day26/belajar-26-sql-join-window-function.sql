-- SQL DAY 26
-- Materi: JOIN, CTE, Window Function

-- Data saat ini:
-- Owi 80 A
-- Joni 65 B
-- Wowo 90 A
-- Didi 70 B
-- Eko 100 A
-- Jefry 70 B
-- Tedy 70 B

-- 1. CTE rata-rata per kelas
WITH rata_kelas AS (
    SELECT kalas, AVG(nilai) AS rata_rata
    FROM siswa
    GROUP BY kalas
)
SELECT *
FROM rata_kelas;

-- 2. CTE + JOIN: rata-rata kelas setiap siswa
WITH rata_kalas AS (
    SELECT kalas, AVG(nilai) AS rata_rata
    FROM siswa
    GROUP BY kalas
)
SELECT s.nama, s.nilai, s.kalas, r.rata_rata
FROM siswa AS s
JOIN rata_kalas AS r
    ON s.kalas = r.kalas;

-- 3. Siswa di atas rata-rata kelas
WITH rata_kalas AS (
    SELECT kalas, AVG(nilai) AS rata_rata
    FROM siswa
    GROUP BY kalas
)
SELECT s.nama, s.nilai, r.kalas, r.rata_rata
FROM siswa AS s
JOIN rata_kalas AS r
    ON s.kalas = r.kalas
WHERE s.nilai > r.rata_rata
ORDER BY s.nilai DESC;

-- 4. Nilai tertinggi per kelas: MAX + JOIN
WITH top AS (
    SELECT kalas, MAX(nilai) AS tertinggi
    FROM siswa
    GROUP BY kalas
)
SELECT s.nama, s.nilai, t.kalas
FROM siswa AS s
JOIN top AS t
    ON s.kalas = t.kalas
WHERE s.nilai = t.tertinggi
ORDER BY s.nilai DESC;

-- 5. Nilai terendah per kelas: MIN + JOIN
WITH bottom AS (
    SELECT kalas, MIN(nilai) AS terendah
    FROM siswa
    GROUP BY kalas
)
SELECT s.nama, s.nilai, b.kalas, b.terendah
FROM siswa AS s
JOIN bottom AS b
    ON s.kalas = b.kalas
WHERE s.nilai = b.terendah
ORDER BY s.nilai DESC;

-- 6. Selisih nilai dengan rata-rata kelas
WITH rata_kalas AS (
    SELECT kalas, AVG(nilai) AS rata_rata
    FROM siswa
    GROUP BY kalas
)
SELECT s.nama, s.nilai, r.kalas,
       s.nilai - r.rata_rata AS selisih
FROM siswa AS s
JOIN rata_kalas AS r
    ON s.kalas = r.kalas
ORDER BY selisih DESC;

-- 7. Hanya siswa di atas rata-rata kelas
WITH rata_kalas AS (
    SELECT kalas, AVG(nilai) AS rata_rata
    FROM siswa
    GROUP BY kalas
)
SELECT s.nama, s.nilai, r.kalas,
       s.nilai - r.rata_rata AS selisih
FROM siswa AS s
JOIN rata_kalas AS r
    ON s.kalas = r.kalas
WHERE s.nilai > r.rata_rata
ORDER BY selisih DESC;

-- 8. ROW_NUMBER()
SELECT nama, nilai, kalas,
       ROW_NUMBER() OVER (
           PARTITION BY kalas
           ORDER BY nilai DESC
       ) AS urutan
FROM siswa;

-- 9. Satu siswa tertinggi per kelas
WITH top AS (
    SELECT nama, nilai, kalas,
           ROW_NUMBER() OVER (
               PARTITION BY kalas
               ORDER BY nilai DESC
           ) AS ranking
    FROM siswa
)
SELECT nama, nilai, kalas
FROM top
WHERE ranking = 1;

-- 10. Dua siswa teratas per kelas
WITH top AS (
    SELECT nama, nilai, kalas,
           ROW_NUMBER() OVER (
               PARTITION BY kalas
               ORDER BY nilai DESC
           ) AS ranking
    FROM siswa
)
SELECT nama, nilai, kalas
FROM top
WHERE ranking <= 2;

-- 11. RANK()
SELECT nama, nilai, kalas,
       RANK() OVER (
           PARTITION BY kalas
           ORDER BY nilai DESC
       ) AS ranking
FROM siswa;

-- 12. DENSE_RANK()
SELECT nama, nilai, kalas,
       DENSE_RANK() OVER (
           PARTITION BY kalas
           ORDER BY nilai DESC
       ) AS ranking
FROM siswa;

-- 13. DENSE_RANK ranking 2
WITH top AS (
    SELECT nama, nilai, kalas,
           DENSE_RANK() OVER (
               PARTITION BY kalas
               ORDER BY nilai DESC
           ) AS ranking
    FROM siswa
)
SELECT nama, nilai, kalas
FROM top
WHERE ranking = 2;

-- 14. LAG tanpa PARTITION
SELECT nama, nilai, kalas,
       LAG(nilai) OVER (
           ORDER BY nilai DESC
       ) AS nilai_sebelumnya
FROM siswa;

-- 15. LAG dalam kelas yang sama
SELECT nama, nilai, kalas,
       LAG(nilai) OVER (
           PARTITION BY kalas
           ORDER BY nilai DESC
       ) AS nilai_sebelumnya
FROM siswa;

-- 16. LEAD
SELECT nama, nilai, kalas,
       LEAD(nilai) OVER (
           PARTITION BY kalas
           ORDER BY nilai DESC
       ) AS nilai_berikutnya
FROM siswa;

-- 17. LAG + CTE + perubahan
WITH data AS (
    SELECT nama, nilai, kalas,
           LAG(nilai) OVER (
               PARTITION BY kalas
               ORDER BY nilai DESC
           ) AS nilai_sebelumnya
    FROM siswa
)
SELECT nama, nilai, kalas,
       nilai - nilai_sebelumnya AS perubahan
FROM data;

-- KONSEP UTAMA DAY 26
-- JOIN      = menghubungkan data dari dua sumber
-- CTE       = hasil sementara seperti tabel
-- GROUP BY  = membuat kelompok hasil
-- PARTITION = kelompok untuk window function tanpa menghilangkan baris
-- ROW_NUMBER = nomor unik per baris
-- RANK      = tie sama, ada gap
-- DENSE_RANK= tie sama, tanpa gap
-- LAG       = baris sebelumnya
-- LEAD      = baris berikutnya
