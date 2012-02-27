'''
Created on 5 Feb 2012

@author: Benjamin
'''
from models import Site, Song, UserProfile
from django.contrib import admin

class SongInline(admin.TabularInline):
    model = Song
    extra = 10

#class UserAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None,               {'fields': ['company']}),
##        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#    ]
##    inlines = [SongInline]
##    
##    list_display = ('question', 'pub_date', 'was_published_today')
##    list_filter = ['pub_date']
#    
##    search_fields = ['name']
##    
##    date_hierarchy = 'pub_date'
##    
#admin.site.register(UserProfile, UserAdmin)

admin.site.register(UserProfile)

class SiteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['site_url']}),
        (None,               {'fields': ['rss_url']}),
        ('Last Crawled', {'fields': ['last_crawled'], 'classes': ['collapse']}),
    ]
    inlines = [SongInline]
#    

admin.site.register(Site, SiteAdmin)