from django import forms
from .models import About, Review, Event, PortfolioItem

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        exclude=['about_id']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude=['about_id']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude=['about_id']

class PortfolioItemForm(forms.ModelForm):
    class Meta:
        model = PortfolioItem
        exclude=['about_id']
    


