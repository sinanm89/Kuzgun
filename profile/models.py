from django.db import models
from django.contrib.auth.models import User

from videos.models import Video

class Favourites(models.Model):
    """ About the favourites """
    user = models.ForeignKey(User)
    video = models.ForeignKey(Video)
    
    def __unicode__(self):
        return str(self.user) +  " || " + str(self.video)



