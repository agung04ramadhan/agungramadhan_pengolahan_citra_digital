from PIL import Image

def encrypt_image(image_path, key):
    # Buka gambar
    image = Image.open(image_path)
    # Konversi gambar ke mode RGB
    image = image.convert("RGB")
    
    width, height = image.size
    
    # Membangun matriks piksel baru untuk gambar terenkripsi
    hiden_image = Image.new("RGB", (width, height))
    
    for y in range(height):
        for x in range(width):
            # Dapatkan piksel RGB pada posisi (x, y)
            r, g, b = image.getpixel((x, y))
            
            # Enkripsi piksel dengan kunci
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            
            # Set piksel terenkripsi pada gambar baru
            hiden_image.putpixel((x, y), (r, g, b))
    
    # Simpan gambar terenkripsi
    hiden_image.save("hiden_image.png")
    print("Gambar berhasil dienkripsi.")


def decrypt_image(image_path, key):
    # Buka gambar terenkripsi
    hiden_image = Image.open(image_path)
    # Konversi gambar ke mode RGB
    hiden_image = hiden_image.convert("RGB")
    
    width, height = hiden_image.size
    
    # Membangun matriks piksel baru untuk gambar terdekripsi
    original_image = Image.new("RGB", (width, height))
    
    for y in range(height):
        for x in range(width):
            # Dapatkan piksel RGB pada posisi (x, y)
            r, g, b = hiden_image.getpixel((x, y))
            
            # Dekripsi piksel dengan kunci
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            
            # Set piksel terdekripsi pada gambar baru
            original_image.putpixel((x, y), (r, g, b))
    
    # Simpan gambar terdekripsi
    original_image.save("original_image.png")
    print("Gambar berhasil didekripsi.")


# Contoh penggunaan
image_path = "luffy.jpg"
key = 42

encrypt_image(image_path, key)

decrypt_image("hiden_image.png", key)