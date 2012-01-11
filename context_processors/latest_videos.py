from videos.models import *

def latest_videos(request):
    videos = Video.objects.order_by('-pub_date')[:5]
    return locals()
