from django.urls import path
from . import views

app_name = 'rh'

urlpatterns = [
    path('', views.index, name='index'),
    path('departamentos/', views.departamento_list, name='departamento_list'),
    path('departamentos/novo/', views.departamento_create, name='departamento_create'),
    path('departamentos/<int:pk>/', views.departamento_detail, name='departamento_detail'),
    path('departamentos/<int:pk>/editar/', views.departamento_update, name='departamento_update'),
    path('departamentos/<int:pk>/excluir/', views.departamento_delete, name='departamento_delete'),
    
    path('cargos/', views.cargo_list, name='cargo_list'),
    path('cargos/novo/', views.cargo_create, name='cargo_create'),
    path('cargos/<int:pk>/', views.cargo_detail, name='cargo_detail'),
    path('cargos/<int:pk>/editar/', views.cargo_update, name='cargo_update'),
    path('cargos/<int:pk>/excluir/', views.cargo_delete, name='cargo_delete'),
    
    path('funcionarios/', views.funcionario_list, name='funcionario_list'),
    path('funcionarios/novo/', views.funcionario_create, name='funcionario_create'),
    path('funcionarios/<int:pk>/', views.funcionario_detail, name='funcionario_detail'),
    path('funcionarios/<int:pk>/editar/', views.funcionario_update, name='funcionario_update'),
    path('funcionarios/<int:pk>/excluir/', views.funcionario_delete, name='funcionario_delete'),
    
    path('beneficios/', views.beneficio_list, name='beneficio_list'),
    path('beneficios/novo/', views.beneficio_create, name='beneficio_create'),
    path('beneficios/<int:pk>/', views.beneficio_detail, name='beneficio_detail'),
    path('beneficios/<int:pk>/editar/', views.beneficio_update, name='beneficio_update'),
    path('beneficios/<int:pk>/excluir/', views.beneficio_delete, name='beneficio_delete'),
]
