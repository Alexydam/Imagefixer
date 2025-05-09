from django.urls import path
from . import views

app_name = 'tools'

urlpatterns = [
    path('', views.home, name='home'),
    path('remove-bg/', views.remove_bg, name='remove_bg'),
    path('resize/', views.resize, name='resize'),
    path('convert/', views.convert, name='convert'),
]