from django import forms
from .models import Competicion, Equipo, Jugador, Jornada

class CompeticionForm(forms.ModelForm):
	class Meta:
		model = Competicion
		fields = ('nombre','descripcion','fecha_inicio','fecha_fin',)
		widgets = {
			'nombre': forms.TextInput(attrs={'size':"100"}),
			'descripcion': forms.TextInput(attrs={'size':"100"}),
            'fecha_inicio': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Seleciona una fecha', 'type':'date'}),
            'fecha_fin': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Seleciona una fecha', 'type':'date'}),
        }

class EquipoForm(forms.ModelForm):
	class Meta:
		model = Equipo
		fields = ('nombre','responsable','creacion','escudo')
		widgets = {
			'nombre': forms.TextInput(attrs={'size':"80"}),
			'responsable': forms.TextInput(attrs={'size':"80"}),
            'creacion': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Seleciona una fecha', 'type':'date'}),
        }

class JugadorForm(forms.ModelForm):
	class Meta:
		model = Jugador
		fields = ('nombre','dorsal','posicion','foto',)
		widgets = {
			'nombre': forms.TextInput(attrs={'size':"80"}),
			'dorsal': forms.TextInput(attrs={'size':"5"}),
            'posicion': forms.TextInput(attrs={'size':"30"}),
        }

class JornadaForm(forms.ModelForm):
	class Meta:
		model = Jornada
		fields = ('ptsEq1','ptsEq2','victoria',)
		widgets = {
            'victoria': forms.TextInput(attrs={'size':"80"}),
        }