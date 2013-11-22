from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_protect

from mentors.models import MentorProfile, QuestionAnswer

@login_required
def mentor(request, mentor_id):
  try:
    profile = MentorProfile.objects.get(pk=mentor_id)
  except ObjectDoesNotExist:
    print 'Can\'t find mentor profile', mentor_id
    return redirect('/')

  data = {'user': request.user}
  if request.method == "POST":
    if _AddQuestion(request, profile, request.POST['question']):
      data['added_question'] = True

  data['profile'] = profile
  data.update(csrf(request))

  if profile.user == request.user or request.user.is_superuser:
    data.update({'is_editable': True})

  # Add questions.
  questions = QuestionAnswer.objects.filter(owner_profile=profile)
  questions_list = [q for q in questions if q.answer]
  data['questions'] = questions_list

  return render_to_response('mentors/mentor.html', data)

def index(request):
  data = {}
  all_profiles = MentorProfile.objects.all()
  data.update({'avail_profiles':all_profiles, 'user': request.user})
  return render_to_response('mentors/index.html', data)


def _AddQuestion(request, profile, question):
  if not question:
    return False

  QuestionAnswer.objects.create(question=question, owner_profile=profile, asker=request.user)
  return True
