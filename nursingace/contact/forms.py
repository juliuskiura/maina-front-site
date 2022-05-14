
from django import forms
from .models import ModelContact, Subscriber


class ModelContactForm(forms.ModelForm):
    class Meta:
        model = ModelContact
        fields = '__all__'
        exclude = ('date_added',)


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email',)
     