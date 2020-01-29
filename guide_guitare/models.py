from django.db import models

class GuitareModel(models.Model):
    nom_guitare = models.CharField(max_length=150)
    type_guitare = models.CharField(max_length=150)
    description_guitare = models.TextField(null=True)
    prix_guitare = models.PositiveIntegerField()
    photo_guitare = models.ImageField(verbose_name=None)
