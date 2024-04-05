from PIL import Image
import os

def resize_image(input_path, output_path, target_size_kb, format='JPEG'):
    # Buka gambar
    img = Image.open(input_path)
    
    # Hitung faktor resize untuk mencapai target size
    target_size_bytes = target_size_kb * 1024
    current_size_bytes = os.path.getsize(input_path)
    resize_factor = (target_size_bytes / current_size_bytes) ** 0.5
    
    # Resize gambar
    width, height = img.size
    new_width = int(width * resize_factor)
    new_height = int(height * resize_factor)
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    
    # Simpan gambar dengan kualitas kompresi yang tinggi
    img.save(output_path, format=format, quality=95)

# Path ke folder gambar input dan output
input_image_folder = "gambar"
output_image_folder = "hasil_resize"
target_size_kb = 100

# Pastikan folder output ada
if not os.path.exists(output_image_folder):
    os.makedirs(output_image_folder)

# Loop melalui semua file dalam folder gambar
for filename in os.listdir(input_image_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        input_image_path = os.path.join(input_image_folder, filename)
        output_image_path = os.path.join(output_image_folder, filename)
        # Panggil fungsi resize_image
        resize_image(input_image_path, output_image_path, target_size_kb)
