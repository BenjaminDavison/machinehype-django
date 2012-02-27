from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('hype.views',
    url(r'^$', 'index'),
    url(r'^(?P<song_id>\d+)/like/$', 'like'),
    url(r'^(?P<user_id>\d+)/user_songs/$', 'user_songs'),
    
    url(r'^popular_songs/$', 'popular_songs'),

)