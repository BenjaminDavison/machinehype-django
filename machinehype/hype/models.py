from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models import signals
from signals import create_profile

class Site(models.Model):
    name = models.CharField(max_length=200)
    last_crawled = models.DateTimeField('date last crawled', null=True)
    site_url = models.CharField(max_length=512, null=True)
    rss_url = models.CharField(max_length=512, null=True)
    
    def was_crawled_today(self):
        return self.last_crawled.date() == datetime.date.today()
    
    was_crawled_today.short_description = 'Crawled today?'
    
    def __unicode__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    blurb = models.CharField(max_length=512)
    pub_date = models.DateTimeField('date published')
    mp3_url = models.CharField(max_length=512)
    likes = models.IntegerField()
    site = models.ForeignKey(Site)
    
    
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    was_published_today.short_description = 'Published today?'
    
    def __unicode__(self):
        return self.name
    
# When model instance is saved, trigger creation of corresponding profile
signals.post_save.connect(create_profile, sender=User)

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    url = models.URLField("Website", blank=True)
    company = models.CharField(max_length=50, blank=True)
    liked_songs = models.ManyToManyField(Song, null=True)
