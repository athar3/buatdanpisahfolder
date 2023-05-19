import os
import shutil

# direktori folder utama
folder_utama = r"C:\Users\hp\Downloads\ASD-benar\ASD"

# daftar folder di folder utama
folders = [f.path for f in os.scandir(folder_utama) if f.is_dir()]

# buat folder "image" dan "label" di setiap subfolder
for folder in folders:
    subfolders = [f.path for f in os.scandir(folder) if f.is_dir()]
    for subfolder in subfolders:
        image_folder = os.path.join(subfolder, "image")
        label_folder = os.path.join(subfolder, "label")

        # buat folder "image" jika belum ada
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)
            print(f"Folder '{image_folder}' berhasil dibuat")

        # buat folder "label" jika belum ada
        if not os.path.exists(label_folder):
            os.makedirs(label_folder)
            print(f"Folder '{label_folder}' berhasil dibuat")

        # Memindahkan gambar ke folder "image"
        if os.path.exists(image_folder):
            image_files = [f.path for f in os.scandir(subfolder) if f.is_file() and f.name.endswith(".jpg")]
            for file in image_files:
                new_path = os.path.join(image_folder, os.path.basename(file))
                shutil.move(file, new_path)
                print(f"Gambar '{file}' berhasil dipindahkan ke '{new_path}'")

        # Memindahkan file .json ke folder "label"
        if os.path.exists(label_folder):
            json_files = [f.path for f in os.scandir(subfolder) if f.is_file() and f.name.endswith(".json")]
            for file in json_files:
                new_path = os.path.join(label_folder, os.path.basename(file))
                shutil.move(file, new_path)
                print(f"File '{file}' berhasil dipindahkan ke '{new_path}'")
        else:
            print(f"Folder 'label' tidak ditemukan di '{subfolder}'")
