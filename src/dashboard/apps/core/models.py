from django.db import models

# Create your models here.
class Configuration(models.Model):
    github_tokem = models.CharField(max_length=200)
    repository = models.CharField(max_length=200)