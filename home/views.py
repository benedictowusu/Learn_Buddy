from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'hero.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def search(request):
    return render(request, 'search.html')
