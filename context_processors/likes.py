from videos.models import *
from profile.models import Like

def likes(request):
    if request.user.is_authenticated():
        likes = Like.objects.filter(user=request.user)
    return locals() 
