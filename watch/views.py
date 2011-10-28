from kuzgun.decorators import rendered_with
from videos.models import Network
from videos.models import Channel
from videos.models import Category
from videos.models import Program
from videos.models import Video

@rendered_with('watch/watch.html')
def watch(request):
	video = Video.objects.get()
	return locals()