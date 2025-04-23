from django.urls import path
from . import views

app_name = 'financeiro'

urlpatterns = [
    path('', views.index, name='index'),
    path('contas-a-pagar/', views.contas_a_pagar_list, name='contas_a_pagar_list'),
    path('contas-a-pagar/nova/', views.conta_a_pagar_create, name='conta_a_pagar_create'),
    path('contas-a-pagar/<int:pk>/', views.conta_a_pagar_detail, name='conta_a_pagar_detail'),
    path('contas-a-pagar/<int:pk>/editar/', views.conta_a_pagar_update, name='conta_a_pagar_update'),
    path('contas-a-pagar/<int:pk>/excluir/', views.conta_a_pagar_delete, name='conta_a_pagar_delete'),
    
    path('contas-a-receber/', views.contas_a_receber_list, name='contas_a_receber_list'),
    path('contas-a-receber/nova/', views.conta_a_receber_create, name='conta_a_receber_create'),
    path('contas-a-receber/<int:pk>/', views.conta_a_receber_detail, name='conta_a_receber_detail'),
    path('contas-a-receber/<int:pk>/editar/', views.conta_a_receber_update, name='conta_a_receber_update'),
    path('contas-a-receber/<int:pk>/excluir/', views.conta_a_receber_delete, name='conta_a_receber_delete'),
    
    path('fluxo-de-caixa/', views.fluxo_caixa_list, name='fluxo_caixa_list'),
    path('fluxo-de-caixa/novo/', views.fluxo_caixa_create, name='fluxo_caixa_create'),
    path('fluxo-de-caixa/<int:pk>/', views.fluxo_caixa_detail, name='fluxo_caixa_detail'),
    path('fluxo-de-caixa/<int:pk>/editar/', views.fluxo_caixa_update, name='fluxo_caixa_update'),
    path('fluxo-de-caixa/<int:pk>/excluir/', views.fluxo_caixa_delete, name='fluxo_caixa_delete'),
]
