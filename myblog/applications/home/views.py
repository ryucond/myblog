import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView
)

from applications.entrada.models import Entry

class TestPlantilla(TemplateView):
    template_name = "plantillas/register.html"   
    

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home/index.html'
    login_url = reverse_lazy('users_app:login-user')
    
    def get_context_data(self, **kwargs):
        context = super(HomePageView,self).get_context_data(**kwargs)
        context["portada"] = Entry.objects.entrada_en_portada()
        return context
    
