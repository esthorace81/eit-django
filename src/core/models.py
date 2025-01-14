from django.db import models


class Cliente(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)

    # def __str__(self) -> str:
    #     return f"{self.apellidos}, {self.nombres}"
