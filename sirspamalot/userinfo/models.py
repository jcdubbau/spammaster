from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.conf import settings
   
class SpamMessage(models.Model):
    date_posted = models.DateTimeField('date posted', default=datetime.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    spam_message = models.CharField(max_length=140)
    
    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        return self.spam_message
        #return "{} in {}".format(self.spam_message, self.profile.name)


class Profile(models.Model):
    # Relations
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile")
    date = models.DateTimeField('date profile created', default=datetime.now)
    user_bio = models.CharField(max_length=500, blank=True)

    def __str__(self):
       return self.user.username
 
    def get_absolute_url(self):
       return reverse('spam_message : user_page', kwargs={'id': self.pk})
    
   
     
