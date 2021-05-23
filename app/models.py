from django.db import models
from django.contrib.auth.models import User

class NewsItem(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    headlines = models.CharField(max_length=80)
    news = models.TextField(max_length=500)
    published = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.headlines
