import email
from django.db import models


# Create your models here.


class News(models.Model):
    headline = models.CharField(max_length=200)
    image = models.ImageField(upload_to="movie/images/", null=True)
    body = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.headline
