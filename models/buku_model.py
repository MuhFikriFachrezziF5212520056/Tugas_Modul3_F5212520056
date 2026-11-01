from config.database import Database

class BukuModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "buku"

    def get_all_buku(self):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            query = f"SELECT * FROM {self.table_name}"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        return []

    def create_buku(self, judul, penulis, tahun_terbit):
        if self.conn:
            cursor = self.conn.cursor()
            query = f"INSERT INTO {self.table_name} (judul, penulis, tahun_terbit) VALUES (%s, %s, %s)"
            val = (judul, penulis, tahun_terbit)
            cursor.execute(query, val)
            self.conn.commit()
            cursor.close()
            return True
        return False
     
    # --- TAMBAHAN UNTUK TUGAS 4 ---
    def update_buku(self, id_buku, judul, penulis, tahun_terbit):
        if self.conn:
            cursor = self.conn.cursor()
            query = f"UPDATE {self.table_name} SET judul = %s, penulis = %s, tahun_terbit = %s WHERE id_buku = %s"
            val = (judul, penulis, tahun_terbit, id_buku)
            cursor.execute(query, val)
            self.conn.commit()
            cursor.close()
            return True
        return False

    def delete_buku(self, id_buku):
        try:
            cursor = self.conn.cursor()

            # 1. Matikan pengecekan FK sementara
            cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")

            # 2. Hapus data buku
            query = "DELETE FROM buku WHERE id_buku = %s"
            cursor.execute(query, (id_buku,))

            # 3. Aktifkan kembali pengecekan FK
            cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")

            self.conn.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error saat menghapus data: {e}")
            self.conn.rollback()
            return False