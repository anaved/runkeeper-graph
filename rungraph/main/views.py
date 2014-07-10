from django.conf import settings
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.http.response import Http404
from django.shortcuts import render, redirect
from django.views.generic.base import View, RedirectView
import healthgraph

class LandingPageView(View):
    
    template_name = "PLanding.html"
    
    def get(self, request, *args, **kwargs):            
        if request.session.has_key('rk_access_token'):
            return redirect(reverse('main_welcome_page'))
        else:
            rk_auth_mgr = healthgraph.AuthManager(settings.RUNKEEPER_CLIENT_ID, settings.RUNKEEPER_CLIENT_SECRET, '/'.join((settings.RUNKEEPER_BASEURL, 'login',)))
            rk_auth_uri = rk_auth_mgr.get_login_url()
            rk_button_img = rk_auth_mgr.get_login_button_url('blue', 'black', 300)              
            return render(request, self.template_name, {'rk_button_img': rk_button_img,
                                                  'rk_auth_uri': rk_auth_uri, })


class LoginPageView(View):    
    
    def get_code_or_404(self, request):
        code = request.GET.get('code')
        if not code:
            raise Http404
        return code
    
    def get(self, request, *args, **kwargs):
        code = self.get_code_or_404(request)        
        rk_auth_mgr = healthgraph.AuthManager(settings.RUNKEEPER_CLIENT_ID, settings.RUNKEEPER_CLIENT_SECRET, '/'.join((settings.RUNKEEPER_BASEURL, 'login',)))
        access_token = rk_auth_mgr.get_access_token(code)        
        request.session['rk_access_token'] = access_token
        return redirect(reverse('main_welcome_page'))        

class WelcomePageView(View):    
    template_name = "PWelcome.html"
    
    def get(self, request, *args, **kwargs):
        access_token = request.session.get('rk_access_token')        
        if access_token:
            user = healthgraph.User(session=healthgraph.Session(access_token))
            profile = user.get_profile()
            records = user.get_records()
#             act_iter =  user.get_fitness_activity_iter()
            activities =[] #[act_iter.next() for _ in range(5)]            
            return render(request, self.template_name, {'profile': profile,
                                                  'activities': activities,
                                                   'records': records.get_totals(),
                                                  })
        else:
            redirect(reverse('main_welcome_page')) 

class LogoutPageView(View):   
    
    def get(self, request, *args, **kwargs):        
        logout(request)
        request.session.flush()
        return redirect(reverse('main_landing_page'))   
