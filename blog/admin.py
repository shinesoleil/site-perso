from django.contrib import admin
from blog.models import Article, Categorie

admin.site.register(Categorie)
admin.site.register(Article)