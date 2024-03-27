from django.shortcuts import render
from .models import Article

def articles(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles.html', {'articles': articles})
