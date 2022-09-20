import email
from email.message import EmailMessage
from django.forms import ModelForm, Textarea
from .models import Review, ProfReview, Reviewer_requests


class ReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields["text"].widget.attrs.update({"class": "form-control"})
        self.fields["watchAgain"].widget.attrs.update({"class": "form-check-input"})

    class Meta:
        model = Review
        fields = ["text", "watchAgain"]
        labels = {"watchAgain": ("Watch Again")}
        widgets = {
            "text": Textarea(attrs={"rows": 4}),
        }


class profReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields["text"].widget.attrs.update({"class": "form-control"})
        self.fields["watchAgain"].widget.attrs.update({"class": "form-check-input"})

    class Meta:
        model = ProfReview
        fields = ["text", "watchAgain"]
        labels = {"watchAgain": ("Watch Again")}
        widgets = {
            "text": Textarea(attrs={"rows": 8}),
        }


class becomeredreviewerform(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control"})
        self.fields["email"].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = Reviewer_requests
        fields = ["name", "email"]
        widgets = {
            "text": Textarea(attrs={"rows": 4}),
            "email": Textarea(attrs={"rows": 1}),
        }
