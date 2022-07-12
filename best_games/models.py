from distutils.command.upload import upload
from django.db import models

class Best_games(models.Model):
    title = models.CharField(max_length=250)
    text = models.CharField(max_length=250)
    image = models.FileField(upload_to = 'best_games/%Y/%m/%d/')
    def __str__(self) -> str:
        return self.title


