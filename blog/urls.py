from django.conf.urls import patterns,url

urlpatterns = patterns('blog.views',
    url(r'^accueil/$','home'),
    url(r'^accueil/(\d+)/$','view_article'),
    url(r'^accueil/(?P<year>\d{4})/(?P<month>\d{2})/$','list_articles'),
)