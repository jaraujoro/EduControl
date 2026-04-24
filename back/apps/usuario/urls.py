from django.urls import path
from .views import list_usuario, login_usuario

urlpatterns = [
    path('list_usuario/', list_usuario),
    path('login_usuario/', login_usuario)
]