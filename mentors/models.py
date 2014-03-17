from django.db import models
from django.contrib.auth.models import User


class MentorProfile(models.Model):
  user = models.OneToOneField(User, related_name="profile", null=True, blank=True)
  bio = models.TextField(verbose_name="Short biography", blank=True)
  oneliner = models.TextField(verbose_name="Sentence that represents well. Dream, one-liner, quote, etc.", blank=True)
  thumbnail = models.ImageField(upload_to="thumbs/", blank=True, null=True)

  def __unicode__(self):
    return u"%s %s" % (self.user.first_name, self.user.last_name)

class VideoLink(models.Model):
  title = models.CharField(max_length=1000, blank=True)
  description = models.TextField(verbose_name="Video description", blank=True)
  embed_code = models.TextField(verbose_name="YouTube or Vimeo embed code (iframe)", blank=True)
  video_id = models.CharField(max_length=1000, blank=True)
  added_on = models.DateTimeField(auto_now_add=True)
  owner_profile = models.ForeignKey(MentorProfile)

  def get_thumbnail(self):
    if self.video_id:
      return 'http://i.ytimg.com/vi/' + self.video_id + '/0.jpg'

class Conference(models.Model):
  title = models.CharField(max_length=1000)
  description = models.TextField(verbose_name="Conference description", blank=True)
  link = models.CharField(max_length=1000, verbose_name="Link to more information about the conference", blank=True)
  date = models.DateTimeField(verbose_name="When the conference is taking place")
  owner_profile = models.ForeignKey(MentorProfile)

class QuestionAnswer(models.Model):
  question = models.CharField(max_length=5000)
  answer = models.TextField(blank=True)
  owner_profile = models.ForeignKey(MentorProfile)
  asker = models.ForeignKey(User)


# STUDENTS

class Choices(models.Model):
  description = models.CharField(max_length=300)

  def __unicode__(self):
    return self.description

class StudentProfile(models.Model):
  user = models.ForeignKey(User, blank=True, unique=True, verbose_name='user')
  choices = models.ManyToManyField(Choices)
  student_email = models.CharField(max_length=100)
  school = models.CharField(max_length=100)
  year = models.CharField(max_length=25, blank=True)
