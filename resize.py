import os
import shutil
from PIL import Image

# Menentukan folder sumber dan tujuan
folder_sumber = [r'D:\CAPSTONE\sapi\test\pinkeye', r'D:\CAPSTONE\sapi\test\sehat', r'D:\CAPSTONE\sapi\train\pinkeye', r'D:\CAPSTONE\sapi\train\sehat']
folder_tujuan = [r'D:\CAPSTONE\sapires\test\pinkeye', r'D:\CAPSTONE\sapires\test\sehat', r'D:\CAPSTONE\sapires\train\pinkeye', r'D:\CAPSTONE\sapires\train\sehat']

# Membuat folder tujuan jika belum ada
for folder in folder_tujuan:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Melakukan reshape pada setiap folder sumber
for i in range(len(folder_sumber)):
    sumber = folder_sumber[i]
    tujuan = folder_tujuan[i]

    # Mengambil daftar file di folder sumber
    file_list = os.listdir(sumber)

    # Melakukan reshape dan menyimpan ke folder tujuan
    for file_name in file_list:
        file_path_sumber = os.path.join(sumber, file_name)
        file_path_tujuan = os.path.join(tujuan, file_name)

        # Membuka gambar menggunakan PIL
        img = Image.open(file_path_sumber)

        # Melakukan resize ke ukuran 640x640 piksel
        resized_img = img.resize((640, 640))

        # Menyimpan gambar ke folder tujuan
        resized_img.save(file_path_tujuan)

print("Reshape dan penyalinan selesai!")
