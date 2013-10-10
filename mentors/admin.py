from django.contrib import admin

from mentors.models import Conference, QuestionAnswer, MentorProfile, VideoLink

admin.site.register(Conference)
admin.site.register(QuestionAnswer)
admin.site.register(VideoLink)
admin.site.register(MentorProfile)
