from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import resolve_url

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def get_login_redirect_url(self, request):
        if hasattr(request.user, 'perfil') and not request.user.perfil.apodo:
            return resolve_url('completar_perfil')
        return resolve_url('home')