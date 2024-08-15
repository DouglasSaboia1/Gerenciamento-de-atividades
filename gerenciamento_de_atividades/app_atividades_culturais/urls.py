from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('', views.lista_eventos, name='lista_eventos'),
    path('evento/<int:pk>/', views.detalhe_evento, name='detalhe_evento'),
    path('evento/novo/', views.criar_evento, name='criar_evento'),
    path('evento/<int:pk>/editar/', views.editar_evento, name='editar_evento'),
    
]