from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Index(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    value = models.FloatField()

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

class Issue(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()