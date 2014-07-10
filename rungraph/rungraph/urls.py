from django.conf.urls import patterns, include, url
from django.contrib import admin
from main.views import LandingPageView, LoginPageView, WelcomePageView, \
    LogoutPageView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', LandingPageView.as_view(), name='main_landing_page'),
     url(r'^login/$', LoginPageView.as_view(), name='main_login_page'),
    url(r'^logout/$', LogoutPageView.as_view(), name='main_logout_page'),
    url(r'^welcome/$', WelcomePageView.as_view(), name='main_welcome_page'),
#      url(r'^view_token/$', LoginPageView.as_view(), name='main_token_page'),
    url(r'^admin/', include(admin.site.urls)),
)
