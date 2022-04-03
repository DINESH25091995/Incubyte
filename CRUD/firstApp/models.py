from django.db import models

# Create your models here.
class Content(models.Model):
    id=models.IntegerField(primary_key=True)
    word=models.CharField(max_length=254)
