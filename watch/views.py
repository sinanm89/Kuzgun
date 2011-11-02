from kuzgun.decorators import rendered_with
from videos.models import Network
from videos.models import Channel
from videos.models import Category
from videos.models import Program
from videos.models import Video

@rendered_with('watch/watch.html')
def watch_latest(request):
	video = Video.objects.latest('pub_date')
	return locals()

@rendered_with('watch/watch.html')
def watch(request,name):
	video = Video.objects.get(name=name)
	return locals()