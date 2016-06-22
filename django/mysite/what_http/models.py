from django.db import models

class AskedUrl(models.Model):
    url = models.CharField(max_length=100)
