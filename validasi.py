"""Modul validasi: memeriksa data sebelum dipakai."""


class DataTidakValidError(Exception):
    """Exception buatan sendiri untuk data yang tidak valid."""


def parse_baris(baris):
    """Ubah satu baris 'kode;nama;harga;stok;kategori' menjadi dict.

    Alur: pecah -> cek jumlah field -> cek kosong -> konversi angka -> cek negatif.
    """
    bagian = baris.strip().split(";")
    if len(bagian) != 5:
        raise DataTidakValidError("jumlah field harus 5")  # raise buatan sendiri
    kode, nama, harga, stok, kategori = bagian
    if not kode or not nama:
        raise DataTidakValidError("kode/nama tidak boleh kosong")
    try:
        harga, stok = int(harga), int(stok)  # ValueError jika bukan angka
    except ValueError:
        raise DataTidakValidError("harga/stok harus angka") from None
    if harga < 0 or stok < 0:
        raise DataTidakValidError("harga/stok tidak boleh negatif")
    return {"kode": kode, "nama": nama, "harga": harga,
            "stok": stok, "kategori": kategori}


if __name__ == "__main__":  # pengujian lokal modul ini
    assert parse_baris("B001;Buku;5000;10;ATK")["harga"] == 5000
    try:
        parse_baris("B002;Pena;abc;3;ATK")
    except DataTidakValidError as e:
        print("OK, error tertangkap:", e)
