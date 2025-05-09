from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField(label='Upload Image')
    
class ResizeImageForm(forms.Form):
    image = forms.ImageField(label='Upload Image')
    width = forms.IntegerField(label='Width (px)', min_value=1)
    height = forms.IntegerField(label='Height (px)', min_value=1)
    
class ConvertImageForm(forms.Form):
    image = forms.ImageField(label='Upload Image')
    format = forms.ChoiceField(label='Convert to', choices=[
        ('PNG', 'PNG'),
        ('JPEG', 'JPEG'),
        ('WEBP', 'WEBP'),
    ])