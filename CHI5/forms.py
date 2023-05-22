from django import forms
from .models import AptitudeTestData

class AptitudeTestForm(forms.ModelForm):
    class Meta:
        model = AptitudeTestData
        fields = ['name', 'age', 'personality', 'intellectual_aptitude', 'love_connection', 'esteem_social_contribution', 'intellectual_interest', 'simple_pleasures', 'physical_engagement']