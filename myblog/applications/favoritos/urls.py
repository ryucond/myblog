#
from django.urls import path
from . import views

app_name = 'favoritos_app'

urlpatterns = [
    path('perfil', views.UserPageListView.as_view(), name='perfil'),
    path('add-favorito/<pk>/', views.AddFavoritesView.as_view(), name='add-fav'),
    path('delete-favorito/<pk>/', views.DeleteFavoritesView.as_view(), name='del-fav'),
]
