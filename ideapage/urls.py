from django.conf.urls.defaults import *
urlpatterns = patterns('',
    url(r'^$', 'ideapage.views.home'),
    url(r'^logged_in/$','ideapage.views.logged_in'),
    url(r'^logged_in/out$','ideapage.views.out'),
    url(r'^logged_in/edit$','ideapage.views.edit'),
)
