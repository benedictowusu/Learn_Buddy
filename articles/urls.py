from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('list/', views.articles, name='list'),
    path("<slug:slug>/", views.article_detail, name='detail')
]