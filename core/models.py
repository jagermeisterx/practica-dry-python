from django.db import models


class Mensaje(models.Model):
    nombre = models.CharField("Nombre", max_length=80)
    email = models.EmailField("Correo electrónico")
    asunto = models.CharField("Asunto", max_length=120)
    contenido = models.TextField("Mensaje")
    creado = models.DateTimeField("Fecha de envío", auto_now_add=True)

    class Meta:
        ordering = ["-creado"]

    def __str__(self):
        return f"{self.asunto} — {self.nombre}"