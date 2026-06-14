class Buku(KoleksiPerpustakaan):
    def __init__(self, kode, judul, tahun, penerbit, pengarang):
        super().__init__(kode, judul, tahun, penerbit)
        self.pengarang = pengarang

    def tampilkan_detail(self, nomor):
        print(f"Koleksi       : {nomor}")
        print(f"Jenis         : Buku")
        print(f"Kode Koleksi  : {self.kode_koleksi}")
        print(f"Judul         : {self.judul}")
        print(f"Tahun Terbit  : {self.tahun_terbit}")
        print(f"Pengarang     : {self.pengarang}")
        print(f"Penerbit      : {self.penerbit}")