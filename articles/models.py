from django.db import models
from embed_video.fields import EmbedVideoField

class Article(models.Model):

    #Giving selection options for the writer
    class specialization(models.TextChoices):
        Front_end = 'FrontEnd', 'FrontEnd Development',
        Backend = 'Backend', 'Backend Development',
        
    title = models.CharField(max_length = 255)
    category = models.CharField(max_length = 50, choices = specialization.choices, default = 1)
    slug = models.SlugField(null= True)
    snippet = models.TextField(null=True, default=None)
    image = models.ImageField(default=None, blank=True)
    url = EmbedVideoField(null=True, default=None)
 
    def __str__(self):
        return self.title + " " + " a " + self.category + " course "