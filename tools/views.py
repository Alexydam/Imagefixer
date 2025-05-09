from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ImageUploadForm, ResizeImageForm, ConvertImageForm
from .utils import remove_background, resize_image, convert_image_format
from .models import ProcessedImage

def home(request):
    return render(request, 'tools/home.html')

def remove_bg(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            processed_image = ProcessedImage(
                original_image=form.cleaned_data['image'],
                operation='background_removal'
            )
            processed_image.processed_image = remove_background(form.cleaned_data['image'])
            processed_image.save()
            return render(request, 'tools/result.html', {
                'original': processed_image.original_image,
                'processed': processed_image.processed_image,
                'operation': 'Background Removal'
            })
    else:
        form = ImageUploadForm()
    
    return render(request, 'tools/remove_bg.html', {'form': form})

def resize(request):
    if request.method == 'POST':
        form = ResizeImageForm(request.POST, request.FILES)
        if form.is_valid():
            processed_image = ProcessedImage(
                original_image=form.cleaned_data['image'],
                operation=f'resize_{form.cleaned_data["width"]}x{form.cleaned_data["height"]}'
            )
            processed_image.processed_image = resize_image(
                form.cleaned_data['image'],
                form.cleaned_data['width'],
                form.cleaned_data['height']
            )
            processed_image.save()
            return render(request, 'tools/result.html', {
                'original': processed_image.original_image,
                'processed': processed_image.processed_image,
                'operation': 'Resize'
            })
    else:
        form = ResizeImageForm()
    
    return render(request, 'tools/resize.html', {'form': form})

def convert(request):
    if request.method == 'POST':
        form = ConvertImageForm(request.POST, request.FILES)
        if form.is_valid():
            processed_image = ProcessedImage(
                original_image=form.cleaned_data['image'],
                operation=f'convert_to_{form.cleaned_data["format"]}'
            )
            processed_image.processed_image = convert_image_format(
                form.cleaned_data['image'],
                form.cleaned_data['format']
            )
            processed_image.save()
            return render(request, 'tools/result.html', {
                'original': processed_image.original_image,
                'processed': processed_image.processed_image,
                'operation': 'Format Conversion'
            })
    else:
        form = ConvertImageForm()
    
    return render(request, 'tools/convert.html', {'form': form})