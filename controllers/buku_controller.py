import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView

class BukuController:
    def __init__(self, user_role="anggota"):
        # === Menerima role pengguna saat login
        self.user_role = user_role
        
        # Inisialisasi Model dan View
        self.model = BukuModel()
        self.view = BukuView()

        # Menampilkan status mode role pada judul window
        self.view.title(f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}")

        # === Simpan ID buku yang sedang dipilih dari tabel
        self.selected_id = None
        
        # Binding (mengikat) tombol di View dengan fungsi di Controller
        self.view.btn_simpan.configure(command=self.simpan_data)
        
        # === Binding tombol Update dan Delete (jika ada di View)
        if hasattr(self.view, 'btn_update'):
            self.view.btn_update.configure(command=self.update_data)
        if hasattr(self.view, 'btn_delete'):
            self.view.btn_delete.configure(command=self.delete_data)

        # === Binding tombol Logout (jika ada di View)
        if hasattr(self.view, 'btn_logout'):
            self.view.btn_logout.configure(command=self.logout)
            
        # === Binding saat pengguna mengklik baris tabel
        self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_data_tabel)

        # === OTORISASI: Jika BUKAN Admin, Kunci Tombol Simpan, Update, Delete & Form Input ===
        if self.user_role != "admin":
            self.view.btn_simpan.configure(state="disabled", text="Akses Terkunci (Khusus Admin)")
            
            if hasattr(self.view, 'btn_update'):
                self.view.btn_update.configure(state="disabled")
            if hasattr(self.view, 'btn_delete'):
                self.view.btn_delete.configure(state="disabled")

            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")

        # Memuat data ke tabel saat aplikasi pertama kali dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Mengosongkan tabel di View terlebih dahulu
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)
        # Mengambil data dari Model (database)
        data_buku = self.model.get_all_buku()

        # Memasukkan data ke tabel di View
        for buku in data_buku:
            self.view.tabel.insert("", "end", values=(buku['id_buku'], buku['judul'], buku['penulis'], buku['tahun_terbit']))

    # === Fungsi untuk menangkap event klik tabel & mengisi otomatis form input
    def pilih_data_tabel(self, event):
        selected_item = self.view.tabel.selection()
        if selected_item:
            item_data = self.view.tabel.item(selected_item[0])['values']
            self.selected_id = item_data[0]  # Simpan id_buku dari kolom pertama

            # Hanya isi form jika mode admin (form tidak ter-disabled)
            if self.user_role == "admin":
                self.view.entry_judul.delete(0, 'end')
                self.view.entry_judul.insert(0, item_data[1])
                self.view.entry_penulis.delete(0, 'end')
                self.view.entry_penulis.insert(0, item_data[2])
                self.view.entry_tahun.delete(0, 'end')
                self.view.entry_tahun.insert(0, item_data[3])

    # === Fungsi pembantu untuk mengosongkan form & me-reset selected_id
    def bersihkan_form(self):
        self.selected_id = None
        if self.user_role == "admin":
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')

    def simpan_data(self):
        # Proteksi Otorisasi Controller
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menambah data!")
            return

        # Mengambil teks dari input di View
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        # Validasi Form Kosong
        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        # Mengirim data ke Model untuk disimpan
        berhasil = self.model.create_buku(judul, penulis, tahun)

        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")

    # === Fungsi Logika untuk Update Data Buku
    def update_data(self):
        # Proteksi Otorisasi Controller
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk memperbarui data!")
            return

        if not self.selected_id:
            messagebox.showwarning("Peringatan", "Pilih data buku dari tabel yang ingin diperbarui terlebih dahulu!")
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.update_buku(self.selected_id, judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal memperbarui data buku.")

    # === Fungsi Logika untuk Delete Data Buku
    def delete_data(self):
        # Proteksi Otorisasi Controller
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menghapus data!")
            return

        if not self.selected_id:
            messagebox.showwarning("Peringatan", "Pilih data buku dari tabel yang ingin dihapus terlebih dahulu!")
            return

        konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data ini?")
        if konfirmasi:
            if self.model.delete_buku(self.selected_id):
                messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
                self.bersihkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror("Error", "Gagal menghapus data buku.")

    # === [TUGAS 3] Fitur Logout (Menutup window utama & kembali ke LoginView)
    def logout(self):
        self.view.destroy()
        from controllers.auth_controller import AuthController
        app_login = AuthController()
        app_login.run()

    def run(self):
        self.view.mainloop()