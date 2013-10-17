from django.contrib import admin

from mentors.models import Conference, QuestionAnswer, MentorProfile, VideoLink

class ConferenceInline(admin.TabularInline):
    model = Conference
    extra = 0

class VideoLinkInline(admin.TabularInline):
  model = VideoLink
  extra = 0

class QuestionAnswerInline(admin.TabularInline):
  model = QuestionAnswer
  extra = 0

class MentorProfileAdmin(admin.ModelAdmin):
  inlines = [
        ConferenceInline,
        VideoLinkInline,
        QuestionAnswerInline,
    ]
  list_select_related = True

  def queryset(self, request):
    qs = super(MentorProfileAdmin, self).queryset(request)
    if request.user.is_superuser:
        return qs
    return qs.filter(user=request.user)

admin.site.register(MentorProfile, MentorProfileAdmin)
#admin.site.register(QuestionAnswer)
