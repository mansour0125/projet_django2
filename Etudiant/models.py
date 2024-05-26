from django.db import models

# Create your models here.

class Apprenant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    email = models.EmailField()
    numero_identification = models.CharField(max_length=100, unique=True)
    filiere_choise = [
        ('ABD','ABD'),
        ('APD','APD'),
        ('BDE','BDE'),
        ('DFE','DFE'),
        ('RSiot','RSiot'),
        ('SSC','SSC'),   
    ]
    filiere = models.CharField(max_length=100, choices=filiere_choise)