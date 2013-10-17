from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

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

class MentorProfileInline(admin.TabularInline):
  extra = 1
  max_num = 1
  model = MentorProfile
  fk_name = 'user'

class UserAdmin(UserAdmin):
  inlines = [
      MentorProfileInline,
  ]
  fieldsets = (
    (None, {
      'fields': ('username', 'password', 'first_name', 'last_name', 'email', 'groups', 'is_staff')
      }),
  )

  def queryset(self, request):
    qs = super(UserAdmin, self).queryset(request)
    if request.user.is_superuser:
        return qs
    return qs.filter(id=request.user.pk)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
