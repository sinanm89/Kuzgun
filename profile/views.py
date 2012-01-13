# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect

from videos.models import Video, Program
from profile.models import Favourite, Like

from django.contrib.auth import authenticate, login, logout

def fav(request,program_name):
    user = request.user
    program = Program.objects.get(name = program_name)
    fav = Favourite(user = user, program = program)
    fav.save()
    return HttpResponse("OK")

def like(request,video_name):
    user = request.user
    video = Video.objects.get(name = video_name)
    like = Like(user = user, video = video)
    like.save()
    return HttpResponse("OK")

def site_login(request):
  print "ahmet"
  if request.method == 'POST':
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    print "ahmet"

    if user is not None:
        login(request, user)
        print "ahmetlog"
        return HttpResponse("OK")


    else:
        return HttpResponse("NOTOK")

      
def site_logout(request):
  logout(request)
  return HttpResponseRedirect("/")
