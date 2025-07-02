from django.db import models

class Proyecto (models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    miniatura = models.ImageField(upload_to='portfolio/thumbnail/')
    imagen_completa = models.ImageField(upload_to='portfolio/fullsize/')

    def __str__(self):
        return self.nombre