from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

TYPE_GUITARE_CHOICES = [
    ['1', 'Classique'],
    ['2', 'Folk'],
    ['3', 'Flamenco'],
    ['4', 'Manouche'],
    ['5', 'Guitare à résonateur'],
    ['6', 'Hawaïenne'],
    ['7', 'Électro-acoustique'],
    ['8', 'Électrique']
]


class GuitareModel(models.Model):
    nom_guitare = models.CharField(max_length=150)
    type_guitare = models.CharField(choices=TYPE_GUITARE_CHOICES, max_length=150)
    description_guitare = models.TextField(null=True, blank=True)
    prix_guitare = models.PositiveIntegerField()
    photo_guitare = models.ImageField(verbose_name=None, upload_to='image_guitare')
    user_guitare = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_guitare
