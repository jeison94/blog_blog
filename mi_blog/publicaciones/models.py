from django.db import models
class Post(models.model):
    titulo = models.CharField(max_length=200) 
    contenido = models.TextField()
    fecha_publicacion = models.DateField()
    categoria = models.CharField(max_length=100)


    def __str__(self):
        return self.titulo

# Create your models here.
