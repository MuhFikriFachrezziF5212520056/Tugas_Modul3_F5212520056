import customtkinter as ctk
from tkinter import ttk

class BukuView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Manajemen Buku")
        self.geometry("800x450")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # FRAME KIRI: FORM BUKU
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kiri, text="Form Data Buku", font=("Arial", 16, "bold")).pack(pady=10)

        self.entry_judul = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Judul Buku")
        self.entry_judul.pack(pady=5, padx=15, fill="x")

        self.entry_penulis = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Nama Penulis")
        self.entry_penulis.pack(pady=5, padx=15, fill="x")

        self.entry_tahun = ctk.CTkEntry(self.frame_kiri, placeholder_text="Tahun Terbit")
        self.entry_tahun.pack(pady=5, padx=15, fill="x")

        # === PASTIKAN TIGA ATRIBUT TOMBOL INI ADA DI VIEW ===
        self.btn_simpan = ctk.CTkButton(self.frame_kiri, text="Simpan Data", fg_color="green")
        self.btn_simpan.pack(pady=5, padx=15, fill="x")

        self.btn_update = ctk.CTkButton(self.frame_kiri, text="Update Data", fg_color="orange")
        self.btn_update.pack(pady=5, padx=15, fill="x")

        self.btn_delete = ctk.CTkButton(self.frame_kiri, text="Hapus Data", fg_color="red")
        self.btn_delete.pack(pady=5, padx=15, fill="x")

        # Tambahkan baris ini di dalam method __init__ pada views/buku_view.py
        self.btn_logout = ctk.CTkButton(self.frame_kiri, text="Logout", fg_color="gray")
        self.btn_logout.pack(pady=10, padx=15, fill="x")

        # FRAME KANAN: TABEL BUKU
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kanan, text="Daftar Koleksi Buku", font=("Arial", 16, "bold")).pack(pady=10)

        kolom = ("id", "judul", "penulis", "tahun")
        self.tabel = ttk.Treeview(self.frame_kanan, columns=kolom, show="headings", height=15)

        self.tabel.heading("id", text="ID")
        self.tabel.heading("judul", text="Judul Buku")
        self.tabel.heading("penulis", text="Penulis")
        self.tabel.heading("tahun", text="Tahun")

        self.tabel.column("id", width=40, anchor="center")
        self.tabel.column("judul", width=150)
        self.tabel.column("penulis", width=120)
        self.tabel.column("tahun", width=60, anchor="center")

        self.tabel.pack(fill="both", expand=True, padx=15, pady=10)

if __name__ == "__main__":
    app = BukuView()
    app.mainloop()