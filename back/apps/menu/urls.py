from .views import list_menu_x_usuario, list_menu
from django.urls import path

urlpatterns = [
    path('list_menu_x_usuario/', list_menu_x_usuario),
    path('list_menu/', list_menu),
]