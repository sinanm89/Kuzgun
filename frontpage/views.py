# Create your views here.
from kuzgun.decorators import rendered_with

@rendered_with('frontpage/index.html')
def frontpage(request):
	return locals()