from django.db import models
from django.contrib.auth.models import User

from videos.models import Program, Video

class Favourite(models.Model):
    """ About the favourites """
    user = models.ForeignKey(User)
    program = models.ForeignKey(Program)
    
    def __unicode__(self):
        return str(self.user) +  " || " + str(self.program)


class Like(models.Model):
    """ About the likes """
    user = models.ForeignKey(User)
    video = models.ForeignKey(Video)

    def __unicode__(self):
        return str(self.user) +  " || " + str(self.video)



