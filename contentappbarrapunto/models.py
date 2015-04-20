from django.db import models

class Put_App(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
