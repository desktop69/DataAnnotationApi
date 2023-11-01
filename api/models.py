from django.db import models

# Create your models here.
class Label(models.Model):
    labelName = models.CharField(max_length=100, unique=True)
    labelColor = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Annotation(models.Model):
    start = models.IntegerField()
    end = models.IntegerField()
    label = models.CharField(max_length=100)
    text = models.TextField()

class Document(models.Model):
    content = models.TextField()
    annotations = models.ManyToManyField(Annotation)
    
    def __str__(self):
        return self.name