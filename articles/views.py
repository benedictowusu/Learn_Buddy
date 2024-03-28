from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def articles(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles.html', {'articles': articles})


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'details.html', {'article': article})