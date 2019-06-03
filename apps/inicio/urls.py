from django.contrib import admin
from django.urls import path
from .views import inicio, add_competicion, ListarCompeticiones, competicion_detail, add_equipo, ListarEquipos, equipo_detail, add_jugador, ListarJugadores, jugador_detail, gen_jornada, delete_equipo, ListarJornada, resultado_partido,pres_jornada
from django.contrib.auth.views import LoginView, LogoutView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', LoginView.as_view(template_name="inicio/index.html"), name="login"),
    path('cerrar/', LogoutView.as_view(), name="logout"),
    path('',inicio, name="inicio"),
    path('nueva_competicion/',add_competicion, name="add_competicion"),
    path('api/competicion/listar/<int:pk>',ListarCompeticiones.as_view(),name = "listar_competiciones"),
    path('competicion/<int:pk>/',competicion_detail, name="competicion_detail"),
    path('nuevo_equipo/<int:pk>/',add_equipo, name="add_equipo"),
    path('api/equipo/listar/<int:pk>',ListarEquipos.as_view(),name = "listar_equipos"),
    path('competicion/<int:id>/equipo/<int:pk>/',equipo_detail, name="equipo_detail"),
    path('nuevo_jugador/<int:pk>/',add_jugador, name="add_jugador"),
    path('api/jugador/listar/<int:pk>/',ListarJugadores.as_view(),name = "listar_jugadores"),
    path('competicion/<int:id>/equipo/<int:pk>/jugador/<int:cl>/',jugador_detail, name="jugador_detail"),
    path('jor_gen/<int:pk>/',gen_jornada, name="gen_jornada"),
    path('jornada/<int:pk>/',pres_jornada, name="pres_jornada"),
    path('api/jornada/listar/<int:pk>/',ListarJornada.as_view(), name="listar_jornada"),
    path('delete_equipo/<int:pk>/',delete_equipo, name="delete_equipo"),
    path('resultado_partido/<int:pk>/',resultado_partido, name="resultado_partido"),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)