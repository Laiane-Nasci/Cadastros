from django.urls import path
from CadastroCliente import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Clientes', views.listar_clientes, name='Clientes'),
]

