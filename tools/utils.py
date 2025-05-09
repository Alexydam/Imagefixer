import os
from io import BytesIO
from PIL import Image
from rembg import remove
from django.core.files.base import ContentFile

def remove_background(image):
    """Remove background from image using rembg"""
    input_image = Image.open(image)
    output_image = remove(input_image)
    
    # Save to BytesIO
    output_buffer = BytesIO()
    output_image.save(output_buffer, format='PNG')
    output_buffer.seek(0)
    
    name, ext = os.path.splitext(image.name)
    return ContentFile(output_buffer.read(), name=f'bg_removed_{name}.png')

def resize_image(image, width, height):
    """Resize image to specified dimensions"""
    img = Image.open(image)
    img = img.resize((width, height), Image.LANCZOS)
    
    output_buffer = BytesIO()
    img.save(output_buffer, format="PNG")
    output_buffer.seek(0)
    
    return ContentFile(output_buffer.read(), name=f'resized_{image.name}')

def convert_image_format(image, target_format):
    """Convert image to specified format"""
    img = Image.open(image)
    
    # Handle transparency for JPEG
    if target_format == 'JPEG' and img.mode in ('RGBA', 'LA'):
        background = Image.new(img.mode[:-1], img.size, (255, 255, 255))
        background.paste(img, img.split()[-1])
        img = background
    
    output_buffer = BytesIO()
    img.save(output_buffer, format=target_format)
    output_buffer.seek(0)
    
    new_name = f"{os.path.splitext(image.name)[0]}.{target_format.lower()}"
    return ContentFile(output_buffer.read(), name=new_name)
