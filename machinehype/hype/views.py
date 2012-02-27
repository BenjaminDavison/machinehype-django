from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from machinehype.hype.models import Site, Song, UserProfile
from django.core.paginator import Paginator, InvalidPage, EmptyPage

def index(request):
    latest_songs = Song.objects.all().order_by('-pub_date')
    paginator = Paginator(latest_songs, 10)
    
    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        songs = paginator.page(page)
    except (EmptyPage, InvalidPage):
        songs = paginator.page(paginator.num_pages)
        
        
    return render_to_response('songs/index.html', {"songs" : songs},
                              context_instance=RequestContext(request))

#get users likes
def user_songs(request, user_id):
    #check if there actually is a user
    if request.user.is_authenticated() == True:
        latest_songs = UserProfile.objects.get(id=request.user.id).liked_songs.all()
        paginator = Paginator(latest_songs, 10)
        
        # Make sure page request is an int. If not, deliver first page.
        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1
    
        # If page request (9999) is out of range, deliver last page of results.
        try:
            songs = paginator.page(page)
        except (EmptyPage, InvalidPage):
            songs = paginator.page(paginator.num_pages)
            
            
        return render_to_response('songs/index.html', {"songs" : songs},
                                  context_instance=RequestContext(request))        

#hit the like button
def like(request, song_id):
    #check if there actually is a user
    if request.user.is_authenticated() == True:
        #has user already liked this song
        if UserProfile.objects.filter(liked_songs=song_id):
            #if so remove it from their liked list
            UserProfile.objects.get(id=request.user.id).liked_songs.remove(Song.objects.get(id=song_id))
            #minus 1 from song liked int
            s = Song.objects.get(id=song_id)
            s.likes -= 1
            s.save()
        else:
            #add it to their liked list
            UserProfile.objects.get(id=request.user.id).liked_songs.add(Song.objects.get(id=song_id))
            #+1 to song liked
            s = Song.objects.get(id=song_id)
            s.likes += 1
            s.save()
    else:
        #tell them they need to register
        pass
    
    return HttpResponseRedirect(reverse('hype.views.index'))

def popular_songs(request):
    latest_songs = Song.objects.all().order_by('-likes')
    paginator = Paginator(latest_songs, 10)
    
    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        songs = paginator.page(page)
    except (EmptyPage, InvalidPage):
        songs = paginator.page(paginator.num_pages)
        
        
    return render_to_response('songs/index.html', {"songs" : songs},
                              context_instance=RequestContext(request))