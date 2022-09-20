from django.urls import path
from . import views

urlpatterns = [
    path("<int:movie_id>", views.detail, name="detail"),
    path("<int:movie_id>/create", views.createreview, name="createreview"),
    path("review/<int:review_id>", views.updatereview, name="updatereview"),
    path("review/<int:review_id>/delete", views.deletereview, name="deletereview"),
    path("<int:movie_id>/profreview", views.profreview, name="profreview"),
    path(
        "<int:movie_id>/createprofreview",
        views.createprofreview,
        name="createprofreview",
    ),
    path(
        "profreview/<int:profreview_id>",
        views.updateprofreview,
        name="updateprofreview",
    ),
    path(
        "profreview/<int:profreview_id>/delete",
        views.deleteprofreview,
        name="deleteprofreview",
    ),
    path(
        "becomeredreviewerform",
        views.becomeredreviewer,
        name="becomeredreviewer",
    ),
    #  path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')))
]
