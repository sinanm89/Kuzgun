from videos.models import *
from profile.models import Favourite

def favourites(request):
    if request.user.is_authenticated():
        favs = Favourite.objects.filter(user=request.user)
    return locals() 
