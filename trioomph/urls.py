from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'trioomph.views.home', name='home'),
    url(r'^$', 'mentors.views.index', name='index'),
    url(r'^a/', include('registration.backends.default.urls')),
    #url(r'^trioomph/', include('trioomph.foo.urls')),
    url(r'^mentor/(\d+)', 'mentors.views.mentor', name='mentor'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
