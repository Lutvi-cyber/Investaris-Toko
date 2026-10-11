"""Modul testing: unit test dengan library unittest."""
import unittest
from .validasi import parse_baris, DataTidakValidError
from .processing import Barang, Inventaris


class TestToko(unittest.TestCase):
    def setUp(self):
        self.inv = Inventaris([Barang("A1", "Buku", 5000, 10),
                               Barang("A2", "Pena", 2000, 3)])

    def test_nilai_total(self):
        self.assertEqual(self.inv.daftar[0].nilai_total(), 50000)

    def test_total_nilai_args(self):
        self.assertEqual(Inventaris.total_nilai(*self.inv.daftar), 56000)

    def test_urut_harga(self):
        self.assertEqual(self.inv.urutkan_harga()[0].kode, "A2")

    def test_stok_menipis(self):
        self.assertEqual(len(self.inv.stok_menipis(batas=5)), 1)

    def test_cari(self):
        self.assertEqual(self.inv.cari("pen")[0].kode, "A2")

    def test_parse_valid(self):
        self.assertEqual(parse_baris("B1;Tas;100;2;X")["stok"], 2)

    def test_parse_harga_bukan_angka(self):
        with self.assertRaises(DataTidakValidError):
            parse_baris("B1;Tas;abc;2;X")

    def test_parse_negatif(self):
        with self.assertRaises(DataTidakValidError):
            parse_baris("B1;Tas;-5;2;X")

    def test_kwargs(self):
        b = Barang("C1", "Mouse", 90000, 1, merek="Logi")
        self.assertEqual(b.atribut["merek"], "Logi")


if __name__ == "__main__":
    unittest.main()
