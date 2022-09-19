from django.contrib import admin

# Register your models here.

# add movie model to admin interface
from .models import Movie, Review, ProfReview, Reviewer_requests

admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(ProfReview)
admin.site.register(Reviewer_requests)
