
from django.urls import path
from . import views
from .views import MascotaListAPIView
urlpatterns = [

    path('',views.inicio,name='inicio'),
    ##path('api/mascotas/',views.api_mascotas),
    path('api/mascotas/<int:pk>/',views.detalle_mascota),
    path('api/propietarios/',views.api_propietarios),
    path('api/consultas/', views.api_consultas),
    path('api/mascotas/', MascotaListAPIView.as_view(), name='mascotas-list'),
    path('api/perfil/', views.perfil, name='api_perfil'),
    path('api/estadisticas/', views.estadisticas, name='api_estadisticas'),
    path('api/sesion/', views.api_sesion, name='api_sesion'),
]