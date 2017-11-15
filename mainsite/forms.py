from django import forms
from .models import *
from django.forms import ModelForm

class ContactMessageForm(ModelForm):
    class Meta:
        model= ContactMessage
        fields= ['nom', 'contenu']
        labels = {
        'nom': 'Nom ou n° de téléphone',
        'contenu': 'Votre message',
    }