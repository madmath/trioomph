from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response, redirect

from mentors.models import MentorProfile

def mentor(request, mentor_id):
  try:
    profile = MentorProfile.objects.get(pk=mentor_id)
  except ObjectDoesNotExist:
    print 'Can\'t find mentor profile', mentor_id
    return redirect('/')

  data = {'profile': profile}
  return render_to_response('mentors/mentor.html', data)

def index(request):
  data = {}
  all_profiles = MentorProfile.objects.all()
  data.update({'avail_profiles':all_profiles, 'user': request.user})
  return render_to_response('mentors/index.html', data)
