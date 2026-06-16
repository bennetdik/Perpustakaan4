from class_buku import Buku
from class_jurnal import Jurnal
from class_majalah import Majalah

# Menambal method abstract dari parent class agar tidak error saat program jalan
def info_dummy(self):
    return f"{self.judul}"

Buku.info = info_dummy
Buku.info_dasar = info_dummy
Jurnal.info = info_dummy
Jurnal.info_dasar = info_dummy
Majalah.info = info_dummy
Majalah.info_dasar = info_dummy

def main():
    daftar_koleksi = []

    while True:
        print("\n1. Tambah koleksi")
        print("2. Hapus koleksi")
        print("3. Tampilkan semua koleksi")
        print("4. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            print("\n--- TAMBAH KOLEKSI ---")
            print("1. Buku")
            print("2. Jurnal")
            print("3. Majalah")
            jenis = input("Pilih jenis koleksi: ")
            
            if jenis not in ["1", "2", "3"]:
                print("Jenis koleksi tidak valid.")
                continue

            kode = input("Masukkan Kode: ")
            judul = input("Masukkan Judul: ")
            
            # Khusus Jurnal/Majalah, biasanya pengarang diisi instansi/nama editor,
            # atau jika kosong bisa diisi "-" agar data tidak bergeser.
            pengarang = input("Masukkan Pengarang (isi '-' jika tidak ada): ")
            tahun = input("Masukkan Tahun Terbit: ")
            penerbit = input("Masukkan Penerbit: ")
            
            if jenis == "1":
                baru = Buku(kode, judul, tahun, penerbit, pengarang)
                daftar_koleksi.append(baru)
                print("Buku berhasil ditambahkan!")
                
            elif jenis == "2":
                edisi = input("Masukkan Edisi Jurnal: ")
                # Mengirim TEPAT 6 parameter sesuai urutan baru
                baru = Jurnal(kode, judul, pengarang, tahun, penerbit, edisi)
                daftar_koleksi.append(baru)
                print("Jurnal berhasil ditambahkan!")
                
            elif jenis == "3":
                edisi = input("Masukkan Edisi Majalah: ")
                # Mengirim TEPAT 6 parameter sesuai urutan baru
                baru = Majalah(kode, judul, pengarang, tahun, penerbit, edisi)
                daftar_koleksi.append(baru)
                print("Majalah berhasil ditambahkan!")
                
        elif pilihan == "2":
            print("\n--- HAPUS KOLEKSI ---")
            if not daftar_koleksi:
                print("Belum ada koleksi yang tersimpan.")
                continue
                
            kode_hapus = input("Masukkan Kode Koleksi yang ingin dihapus: ")
            ditemukan = False
            
            for koleksi in daftar_koleksi:
                if hasattr(koleksi, 'kode') and koleksi.kode == kode_hapus:
                    daftar_koleksi.remove(koleksi)
                    print(f"Koleksi dengan Kode {kode_hapus} berhasil dihapus!")
                    ditemukan = True
                    break
            
            if not ditemukan:
                print("Koleksi tidak ditemukan.")
                
        elif pilihan == "3":
            print("\n--- DAFTAR SEMUA KOLEKSI ---")
            if not daftar_koleksi:
                print("Perpustakaan masih kosong.")
                continue
                
            for index, koleksi in enumerate(daftar_koleksi, start=1):
                koleksi.tampilkan_detail(index)
                print("-" * 45)
                
        elif pilihan == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

if __name__ == "__main__":
    main()