from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    body = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='blog_images')

    def __str__(self):
        return self.title
    