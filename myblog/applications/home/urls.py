#
from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path(
        'plantilla/', 
        views.TestPlantilla.as_view(),
        name='plantilla',
    ),
    path("panel/", views.HomePage.as_view(), name='panel'),  
]