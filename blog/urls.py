from django.conf.urls import patterns,url
from django.views.generic import TemplateView 

urlpatterns = patterns('',
    url(r'^home/',
TemplateView.as_view(template_name='blog/home.html')),
    url(r'^log/',
TemplateView.as_view(template_name='blog/logged.html')),
    url(r'^labo/',
TemplateView.as_view(template_name='blog/labo_timecounter.html')),
    url(r'^connexion/$','blog.views.connexion',name='connexion'),
    url(r'^deconnexion/$','blog.views.connexion',name='deconnexion'),
)