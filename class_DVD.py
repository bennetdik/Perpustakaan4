from koleksi_perpustakaan import KoleksiPerpustakaan

class DVD(KoleksiPerpustakaan):
    def __init__(self, judul, tahun_terbit, penerbit, kode, durasi):
        super().__init__(kode, judul, "-", tahun_terbit, penerbit)
        self.durasi = durasi

    def info(self):
        return (
            f"{self.info_dasar()}\n"
            f"durasi: {self.durasi} menit"
        )

    def tampilkan_detail(self, nomor):
        print(f"Koleksi Nomor {nomor} :")
        print(f"Jenis         : DVD")
        print(f"Kode Koleksi  : {self.kode_koleksi}")
        print(f"Judul         : {self.judul}")
        print(f"Tahun Terbit  : {self.tahun_terbit}")
        print(f"Penerbit      : {self.penerbit}")
        print(f"Durasi        : {self.durasi} menit")

    def info_dasar(self):
        return super().info_dasar()
