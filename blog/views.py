#-*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.shortcuts import redirect

def home(request):
  text="""<h1>hello world</h1>
<p>la première phrase de mon site.</p>"""
  return HttpResponse(text)

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