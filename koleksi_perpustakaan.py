from abc import ABC, abstractmethod


class KoleksiPerpustakaan(ABC):
    def __init__(self, kode_koleksi, judul, pengarang, tahun_terbit, penerbit):
        self.kode_koleksi = kode_koleksi
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.penerbit = penerbit

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def info_dasar(self):
        return (
            f"Kode: {self.kode_koleksi}\n"
            f"Judul: {self.judul}\n"
            f"Pengarang: {self.pengarang}\n"
            f"Tahun Terbit: {self.tahun_terbit}\n"
            f"Penerbit: {self.penerbit}\n"
        )
