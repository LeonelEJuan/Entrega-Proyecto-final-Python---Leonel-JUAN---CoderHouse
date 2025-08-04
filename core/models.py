from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Usuario personalizado (CEO, Reclutadores, etc.)
class CustomUser(AbstractUser):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

# Modelo para las páginas del blog
class Page(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pages/')
    date = models.DateTimeField(auto_now_add=True)  # ← Aquí el cambio

    def __str__(self):
        return self.title

# Solicitud de reclutamiento
class RecruitmentRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    experience_years = models.IntegerField()
    modality = models.CharField(
        max_length=20,
        choices=[
            ('remoto', 'Remoto'),
            ('presencial', 'Presencial'),
            ('híbrido', 'Híbrido')
        ]
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.role} ({self.user.username})'

