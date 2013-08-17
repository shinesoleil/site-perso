#-*- coding: utf-8 -*-
from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=50)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False,
verbose_name="Date de parution")

#def __unicode__(self):
#  return u"%s" % self.titre
