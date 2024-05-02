import os
import tkinter as tk
from tkinter import messagebox

# Fungsi untuk merename file
def rename_files(directory):
    try:
        # Mendapatkan daftar nama file dalam direktori
        files = os.listdir(directory)
        files.sort()  # Mengurutkan nama file secara alfanumerik (opsional)

        # Inisialisasi counter untuk nama baru
        counter = 1

        # Iterasi melalui setiap file
        for filename in files:
            # Mendapatkan path lengkap untuk setiap file
            old_path = os.path.join(directory, filename)

            # Membuat nama baru dengan counter
            new_filename = f"{counter}{os.path.splitext(filename)[1]}"
            new_path = os.path.join(directory, new_filename)

            # Melakukan rename file
            os.rename(old_path, new_path)

            # Meningkatkan counter
            counter += 1

        # Menampilkan pop-up window untuk memberi tahu pengguna bahwa proses berhasil
        messagebox.showinfo("Sukses", "Proses rename file berhasil!")
    except Exception as e:
        # Menampilkan pop-up window untuk memberi tahu pengguna bahwa proses gagal
        messagebox.showerror("Error", f"Proses rename file gagal: {str(e)}")

# Memanggil fungsi rename_files dengan directory yang sesuai
rename_files("hasil_resize")