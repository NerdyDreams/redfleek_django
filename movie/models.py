from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="movie/images/")
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watchAgain = models.BooleanField()

    def __str__(self):
        return self.text


class ProfReview(models.Model):
    text = models.TextField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watchAgain = models.BooleanField()

    # def save(self, *args, **kwargs):
    #     if not self.pk and ProfReview.objects.exists():
    #         # if you'll not check for self.pk
    #         # then error will also raised in update of exists model
    #         raise ValidationError("There can be only one RedReview")
    #     return super(ProfReview, self).save(*args, **kwargs)
