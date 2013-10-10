from django.db import models
from django.contrib.auth.models import User


class MentorProfile(models.Model):
  user = models.OneToOneField(User, related_name="profile", null=True, blank=True)
  bio = models.TextField(verbose_name="Short biography")
  oneliner = models.TextField(verbose_name="Sentence that represents well. Dream, one-liner, quote, etc.")
  thumbnail = models.ImageField(upload_to="thumbs/", blank=True, null=True)

  def __unicode__(self):
    return u"Profile for: " + self.user.first_name

class VideoLink(models.Model):
  title = models.CharField(max_length=1000)
  description = models.TextField(verbose_name="Video description")
  embed_code = models.TextField(verbose_name="YouTube or Vimeo embed code (iframe)")
  video_id = models.CharField(max_length=1000)
  added_on = models.DateTimeField(auto_now_add=True)
  owner_profile = models.ForeignKey(MentorProfile)

  def get_thumbnail(self):
    if self.video_id:
      return 'http://i.ytimg.com/vi/' + self.video_id + '/0.jpg'

class Conference(models.Model):
  title = models.CharField(max_length=1000)
  description = models.TextField(verbose_name="Conference description")
  link = models.CharField(max_length=1000, verbose_name="Link to more information about the conference")
  date = models.DateTimeField(verbose_name="When the conference is taking place")
  owner_profile = models.ForeignKey(MentorProfile)

class QuestionAnswer(models.Model):
  question = models.CharField(max_length=5000)
  answer = models.TextField()
  owner_profile = models.ForeignKey(MentorProfile)
  asker = models.ManyToManyField(User, related_name="question", null=True, blank=True)
