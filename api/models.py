from django.db import models

# Create your models here.
class Label(models.Model):
    labelName = models.CharField(max_length=100, unique=True)
    labelColor = models.CharField(max_length=20)



    def __str__(self):
        return self.name