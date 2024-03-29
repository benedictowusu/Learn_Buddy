from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):

    class Courses(models.TextChoices):
        English = 'en', 'English',
        Maths = 'ma', 'Maths',
        History = 'hi', 'History',
        
    title = models.CharField(max_length = 255)
    category = models.CharField(max_length = 50, choices = Courses.choices, default = 1)
    slug = models.SlugField()
    body = models.TextField(null = True)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete = models.DO_NOTHING)
 
    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:50] + '...'