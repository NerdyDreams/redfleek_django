from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Review, ProfReview
from django.shortcuts import get_object_or_404, redirect
from .forms import ReviewForm, profReviewForm, becomeredreviewerform
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.core.exceptions import ValidationError

# Create your views here.


def home(request):
    searchTerm = request.GET.get("searchMovie")
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, "home.html", {"searchTerm": searchTerm, "movies": movies})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def signup(request):
    email = request.GET.get("email")
    return render(request, "signup.html", {"email": email})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = Review.objects.filter(movie=movie)
    return render(request, "detail.html", {"movie": movie, "reviews": reviews})


@login_required
def createreview(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == "GET":
        return render(
            request, "createreview.html", {"form": ReviewForm(), "movie": movie}
        )
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.movie = movie
            newReview.save()
            return redirect("detail", newReview.movie.id)
        except ValueError:
            return render(
                request,
                "createreview.html",
                {"form": ReviewForm(), "error": "bad data passed in"},
            )


@login_required
def updatereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == "GET":
        form = ReviewForm(instance=review)
        return render(request, "updatereview.html", {"review": review, "form": form})
    else:
        try:
            form = ReviewForm(
                request.POST, instance=review
            )  # populates previous reviews
            form.save()
            return redirect("detail", review.movie.id)
        except ValueError:
            return render(
                request,
                "updatereview.html",
                {"review": review, "form": form, "error": "Bad data in form"},
            )


@login_required
def deletereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect("detail", review.movie.id)


# PROFESSIONAL REVIEWS
def profreview(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    profreview = ProfReview.objects.get(pk=movie_id)
    return render(
        request, "profreview.html", {"movie": movie, "profreview": profreview}
    )


@staff_member_required
def createprofreview(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    args = {}

    if request.method == "GET":
        return render(
            request, "createprofreview.html", {"form": ReviewForm(), "movie": movie}
        )
    else:
        try:
            form = profReviewForm(request.POST)
            newProfReview = form.save(commit=False)
            newProfReview.user = request.user
            newProfReview.movie = movie
            if form.is_valid() and not ProfReview.objects.exists():
                newProfReview.save()
                return redirect("profreview", newProfReview.movie.id)
            else:
                form = profReviewForm()
            args["form"] = form
            return render(
                request,
                "createprofreview.html",
                {"error": "A RedReview already exists for this film"},
            )
        except ValueError or ValidationError:
            if ValueError:
                return render(
                    request,
                    "createprofreview.html",
                    {"form": profReviewForm(), "error": "bad data passed in"},
                )


@login_required
def updateprofreview(request, profreview_id):
    profreview = get_object_or_404(ProfReview, pk=profreview_id, user=request.user)
    if request.method == "GET":
        form = profReviewForm(instance=profreview)
        return render(
            request, "updateprofreview.html", {"review": profreview, "form": form}
        )
    else:
        try:
            form = ReviewForm(
                request.POST, instance=profreview
            )  # populates previous reviews
            form.save()
            return redirect("detail", profreview.movie.id)
        except ValueError:
            return render(
                request,
                "updateprofreview.html",
                {"review": profreview, "form": form, "error": "Bad data in form"},
            )


@login_required
def deleteprofreview(request, profreview_id):
    profreview = get_object_or_404(ProfReview, pk=profreview_id, user=request.user)
    profreview.delete()
    return redirect("detail", profreview.movie.id)


def becomeredreviewer(request):
    if request.method == "GET":
        return render(
            request, "becomeredreviewerform.html", {"form": becomeredreviewerform()}
        )
    else:
        try:
            form = becomeredreviewerform(request.POST)
            data = request.POST.get("name")
            form.save(commit=True)
            return render(request, "becomeredreviewerthanks.html", {"name": data})
            # if "var_name" in request.POST:
            #     # context is the name of dict that we gonna pass to our template
            #     #'var_name' derives from the template
            #     context["name"] = request.POST["var_name"]
        except ValueError:
            return render(
                request,
                "becomeredreviewerform.html",
                {"form": becomeredreviewerform(), "error": "bad data passed in"},
            )


# def becomeredreviewer(request):
#     # context = {}
