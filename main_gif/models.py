from email.mime import image
from django.db import models

# Create your models here.
class Main_gif(models.Model):
    text = models.CharField(max_length=122)
    image = models.FileField(upload_to = 'main_gif/%Y/%m/%d/')
    def __str__(self) -> str:
        return self.text
        