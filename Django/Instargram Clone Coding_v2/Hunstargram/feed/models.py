from django.db import models


# Create your models here.
class Feed(models.Model):
    profile_image = models.TextField()
    user_name = models.TextField()
    content_image = models.TextField()
    like_count = models.IntegerField()
    content = models.TextField()
