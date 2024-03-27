from django.urls import URLPattern, path
from .views import home

app_name = 'dashboard'

urlpatterns = [
    path('', home, name='dashboard')
]