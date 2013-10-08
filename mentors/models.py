from django.db import models
from django.contrib.auth.models import User

class MentorProfile(models.Model):
  user = models.OneToOneField(User, related_name="profile", null=True, blank=True)
  bio = models.TextField()
  oneliner = models.TextField()
  thumbnail = models.ImageField(upload_to="thumbs/", blank=True, null=True)

  def __unicode__(self):
    return u"Profile for: " + self.user.first_name
