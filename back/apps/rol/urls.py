from .views import list_rol, list_rol_x_menu, save_rol
from django.urls import path

urlpatterns = [
    path('list_rol/', list_rol),
    path('list_rol_x_menu/<int:rol_id>/', list_rol_x_menu),
    path('save_rol/', save_rol),
]