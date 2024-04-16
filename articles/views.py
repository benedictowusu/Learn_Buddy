from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from . import forms

def articles(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})

@login_required
def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'details.html', {'article': article})