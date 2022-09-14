from django.shortcuts import render
from .models import News
from django.shortcuts import get_object_or_404
from datetime import date

# for modal
from django.urls import reverse_lazy
from .models import News

# Create your views here.


def news(request):
    newss = News.objects.all().order_by("-date")
    today = date.today()
    return render(request, "news.html", {"newss": newss, "today": today})


def newsItem(request, news_id):
    news = get_object_or_404(News, pk=news_id)

    return render(request, "newsitem.html", {"news": news})
