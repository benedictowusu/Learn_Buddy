from django.urls import URLPattern, path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard')
]