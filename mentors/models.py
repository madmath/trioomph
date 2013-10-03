from django.db import models
from django.contrib.auth.models import User

class MentorProfile(models.Model):
	bio = models.TextField()
	user = models.OneToOneField(User, related_name="profile", null=True, blank=True)
