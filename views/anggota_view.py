import customtkinter as ctk
from tkinter import ttk

class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Manajemen Anggota")
        self.geometry("800x450")

        # ... (setting grid/frame kamu) ...
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Entry Input Anggota
        self.entry_nama = ctk.CTkEntry(self.frame_kiri, placeholder_text="Nama Anggota")
        self.entry_nama.pack(pady=5, padx=15, fill="x")

        self.entry_alamat = ctk.CTkEntry(self.frame_kiri, placeholder_text="Alamat")
        self.entry_alamat.pack(pady=5, padx=15, fill="x")

        # === TARUH TOMBOL DI SINI (DI DALAM __init__) ===
        self.btn_simpan = ctk.CTkButton(self.frame_kiri, text="Simpan Data", fg_color="green")
        self.btn_simpan.pack(pady=5, padx=15, fill="x")

        self.btn_update = ctk.CTkButton(self.frame_kiri, text="Update Data", fg_color="orange")
        self.btn_update.pack(pady=5, padx=15, fill="x")

        self.btn_delete = ctk.CTkButton(self.frame_kiri, text="Hapus Data", fg_color="red")
        self.btn_delete.pack(pady=5, padx=15, fill="x")

        # ... (setting frame kanan / tabel kamu) ...

if __name__ == "__main__":
    app = AnggotaView()
    app.mainloop()  # app.mainloop() HARUS TETAP DI PALING BAWAH