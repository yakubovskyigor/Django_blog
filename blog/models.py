from django.conf import settings
from django.db import models


class Post(models.Model):
    article_number = models.IntegerField()
    title_translit = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    summary = models.CharField(max_length=250)
    text = models.TextField()
    views = models.IntegerField()
    favorites = models.BooleanField(True, False)
    mark = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.title