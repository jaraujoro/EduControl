from .views import list_menu_x_usuario
from django.urls import path

urlpatterns = [
    path('list_menu_x_usuario/', list_menu_x_usuario),
]