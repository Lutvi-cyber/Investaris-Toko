"""File utama: menjalankan seluruh alur program."""
import unittest
from toko import fileio, testing
from toko.processing import Inventaris

DATA_AWAL = ("B001;Buku Tulis;5000;20;ATK\n"
             "B002;Pensil;2000;4;ATK\n"
             "B003;Penggaris;3500;8;ATK\n"
             "B004;Pulpen;abc;10;ATK\n")  # baris rusak (sengaja)

FILE_DATA, FILE_LAPORAN = "barang.txt", "laporan.txt"


def main():
    fileio.buat_file(FILE_DATA, DATA_AWAL)                        # mode x
    fileio.tambah_barang(FILE_DATA, "B005;Stabilo;7500;3;ATK")    # mode a
    inv = Inventaris(fileio.baca_barang(FILE_DATA))               # mode r
    laporan = inv.buat_laporan(batas=5)
    fileio.tulis_laporan(FILE_LAPORAN, laporan)                   # mode w
    print(laporan)
    print("\n--- Pengujian unittest ---")
    unittest.main(module=testing, argv=["x"], exit=False)         # uji global


if __name__ == "__main__":
    main()
