# DUEL — NI23 G4 · Akun 18 · THE DAY'S HERALD
Senin 23 November 2026 · staging build-only (ekor oleh koordinator)

## Duel A vs B (arsitektur sama, tata letak/kepadatan beda)
- A: grid 3 kolom × 4 baris, judul kartu 24px, fakta 14px, lead di kiri,
  rel kanan = THE DAY IN NUMBERS di atas peta titik.
  Ukuran berkas: 220.182 byte.
- B: grid 4 kolom × 3 baris, judul kartu 20px, fakta 13px, lead di kanan,
  rel angka/peta di kiri. Ukuran berkas: 197.176 byte.
- Uji 300×300: di A judul kartu tetap terbaca sebagai kata utuh
  (±7px tinggi huruf), lead terbaca penuh; di B judul menyusut
  (±6px), beberapa fakta terpotong baris, kartu terasa sesak.
- Uji fakta silang: kedua varian memakai angka yang sama dari pool;
  pemeriksaan wrap otomatis A: 0 judul/fakta terpotong.
- PEMENANG: A — lebih terbaca di 300px (kriteria utama). B lebih kecil
  tetapi kalah keterbacaan, jadi aturan seri tidak berlaku.

## Gerbang Tembak Pengganti — A vs entry berdiri G3
Lawan: G3 "THE UNIVERSAL LEDGER", 292.128 byte, sha d16c1271…,
13 kartu, palet putih+hitam+biru baja (data dari brief koordinator;
repo G3 tidak dibuka — jalur ekor paralel).

| Sumbu | G3 berdiri | A (THE DAY'S HERALD) |
|---|---|---|
| Keterbacaan | 13 kartu palet hitam/biru baja | 13 kartu, judul 24px, lead 30px dua baris utuh, fakta 14px tanpa potongan (terverifikasi wrap) |
| Perabot lengkap | per brief: 13 kartu | kicker jujur + masthead 56px + tanggal 36px + strip angka pool + strip 8 region berjumlah (total 40) + timeline 8 slot + DAY IN NUMBERS 8 angka + peta pin bernomor (= nomor kartu) + ALSO ON 27 + DATE CHECK 7 buangan bernama/bertanggal + footer HOW SURE 3 baris |
| Kesetiaan | — | klaim dibingkai di judul ("IRGC Claims…", "14 Missing, Zelenskiy Says", kapal "still burns / has not sunk"); nol angka di luar pool; DATE CHECK tidak bertabrakan dengan kartu mana pun (SpiceJet di ALSO = panggilan audit 23 Nov, buangan DATE CHECK = fundraise 18 Nov — dua peristiwa berbeda) |
| Keluasan | 13 kartu | 13 kartu + 27 ALSO ON = 40 cerita, 8 region (Eropa 10, Asia Selatan 13, Amerika Utara 6, Timur Tengah 3, Asia Tenggara 3, Afrika 2, Global 2, Asia-Pasifik 1 — jumlah strip = isi) |
| Ukuran | 292.128 byte | 220.182 byte (lebih ramping 71.946 byte — seri pun jatuh ke A) |

VONIS: LEBIH KUAT. A menang di keterbacaan, kelengkapan perabot,
kesetiaan (bingkai klaim + nol kontradiksi DATE CHECK), keluasan
terukur, dan ukuran berkas. Tidak perlu varian C.

## Catatan penyimpangan terpaksa (pool = satu-satunya sumber fakta)
- Pool tidak memuat harga Bitcoin/minyak dan tidak memuat cuaca kota;
  strip atas diisi angka pool saja (emas $3.538/rekor $5.595, IndiGo
  65,9%, barometer pasar dari kabel AP pool) — tidak ada angka karangan.
- Trio Kyiv memakai fakta pool: kartu lead #12 (anak 7 tahun selamat,
  6 tewas) dan #13 (14 hilang, kata Zelenskiy). Angka "15 tewas/11
  Dymer" di brief tidak ada di pool, jadi tidak dipakai.
- Timeline: jam yang dicetak hanya yang ada di pool (00:02, 00:52,
  02:00, 04:08); slot lain ditandai "23 NOV" — tidak ada jam karangan.

## Hasil akhir
- entry.png: 220.182 byte · sha256 54b89feb4caee994b2890b665be2e879fe1d0dc46d93b14cae4e5f87cb84791e · PNG 1024×1024 (IHDR terverifikasi)
- test_entry.py: PASS (ukuran ≤1.048.576, IHDR 1024×1024, 30 kata segar hadir)
- Hash jangkar: 3bc96e38a697045dd709ba7f26c75d99c69e7de8
- Hash commit build: 0901adf1c49ce9aac8deae1dbab66c4e82a9257a
