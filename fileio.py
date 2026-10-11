"""Modul fileio: semua operasi baca/tulis file (selalu with open)."""
from .validasi import parse_baris, DataTidakValidError
from .processing import Barang


def buat_file(path, isi_awal):
    """Mode 'x': buat file pertama kali, tidak menimpa file yang ada."""
    try:
        with open(path, "x", encoding="utf-8") as f:
            f.write(isi_awal)
        print(f"File {path} dibuat.")
    except FileExistsError:
        print(f"File {path} sudah ada, tidak ditimpa.")


def tambah_barang(path, record):
    """Mode 'a': tambah data baru di akhir tanpa menghapus data lama."""
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{record}\n")


def baca_barang(path):
    """Mode 'r' iteratif; baris rusak dilewati, program tetap jalan."""
    hasil = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for no, baris in enumerate(f, start=1):
                if not baris.strip():
                    continue
                try:
                    hasil.append(Barang(**parse_baris(baris)))
                except DataTidakValidError as e:
                    print(f"Baris {no} dilewati: {e}")
    except FileNotFoundError:
        print(f"Error: file {path} belum ada. Buat file data terlebih dahulu.")
    return hasil


def tulis_laporan(path, teks):
    """Mode 'w': tulis laporan (dibuat ulang setiap dijalankan)."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(teks)
