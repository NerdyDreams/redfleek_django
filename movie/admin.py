from django.contrib import admin

# Register your models here.

# add movie model to admin interface
from .models import Movie, Review

admin.site.register(Movie)
admin.site.register(Review)
