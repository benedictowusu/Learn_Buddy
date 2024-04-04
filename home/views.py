from django.shortcuts import render

# Create your views here.
def hero(request):
    return render(request, 'hero.html')

def contact(request):
    return render(request, 'contact.html')