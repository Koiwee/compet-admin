from django.contrib import admin
from .models import Competicion, Equipo, Jugador, Jornada
# Register your models here.

admin.site.register(Competicion)
admin.site.register(Equipo)
admin.site.register(Jugador)
admin.site.register(Jornada)