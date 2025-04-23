from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('financeiro/', include('financeiro.urls')),
    path('estoque/', include('estoque.urls')),
    path('vendas/', include('vendas.urls')),
    path('rh/', include('rh.urls')),
    path('', RedirectView.as_view(url='/financeiro/', permanent=False)),
]
