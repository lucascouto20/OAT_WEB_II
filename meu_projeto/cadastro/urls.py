from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views



urlpatterns = [
    path('', views.listar_filmes_series, name='listar_filmes_series'),  # Página inicial
    path('adicionar/', views.criar_filme_serie, name='criar_filme_serie'),  # Página de adicionar filme
    path('editar/<int:id>/', views.editar_filme_serie, name='editar_filme_serie'),  # Página de editar filme
    path('excluir/<int:id>/', views.excluir_filme_serie, name='excluir_filme_serie'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
