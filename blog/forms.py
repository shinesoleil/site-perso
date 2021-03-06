#-*- coding: utf-8 -*-
from django import forms

class ConnexionForm(forms.Form):
    username=forms.CharField(label="Nom d'utilisateur",max_length=30)
    password=forms.CharField(label="Mot de passe",widget=forms.PasswordInput)

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label=u"Votre adresse mail")
    renvoi = forms.BooleanField(help_text=u"Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)