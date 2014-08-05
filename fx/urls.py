from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Examples:
    # url(r'^$', 'fx.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','fx_app.views.home', name='home'),

    # url(r'^all_articles/$', 'fx_app.views.all_articles', name='all_articles'),

    url(r'^tweets/$','fx_app.views.tweets', name='tweets'),

    # url(r'^return_tweets_py/$','fx_app.views.return_tweets_py', name='tweets_py'),
)
