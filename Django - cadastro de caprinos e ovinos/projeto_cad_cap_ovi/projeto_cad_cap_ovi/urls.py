
from django.urls import path
from app_cad import views

urlpatterns = [
    # rota, view, nome
    # ususarios.com
    path('',views.home,name='home'),
    # usuarios.com/usuarios
    path('usuarios/',views.usuarios,name='listagem_usuarios')
]
