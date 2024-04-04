from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.hero, name='hero'),
    path('', views.contact, name='contact')
]