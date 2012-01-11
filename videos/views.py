from videos.models import *
from kuzgun.decorators import rendered_with
from django.http import Http404

@rendered_with('latest_videos.html')
def latest_videos(request):
    videos = Video.objects.order_by('-pub_date')[:5]
    return locals()

@rendered_with('program_videos.html')
def program_videos(request, program_name):
    program = Program.objects.get(name = program_name) 
    videos = Video.objects.filter(program = program)
    return locals()

@rendered_with('category_programs.html')
def category_programs(request, category_name):
    category = Category.objects.get(name = category_name)
    programs = Program.objects.filter(category = category)
    return locals()

@rendered_with('channel_programs.html')
def channel_programs(request, channel_name):
    channel = Channel.objects.get(name = channel_name)
    programs = Program.objects.filter(channel = channel)
    return locals()

@rendered_with('network_channels.html')
def network_channels(request, network_name):
    network = Network.objects.get(name = network_name)
    channels = Channel.objects.get(network = network)
    return locals()

@rendered_with('networks.html')
def networks(request):
    networks = Network.objects.all()
    return locals()

@rendered_with('video.html')
def video(request, program_name, episode_number):
    program = Program.objects.get(name = program_name)
    video = Video.objects.get(program = program, episode_number = episode_number)
    return locals()
