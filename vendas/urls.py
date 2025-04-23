from django.urls import path
from . import views

app_name = 'vendas'

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/novo/', views.cliente_create, name='cliente_create'),
    path('clientes/<int:pk>/', views.cliente_detail, name='cliente_detail'),
    path('clientes/<int:pk>/editar/', views.cliente_update, name='cliente_update'),
    path('clientes/<int:pk>/excluir/', views.cliente_delete, name='cliente_delete'),
    
    path('pedidos/', views.pedido_list, name='pedido_list'),
    path('pedidos/novo/', views.pedido_create, name='pedido_create'),
    path('pedidos/<int:pk>/', views.pedido_detail, name='pedido_detail'),
    path('pedidos/<int:pk>/editar/', views.pedido_update, name='pedido_update'),
    path('pedidos/<int:pk>/excluir/', views.pedido_delete, name='pedido_delete'),
    path('pedidos/<int:pk>/adicionar-item/', views.item_pedido_create, name='item_pedido_create'),
    path('pedidos/item/<int:pk>/excluir/', views.item_pedido_delete, name='item_pedido_delete'),
]
