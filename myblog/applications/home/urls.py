#
from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('register-suscription', views.SuscribersCreateView.as_view(), name='add-suscription'),
    path('contacto', views.ContactCreateView.as_view(), name='add-contacto')
]