from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from django.views.generic import ListView, View, DeleteView
from .models import Favorites
from applications.entrada.models import Entry




class UserPageListView(LoginRequiredMixin,ListView):
    template_name = "favoritos/perfil.html"
    context_object_name = 'favoritos'
    login_url = reverse_lazy('users:login-user')
    
    def get_queryset(self):
        return Favorites.objects.entradas_user(self.request.user)
    

class AddFavoritesView(LoginRequiredMixin,View):
    
    login_url = reverse_lazy('users:login-user')
    
    def post(self, request, *args, **kwargs):
        #recuperar usuario
        usuario = self.request.user
        entrada = Entry.objects.get(id=self.kwargs['pk'])
        #registramos favorito
        Favorites.objects.create(
            user = usuario,
            entry = entrada,
        ) 
        
        return HttpResponseRedirect(
            reverse('favoritos_app:perfil')
        )
        
class DeleteFavoritesView(DeleteView):
    model = Favorites
    success_url = '/perfil'
    
    
    


