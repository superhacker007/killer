import os
from PIL import Image

def compress_image(image_path, quality=85):
    """Compresses an image and overwrites the original file."""
    with Image.open(image_path) as img:
        img = img.convert('RGB')  # Ensure the image is in RGB mode
        img.save(image_path, 'JPEG', quality=quality)

def compress_images_in_folder(folder_path, quality=85, size_threshold_kb=100):
    """Compresses all images in the specified folder that are above the size threshold."""
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
            image_path = os.path.join(folder_path, filename)
            file_size_kb = os.path.getsize(image_path) / 1024  # Convert size to KB
            if file_size_kb > size_threshold_kb:
                compress_image(image_path, quality)
                print(f'Compressed: {filename} (Original size: {file_size_kb:.2f} KB)')

folder_path = 'static/pack/images/vc'  # Replace with your folder path
compress_images_in_folder(folder_path, quality=85, size_threshold_kb=100)
