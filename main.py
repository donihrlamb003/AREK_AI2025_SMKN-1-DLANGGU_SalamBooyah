import os
import time
from datetime import datetime

class ModernSkalaCalculator:
    def __init__(self):
        self.skala = None
        self.history = []
        
    def clear_screen(self):  
        """Membersihkan layar"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_color(self, text, color_code):
        """Print text dengan color code"""
        print(f"\033[{color_code}m{text}\033[0m")
    
    def animate_text(self, text, delay=0.03):
        """Animasi ketik untuk teks"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    def fmt_num(self, number, precision=2):
        """Helper untuk format angka: titik jadi koma (Logika Kode 1)"""
        # Format angka dengan presisi tertentu, lalu ganti titik dengan koma
        formatted = f"{number:.{precision}f}"
        # Hapus .00 jika bulat agar lebih rapi
        if formatted.endswith(",00") or formatted.endswith(".00"):
             return str(int(number))
        return formatted.replace('.', ',')
    
    def print_header(self):
        """Header dengan design modern (Style Kode 2)"""
        self.clear_screen()
        print("=" * 50)
        self.print_color("🚀 MODERN SCALE CALCULATOR 🚀", "1;36")
        print("=" * 50)
        print()
        
    def print_card(self, title, content, color="36"):
        """Menampilkan card style modern (Style Kode 2 - Lebar 60)"""
        width = 60
        print("┌" + "─" * (width-2) + "┐")
        self.print_color(f"│ {title:^{width-4}} │", f"1;{color}")
        print("├" + "─" * (width-2) + "┤")
        for line in content:
            # Membersihkan kode warna ANSI untuk menghitung padding yang benar
            clean_line = line.replace('\033[1;33m', '').replace('\033[1;36m', '').replace('\033[0m', '')
            padding = width - 4 - len(clean_line)
            if padding < 0: padding = 0
            print(f"│ {line}{' ' * padding} │")
        print("└" + "─" * (width-2) + "┘")
        print()

    def show_menu_header(self, title, subtitle, color="33"):
        """Menampilkan header untuk menu (Fitur Kode 2)"""
        print()
        print("🎯 " + "="*50)
        self.print_color(f"📐 {title}", f"1;{color}")
        self.print_color(f"🔹 {subtitle}", f"1;{color}")
        print("🎯 " + "="*50)
        print()
    
    def show_welcome(self):
        """Animasi welcome"""
        self.print_header()
        welcome_text = "✨ Selamat datang di Modern Scale Calculator! ✨"
        self.animate_text(welcome_text, 0.02)
        print()
        
        # Info card (Style Kode 2)
        info_content = [
            "📐 Hitung skala desain bangunan dengan mudah",
            "🔄 Konversi dua arah: gambar ↔ asli", 
            "📊 Hasil dalam multiple units (m, cm, mm)",
            "💾 Riwayat perhitungan tersimpan",
            "🎨 Interface modern dan user-friendly"
        ]
        self.print_card("🌟 FITUR UTAMA", info_content, "35")
        time.sleep(1)
    
    def show_formula_explanation(self):
        """Menampilkan penjelasan rumus"""
        formula_content = [
            "📏 Rumus Dasar: Skala = 1 : S",
            "",
            "🎯 GAMBAR → ASLI:",
            " Asli (m) = (Gambar (cm) × S) ÷ 100",
            "",
            "🎯 ASLI → GAMBAR:", 
            " Gambar (cm) = (Asli (m) × 100) ÷ S",
            "",
            "💡 Keterangan:",
            " S = faktor skala (contoh: 100 untuk skala 1:100)"
        ]
        self.print_card("🧮 PENJELASAN RUMUS", formula_content, "34")
    
    def input_skala(self):
        """Input skala dengan validasi"""
        while True:
            try:
                print("🎨 " + "="*50)
                self.print_color("📐 SETTING SKALA", "1;33")
                print("🎨 " + "="*50)
                
                print("\nContoh input: 50, 100, 200, atau 33,5")
                # Replace koma dengan titik agar bisa diolah Python
                skala_input = input("🎯 Masukkan faktor skala (1:__): ").strip().replace(',', '.')
                
                if not skala_input:
                    self.print_color("❌ Error: Skala tidak boleh kosong!", "1;31")
                    continue
                
                skala = float(skala_input)
                
                if skala <= 0:
                    self.print_color("❌ Error: Skala harus lebih besar dari 0!", "1;31")
                    continue
                
                self.skala = skala
                
                val_skala = int(skala) if skala.is_integer() else self.fmt_num(skala, 1)
                success_msg = f"✅ Skala berhasil diatur: 1:{val_skala}"
                self.print_color(success_msg, "1;32")
                print()
                break
                
            except ValueError:
                self.print_color("❌ Error: Masukkan angka yang valid!", "1;31")
    
    def input_ukuran(self, prompt, satuan="cm"):
        """Input ukuran dengan validasi"""
        while True:
            try:
                print(f"\n📏 {prompt}")
                # Replace koma dengan titik untuk input
                raw_input = input(f"🎯 Ukuran ({satuan}): ").strip().replace(',', '.')
                ukuran = float(raw_input)
                
                if ukuran < 0:
                    self.print_color("❌ Error: Ukuran tidak boleh negatif!", "1;31")
                    continue
                
                return ukuran
                
            except ValueError:
                self.print_color("❌ Error: Masukkan angka yang valid!", "1;31")
    
    def konversi_satuan_cm(self, nilai_cm):
        """Konversi dari cm ke berbagai satuan"""
        return {
            'm': nilai_cm / 100,
            'cm': nilai_cm,
            'mm': nilai_cm * 10
        }
    
    def konversi_satuan_m(self, nilai_m):
        """Konversi dari m ke berbagai satuan"""
        return {
            'm': nilai_m,
            'cm': nilai_m * 100,
            'mm': nilai_m * 1000
        }
    
    def hitung_gambar_ke_asli(self):
        """Menu 1: Gambar → Asli (Logika Kode 1, Tampilan Kode 2)"""
        self.print_header()
        
        # Header menu style Kode 2
        self.show_menu_header(
            "GAMBAR → UKURAN ASLI", 
            "Konversi ukuran gambar (cm) ke ukuran sebenarnya (m)"
        )
        
        # Card proses style Kode 2
        process_content = [
            "📥 INPUT: Ukuran pada gambar (cm)",
            "🔄 PROSES: (Gambar × Skala) ÷ 100", 
            "📤 OUTPUT: Ukuran sebenarnya (m)",
            ""
        ]
        self.print_card("🔍 PROSES KONVERSI", process_content, "34")
        
        print("📝 Masukkan data ukuran pada gambar:")
        ukuran_gambar_cm = self.input_ukuran("Ukuran pada gambar", "cm")
        
        # Hitung (Logika Kode 1)
        ukuran_asli_cm = ukuran_gambar_cm * self.skala
        ukuran_asli_m = ukuran_asli_cm / 100
        
        # Format string untuk tampilan
        val_gbr = self.fmt_num(ukuran_gambar_cm, 2)
        val_skl = int(self.skala) if self.skala.is_integer() else self.fmt_num(self.skala, 1)
        val_res_cm = self.fmt_num(ukuran_asli_cm, 2)
        val_res_m = self.fmt_num(ukuran_asli_m, 3)
        
        # Tampilan Hasil Style Kode 2 (Detail)
        result_content = [
            f"📐 Skala Saat Ini : 1:{val_skl}",
            "─" * 45,
            f"📥 Input Gambar : {val_gbr} cm",
            f"✖️ Dikali Skala : {val_gbr} × {val_skl}",
            f"🧮 Hasil (cm)   : {val_res_cm} cm", 
            f"🔀 Konversi ke m: {val_res_cm} ÷ 100",
            "─" * 45,
            f"🎯 HASIL AKHIR  : {val_res_m} m"
        ]
        self.print_card("🎉 HASIL PERHITUNGAN", result_content, "32")
        
        # Konversi lengkap (Style Kode 2)
        hasil_konversi = self.konversi_satuan_m(ukuran_asli_m)
        print("📊 " + "\033[1;36mKONVERSI LENGKAP:\033[0m")
        print(f" ➡️ {self.fmt_num(hasil_konversi['m'], 3):>10} m")
        print(f" ➡️ {self.fmt_num(hasil_konversi['cm'], 2):>10} cm") 
        print(f" ➡️ {self.fmt_num(hasil_konversi['mm'], 0):>10} mm")
        
        # Simpan ke history
        self.history.append({
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'jenis': 'GAMBAR → ASLI',
            'input': f"{val_gbr} cm",
            'skala': f"1:{val_skl}",
            'hasil': f"{val_res_m} m",
            'detail': f"{val_gbr}cm gambar → {val_res_m}m asli"
        })
    
    def hitung_asli_ke_gambar(self):
        """Menu 2: Asli → Gambar (Logika Kode 1, Tampilan Kode 2)"""
        self.print_header()
        
        # Header menu style Kode 2
        self.show_menu_header(
            "UKURAN ASLI → GAMBAR", 
            "Konversi ukuran sebenarnya (m) ke ukuran gambar (cm)"
        )
        
        # Card proses style Kode 2
        process_content = [
            "📥 INPUT: Ukuran sebenarnya (meter)",
            "🔄 PROSES: (Asli × 100) ÷ Skala", 
            "📤 OUTPUT: Ukuran pada gambar (cm)",
            ""
        ]
        self.print_card("🔍 PROSES KONVERSI", process_content, "34")
        
        print("📝 Masukkan data ukuran sebenarnya:")
        ukuran_asli_m = self.input_ukuran("Ukuran sebenarnya", "m")
        
        # Hitung (Logika Kode 1)
        ukuran_asli_cm_input = ukuran_asli_m * 100
        ukuran_gambar_cm = ukuran_asli_cm_input / self.skala
        
        # Format string
        val_asli = self.fmt_num(ukuran_asli_m, 3)
        val_asli_cm = self.fmt_num(ukuran_asli_cm_input, 2)
        val_skl = int(self.skala) if self.skala.is_integer() else self.fmt_num(self.skala, 1)
        val_res = self.fmt_num(ukuran_gambar_cm, 2)
        
        # Tampilan Hasil Style Kode 2
        result_content = [
            f"📐 Skala Saat Ini : 1:{val_skl}",
            "─" * 45,
            f"📥 Input Asli   : {val_asli} m",
            f"🔀 Konversi ke cm : {val_asli} × 100",
            f"🧮 Hasil (cm)   : {val_asli_cm} cm",
            f"➗ Dibagi Skala  : {val_asli_cm} ÷ {val_skl}",
            "─" * 45,
            f"🎯 HASIL AKHIR  : {val_res} cm"
        ]
        self.print_card("🎉 HASIL PERHITUNGAN", result_content, "32")
        
        # Konversi lengkap
        hasil_konversi = self.konversi_satuan_cm(ukuran_gambar_cm)
        print("📊 " + "\033[1;36mKONVERSI LENGKAP:\033[0m")
        print(f" ➡️ {self.fmt_num(hasil_konversi['cm'], 2):>10} cm")
        print(f" ➡️ {self.fmt_num(hasil_konversi['m'], 4):>10} m")
        print(f" ➡️ {self.fmt_num(hasil_konversi['mm'], 1):>10} mm")
        
        # Simpan ke history
        self.history.append({
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'jenis': 'ASLI → GAMBAR',
            'input': f"{val_asli} m",
            'skala': f"1:{val_skl}",
            'hasil': f"{val_res} cm",
            'detail': f"{val_asli}m asli → {val_res}cm gambar"
        })
    
    def show_history(self):
        """Menampilkan riwayat perhitungan (Style Kode 2)"""
        if not self.history:
            self.print_card("📝 RIWAYAT", ["Belum ada riwayat perhitungan"], "35")
            return
        
        history_content = []
        for i, item in enumerate(self.history[-5:], 1): # Tampilkan 5 terakhir
            history_content.append(f"{i}. [{item['timestamp']}]")
            history_content.append(f" {item['jenis']}")
            history_content.append(f" Input: {item['input']} | Skala: {item['skala']}")
            history_content.append(f" Hasil: {item['hasil']}")
            history_content.append("─" * 45)
        
        self.print_card("📝 RIWAYAT TERAKHIR (5 terbaru)", history_content, "35")
    
    def show_quick_calc(self):
        """Kalkulator cepat untuk skala umum (Style Kode 2)"""
        self.print_header()
        self.print_card("⚡ KALKULATOR CEPAT", ["Skala umum yang sering digunakan"], "36")
        
        skala_umum = [50, 100, 200, 500]
        ukuran_contoh = 5 # cm di gambar
        
        quick_content = []
        for skala in skala_umum:
            asli_cm = ukuran_contoh * skala
            asli_m = asli_cm / 100
            # Format desimal koma (Logika Kode 1)
            str_asli = self.fmt_num(asli_m, 2)
            quick_content.append(f"1:{skala:<3d} → {ukuran_contoh}cm gambar = {str_asli}m asli")
        
        self.print_card("📊 CONTOH: GAMBAR → ASLI", quick_content, "34")
        
        print()
        
        # Contoh untuk Asli → Gambar
        ukuran_contoh_asli = 10 # m asli
        quick_content2 = []
        for skala in skala_umum:
            gambar_cm = (ukuran_contoh_asli * 100) / skala
            # Format desimal koma (Logika Kode 1)
            str_gbr = self.fmt_num(gambar_cm, 2)
            quick_content2.append(f"1:{skala:<3d} → {ukuran_contoh_asli}m asli = {str_gbr}cm gambar")
        
        self.print_card("📊 CONTOH: ASLI → GAMBAR", quick_content2, "34")
    
    def main_menu(self):
        """Menu utama dengan design modern (Style Kode 2)"""
        while True:
            self.print_header()
            
            # Info skala saat ini
            if self.skala:
                val_skala = int(self.skala) if self.skala.is_integer() else self.fmt_num(self.skala, 1)
                skala_info = f"🎯 Skala saat ini: 1:{val_skala}"
                self.print_color(skala_info, "1;32")
                print()
            
            # Menu options dengan penjelasan satuan (Layout Kode 2)
            menu_content = [
                "1. 🎯 Gambar → Asli (cm → m)",
                "2. 🎨 Asli → Gambar (m → cm)", 
                "3. ⚡ Kalkulator Cepat",
                "4. 📝 Lihat Riwayat",
                "5. 🔧 Ganti Skala",
                "6. 📚 Lihat Rumus", 
                "7. 🚪 Keluar"
            ]
            self.print_card("📋 MENU UTAMA", menu_content, "36")
            
            # Input pilihan
            print("👉 " + "="*40)
            pilihan = input("🎯 Pilih menu (1-7): ").strip()
            
            if pilihan == '1':
                self.hitung_gambar_ke_asli()
            elif pilihan == '2':
                self.hitung_asli_ke_gambar()
            elif pilihan == '3':
                self.show_quick_calc()
            elif pilihan == '4':
                self.print_header()
                self.show_history()
            elif pilihan == '5':
                self.input_skala()
                continue
            elif pilihan == '6':
                self.print_header()
                self.show_formula_explanation()
            elif pilihan == '7':
                self.show_exit()
                break
            else:
                self.print_color("❌ Error: Pilih menu 1-7!", "1;31")
                time.sleep(1)
                continue
            
            # Continue prompt
            if pilihan in ['1', '2', '3', '4', '6']:
                print("\n" + "👉 " + "="*40)
                lanjut = input("🔄 Lanjutkan? (y/n): ").strip().lower()
                if lanjut != 'y':
                    self.show_exit()
                    break
    
    def show_exit(self):
        """Animasi exit"""
        self.print_header()
        goodbye_text = "👋 Terima kasih telah menggunakan Modern Scale Calculator!"
        self.animate_text(goodbye_text, 0.03)
        print()
        
        stats_content = [
            f"📊 Total perhitungan: {len(self.history)}",
            "🌟 Sampai jumpa lagi!",
            "💡 Developed with ❤️ untuk desain bangunan"
        ]
        self.print_card("📈 STATISTIK", stats_content, "35")
        time.sleep(2)

def main():
    """Fungsi utama"""
    try:
        calculator = ModernSkalaCalculator()
        calculator.show_welcome()
        input("\n🎯 Tekan Enter untuk melanjutkan...")
        calculator.input_skala()
        calculator.main_menu()
    except KeyboardInterrupt:
        print("\n\n❌ Program dihentikan oleh user")
    except Exception as e:
        print(f"\n\n💥 Error: {e}")

if __name__ == "__main__":
    main()