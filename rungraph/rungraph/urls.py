from django.conf.urls import patterns, include, url
from django.contrib import admin
from main.views import LandingPageView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', LandingPageView.as_view(), name='main_landing_page'),
    url(r'^admin/', include(admin.site.urls)),
)
