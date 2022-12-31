import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView, CreateView
)

from .models import Home, Suscribers
from .forms import SuscribersForm, ContactForm
from applications.entrada.models import Entry

class TestPlantilla(TemplateView):
    template_name = "plantillas/register.html"   
    

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home/index.html'
    login_url = reverse_lazy('users_app:login-user')
    
    def get_context_data(self, **kwargs):
        context = super(HomePageView,self).get_context_data(**kwargs)
        #cargamos mensaje home
        context["mensaje"] = Home.objects.latest('created')
        #contexto para portada
        context["portada"] = Entry.objects.entrada_en_portada()
        #contexto para articulos home
        context["entradas_home"] = Entry.objects.entrada_en_home()
        #contexto para entradas recientes
        context["entradas_recientes"] = Entry.objects.entrada_recientes()
        #enviamos formulario de suscripcion
        context["form"] = SuscribersForm
        return context
    
    
class SuscribersCreateView(CreateView):
    form_class = SuscribersForm
    success_url = '.'
    

class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url = '.'
    

    
