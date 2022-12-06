from django.db import models

# Create your models here.
class Feed(models.Model):
    location = models.TextField()
    image = models.TextField()
    click = models.TextField()
    conv = models.TextField()