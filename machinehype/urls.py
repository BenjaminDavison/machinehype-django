# This also imports the include function
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
from machinehype.hype.forms import ProfileForm

admin.autodiscover()

#from machinehype.hype.forms import ProfileForm
#    ('^profiles/edit', 'profiles.views.edit_profile', {'form_class': ProfileForm,}),
#    (r'^profiles/', include('profiles.urls')),
#    
#from machinehype.hype.forms import ProfileForm
#    ('^profiles/edit', 'profiles.views.edit_profile', {'form_class': ProfileForm,'success_url':'/my/custom/url',}),
#    (r'^profiles/', include('profiles.urls')),

urlpatterns = patterns('',
    url(r'^songs/', include('hype.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.urls')),
#    url('^profiles/edit', 'profiles.views.edit_profile', {'form_class': ProfileForm,}),
#    url(r'^profiles/', include('profiles.urls')),
#    url(r"^profiles/", include("profiles.urls"))
)