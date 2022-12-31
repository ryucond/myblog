from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import ListView, DetailView
from .models import Entry, Category



class EntryListView(LoginRequiredMixin,ListView):
    template_name = 'entrada/lista.html'
    context_object_name = 'entradas'
    paginate_by = 6
    login_url = reverse_lazy('users_app:login-user')
    
    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context["categorias"] = Category.objects.all()
        return context
    
    
    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        categoria = self.request.GET.get("categoria", '')
        # Consulta de busqueda
        resultado = Entry.objects.buscar_entrada(kword,categoria) 
        return resultado
    

class EntryDetailView(LoginRequiredMixin,DetailView):
    model = Entry
    template_name = "entrada/detail.html"
    context_object_name = 'detalle'
    login_url = reverse_lazy('users_app:login-user')

    
    

