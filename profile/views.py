# Create your views here.

from django.http import HttpResponse

from videos.models import Video, Program
from profile.models import Favourite, Like



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
