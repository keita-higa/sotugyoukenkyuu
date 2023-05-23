from django.db import models

# Create your models here.

class SotukenConfig(models.Model):

    sotu1 = models.CharField(max_length=100)
    sotu2 = models.IntegerField()

    