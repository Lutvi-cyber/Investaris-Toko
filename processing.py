"""Modul processing: class Barang dan Inventaris untuk pengolahan data."""


class Barang:
    """Satu record barang; atribut tambahan diterima lewat **kwargs."""

    def __init__(self, kode, nama, harga, stok, **atribut):
        self.kode, self.nama = kode, nama
        self.harga, self.stok = harga, stok
        self.atribut = atribut  # contoh: kategori, merek

    def nilai_total(self):
        """Nilai stok = harga x stok."""
        return self.harga * self.stok

    def __str__(self):
        return f"{self.kode} | {self.nama} | Rp{self.harga} | stok {self.stok}"


class Inventaris:
    """Kumpulan Barang beserta fungsi analisisnya."""

    def __init__(self, daftar=None):
        self.daftar = daftar if daftar else []

    def tambah(self, barang):
        """Tambah satu Barang ke daftar."""
        self.daftar.append(barang)

    def cari(self, kata):
        """Cari berdasarkan nama memakai filter + lambda."""
        return list(filter(lambda b: kata.lower() in b.nama.lower(), self.daftar))

    def urutkan_harga(self, turun=False):
        """Urutkan dengan lambda sebagai key sorted()."""
        return sorted(self.daftar, key=lambda b: b.harga, reverse=turun)

    def stok_menipis(self, batas=5):
        """Barang dengan stok <= batas."""
        return list(filter(lambda b: b.stok <= batas, self.daftar))

    @staticmethod
    def total_nilai(*barang):
        """*args: jumlah Barang bebas. assert memastikan tipe data."""
        assert all(isinstance(b, Barang) for b in barang), "harus objek Barang"
        return sum(map(lambda b: b.nilai_total(), barang))

    def buat_laporan(self, batas=5):
        """Susun teks laporan: daftar, total nilai, stok menipis."""
        baris = ["LAPORAN INVENTARIS TOKO", "=" * 30]
        for b in self.urutkan_harga(turun=True):
            baris.append(str(b))
        baris.append(f"Total nilai stok : Rp{self.total_nilai(*self.daftar)}")
        baris.append(f"Stok menipis (<= {batas}):")
        for b in self.stok_menipis(batas=batas):  # keyword argument
            baris.append(f"  - {b.nama} ({b.stok})")
        return "\n".join(baris)
