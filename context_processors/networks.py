from videos.models import *

def networks(request):
    networks = Network.objects.all()
    return locals()
