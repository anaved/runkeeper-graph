from django.shortcuts import render
from django.views.generic.base import View
import healthgraph
from django.conf import settings
class LandingPageView(View):
    
    template_name = "PLanding.html"
    
    def get(self, request, *args, **kwargs):
        rk_auth_mgr = healthgraph.AuthManager(settings.RUNKEEPER_CLIENT_ID, settings.RUNKEEPER_CLIENT_SECRET,'/'.join((settings.RUNKEEPER_BASEURL, 'login',)))
        rk_auth_uri = rk_auth_mgr.get_login_url()
        rk_button_img = rk_auth_mgr.get_login_button_url('blue', 'black', 300)              
        return render(request, self.template_name,{'rk_button_img': rk_button_img,
                                              'rk_auth_uri': rk_auth_uri,})

