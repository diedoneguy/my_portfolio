from django.db import models

# Create your models here.
class Port228(models.Model):
    title = models.CharField(max_length=250)
    about = models.CharField(max_length=2500)
    image = models.FileField(upload_to = 'port228/%Y/%m/%d/')
    def __str__(self) -> str:
        return self.title
