from django.shortcuts import render
from articles.models import Article

# Create your views here.

def home(request):
    return render(request, 'hero.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        courses = Article.objects.filter(name_contains = searched)
        return render(request, 'search.html', {'searched': searched}, {'Article': courses})
    else:
        return render(request, 'search.html')