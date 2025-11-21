# AREK_AI2025_SMKN-1-DLANGGU_SalamBooyah

🚀 Modern Scale Calculator

Modern Scale Calculator adalah aplikasi berbasis CLI (Command Line Interface) menggunakan Python yang dirancang untuk membantu arsitek, drafter, dan desainer menghitung konversi skala bangunan dengan cepat, akurat, dan tampilan yang estetis.

✨ Fitur Utama

    Konversi Dua Arah: Hitung ukuran Gambar ke Asli atau Asli ke Gambar.

    Multi-Satuan: Hasil ditampilkan otomatis dalam meter (m), sentimeter (cm), dan milimeter (mm).

    Riwayat Perhitungan: Menyimpan 5 perhitungan terakhir dalam sesi aktif.

    Fleksibel: Mendukung input desimal menggunakan titik (.) maupun koma (,).

    Antarmuka Modern: Tampilan berwarna, rapi, dan mudah dibaca.

💻 Prasyarat (Requirements)

Sebelum menjalankan program, pastikan komputer Anda sudah terinstal:

    Python 3.x (Dianjurkan versi 3.6 ke atas).

        Cek apakah sudah terinstal dengan mengetik python --version di terminal/CMD.

    Sistem Operasi: Windows, macOS, atau Linux (Program ini mendukung cross-platform).

Catatan: Program ini hanya menggunakan pustaka standar bawaan Python (os, time, datetime), jadi tidak perlu menginstall library tambahan (pip install).

🛠️ Cara Instalasi

    Siapkan File Python:

        Buat file baru di komputer Anda, beri nama skala_calculator.py.

        Salin (Copy) seluruh kode program yang Anda miliki.

        Tempel (Paste) kode tersebut ke dalam file skala_calculator.py dan simpan (Save).

    Buka Terminal / Command Prompt:

        Windows: Tekan Win + R, ketik cmd, lalu Enter.

        Mac/Linux: Buka aplikasi Terminal.

    Masuk ke Folder Program: Gunakan perintah cd untuk masuk ke folder tempat Anda menyimpan file.

        Contoh: cd Documents/ProjectSkala

▶️ Cara Menjalankan Program

Ketik perintah berikut di terminal Anda:
Bash

python skala_calculator.py

(Jika perintah python tidak bekerja, coba gunakan python3)

📖 Panduan Penggunaan

1. Mengatur Skala Awal

Saat pertama kali dibuka, program akan meminta Anda memasukkan skala.

    Masukkan angka skala (contoh: 100 untuk skala 1:100, atau 50 untuk 1:50).

    Tekan Enter.

2. Menu Utama

Anda akan melihat pilihan menu berikut:

    [1] Gambar → Asli: Masukkan ukuran di penggaris (cm), program menghitung ukuran bangunan nyata (m).

    [2] Asli → Gambar: Masukkan ukuran bangunan nyata (m), program menghitung berapa cm harus digambar.

    [3] Kalkulator Cepat: Melihat tabel perbandingan cepat untuk skala umum.

    [4] Lihat Riwayat: Melihat log perhitungan sebelumnya.

    [5] Ganti Skala: Mengubah settingan skala (misal dari 1:100 ke 1:50).

    [6] Lihat Rumus: Penjelasan matematika di balik perhitungan.

    [7] Keluar: Menutup program.

3. Tips Input

    Program menerima angka desimal.

    Anda bisa mengetik 2.5 atau 2,5 (program otomatis mengonversi koma menjadi titik).

⚠️ Pemecahan Masalah (Troubleshooting)

    Tampilan warna aneh/kode aneh muncul (misal: [36m):

        Ini terjadi jika terminal Anda tidak mendukung ANSI color codes. Coba gunakan terminal modern seperti PowerShell, Windows Terminal, VS Code Terminal, atau iTerm2.

    Error python is not recognized:

        Artinya Python belum masuk ke Environment Variables komputer Anda. Coba install ulang Python dan centang opsi "Add Python to PATH".

Selamat Menggunakan! 🏗️
