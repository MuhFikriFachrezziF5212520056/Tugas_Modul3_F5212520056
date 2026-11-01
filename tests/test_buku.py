from unittest.mock import MagicMock
from models.buku_model import BukuModel

def test_create_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

    # Memanipulasi (Mock) koneksi database agar tidak mengotori data asli
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Melakukan eksekusi fungsi
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)

    # Memverifikasi apakah fungsi mengembalikan nilai True
    assert hasil is True
    # Memverifikasi apakah cursor.execute benar-benar dipanggil
    mock_cursor.execute.assert_called_once()
    # Memverifikasi apakah perintah commit (simpan) dipanggil
    model.conn.commit.assert_called_once()

# === Pengujian untuk fungsi get_all_buku() ===
def test_get_all_buku():
    # Inisialisasi Model
    model = BukuModel()

    # Mock koneksi database
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Simulasi data yang dikembalikan oleh kueri SELECT dari database
    mock_cursor.fetchall.return_value = [
        {'id_buku': 1, 'judul': 'Buku Testing', 'penulis': 'Penulis QA', 'tahun_terbit': 2026}
    ]

    # Eksekusi fungsi get_all_buku
    hasil = model.get_all_buku()

    # Memverifikasi hasil pengujian
    assert len(hasil) == 1
    assert hasil[0]['judul'] == 'Buku Testing'
    mock_cursor.execute.assert_called_once()
    mock_cursor.fetchall.assert_called_once()