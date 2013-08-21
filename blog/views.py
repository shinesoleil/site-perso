#-*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.shortcuts import render
from datetime import datetime
from blog.forms import ContactForm,ConnexionForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

def connexion(request):
  error = False
  
  if request.method == "POST":
    form = ConnexionForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data["username"] 
      password = form.cleaned_data["password"]
      user = authenticate(username=username,
password=password) 
      if user: # Si l'objet renvoyé n'est pas None
        login(request, user) # nous connectons l'utilisateur
      else: 
        error = True
      return render(request, 'blog/logged.html',locals())
  else:
    form = ConnexionForm()
    return render(request, 'blog/connexion.html',locals())

def deconnexion(request):
  logout(request)
  return redirect(reverse(connexion))

def contact(request):
  if request.method == 'POST': # S'il s'agit d'une requête POST
    form = ContactForm(request.POST) # Nous reprenons les données
    if form.is_valid(): # Nous vérifions que les données envoyées sont valides
      # Ici nous pouvons traiter les données du formulaire
      sujet = form.cleaned_data['sujet']
      message = form.cleaned_data['message']
      envoyeur = form.cleaned_data['envoyeur']
      renvoi = form.cleaned_data['renvoi']
      # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer
      envoi = True

  else: # Si ce n'est pas du POST, c'est probablement une requête GET
    form = ContactForm()  # Nous créons un formulaire vide
  
  return render(request, 'blog/contact.html', locals())


def home(request):
  text="""<h1>hello world</h1>
<p>la première phrase de mon site.</p>"""
  return HttpResponse(text)

def tpl(request):
  return render(request, 'blog/tpl.html',{'current_date':
datetime.now()})

def view_article(request, id_article):
  """ Vue qui affiche un article selon son identifiant 
(ou ID,ici un numéro). Son ID est le second paramètre de 
la fonction(pour rappel, le premier paramètre est TOUJOURS la requête de
l'utilisateur) """
  text = "Vous avez demandé l'article n°{} !".format(id_article)
  #return redirect("http://www.sina.com")
  return HttpResponse(text)

def list_articles(request, month, year):
  """ Liste des articles d'un mois précis. """
  #if int(year)<2000:
  #  raise Http404
  text = "Vous avez demandé les articles de {1}{0}.".format(month, year)
  return HttpResponse(text)