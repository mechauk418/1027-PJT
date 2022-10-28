from ctypes import resize
from lib2to3.pgen2.grammar import opmap_raw
from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.

class Article(models.Model):

    title = models.CharField(max_length=80)
    content = models.TextField()
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(1200, 960)],
        format="JPEG",
        options={"quality": 90},
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    grade = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_article"
    )


class Comment(models.Model):

    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
