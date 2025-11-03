from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_usuario, name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.logout_usuario, name='logout'),
    path('menu/', views.menu, name='menu'),
    path('calificaciones/', views.calificaciones, name='calificaciones'),
    path('avisos/', views.avisos, name='avisos'),
    path('servicio/', views.servicio, name='servicio'),
]
