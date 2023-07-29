from django.db import models

class Text(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    text = models.TextField(null=True, blank=True)