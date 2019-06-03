from rest_framework import serializers
from . models import Competicion, Equipo, Jugador, Jornada

class CompeticionSerializers(serializers.ModelSerializer):
	class Meta:
		model = Competicion
		fields = '__all__'

class EquipoSerializers(serializers.ModelSerializer):
	class Meta:
		model = Equipo
		fields = '__all__'

class JugadorSerializers(serializers.ModelSerializer):
	class Meta:
		model = Jugador
		fields = '__all__'

class JornadaSerializers(serializers.ModelSerializer):
	class Meta:
		model = Jornada
		fields = '__all__'