
from django.db import models


opcion_query = [
    [0, 'consulta'],
    [1,'reclamo'],
    [2, 'reseña'],

]
class Contact(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono=models.CharField(max_length=30,null=True, blank=True)
    tipo_de_consulta = models.IntegerField(choices=opcion_query,null=True, blank=True)
    comentario = models.TextField()
    notificaciones = models.BooleanField()

    def __str__(self):
        return self.nombre