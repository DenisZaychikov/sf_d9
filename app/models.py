from django.db import models
from django.utils import timezone


class Category(models.Model):
    categoty_title = models.CharField(max_length=255)
    url = models.SlugField()


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    status = models.CharField(max_length=10, choices=[('D', 'draft'), ('P', 'published')])
    content = models.TextField()
    updated = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
