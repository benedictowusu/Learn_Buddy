from django.urls import path
from .views import articles, article_detail

app_name = 'articles'

urlpatterns = [
    path('', articles, name='list'),
    path("<slug:slug>/", article_detail, name='detail')
]