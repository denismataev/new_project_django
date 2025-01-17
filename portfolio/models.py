from django.db import models

# Create your models here.

class indexPage(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
