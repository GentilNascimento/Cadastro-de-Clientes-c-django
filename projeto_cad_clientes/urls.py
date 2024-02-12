from django.urls import path
from app_cad_clientes import views

urlpatterns = [
    # rota, view responsável, nome de referência
    # clientes.com
    path('', views.home,name='home'),
     #clientes.com/clientes
    path('clientes/', views.clientes,name='listagem_clientes')
]
