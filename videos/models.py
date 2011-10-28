from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Network(models.Model):
    """ About the network """

    name = models.CharField(max_length = 30, verbose_name = "Name of the Network") 
    #@@TODO:
    #logo = models.ImageField()

    def __unicode__(self):
        return self.name

    
class Channel(models.Model):
    """ About the Channel """
    network = models.ForeignKey(Network)
    name = models.CharField(max_length = 20, verbose_name = "Name of the Channel")
    #@@TODO:
    #logo = models.ImageField()

    def __unicode__(self):
        return self.name


class Category(models.Model):
    """ About the Category """
    name = models.CharField(max_length = 20, verbose_name = "Name of the Category")

    def __unicode__(self):
        return self.name

class Program(models.Model):
    """ About the Program """
    channel = models.ForeignKey(Channel)
    name = models.CharField(max_length = 40, verbose_name = "Name of the Program")
    #@@TODO:
    #    logo = models.ImageField()
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.name

class Video(models.Model):
    """ About the Video """
    program = models.ForeignKey(Program)
    name = models.CharField(max_length = 20, verbose_name = "Name of the Video")
    episode_number = models.IntegerField(max_length=4, verbose_name = "Which episode in series")
    #@@TODO: 
    #thumbnail = models.ImageField()
    pub_date = models.DateTimeField(auto_now = True,verbose_name = "Date of release")
    duration = models.IntegerField(max_length = 6, verbose_name = "Duration in seconds")
    view_count = models.IntegerField(max_length = 7, verbose_name = "Number of views")
    publisher = models.ForeignKey(User)
    last_watched = models.DateTimeField(verbose_name = "Last watched on")

    def __unicode__(self):
        return self.name
