from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.usuario.username