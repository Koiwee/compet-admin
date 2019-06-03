from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, resolve
from django.http import HttpResponseRedirect
from .models import Competicion, Equipo, Jugador, Jornada
from .forms import CompeticionForm, EquipoForm, JugadorForm, JornadaForm
from . serializers import CompeticionSerializers, EquipoSerializers, JugadorSerializers, JornadaSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
import collections

# Create your views here.
def inicio(request):
	return redirect('login')

def add_competicion(request):
	if request.method == "POST":
		form_compet = CompeticionForm(request.POST)
		if form_compet.is_valid():
			post = form_compet.save(commit=False)
			post.admin = request.user
			post.programado = False
			post.save()
			return redirect("login")
	else:
		form_compet = CompeticionForm()
	return render(request,"inicio/reg_compet.html", {'form_compet': form_compet})

class ListarCompeticiones(APIView):
	def get(self,request,pk):
		competiciones = Competicion.objects.filter(admin=pk)
		competiciones_json = CompeticionSerializers(competiciones, many = True)
		return Response(competiciones_json.data)

def competicion_detail(request,pk):
	comp = get_object_or_404(Competicion, pk=pk)

	if comp.programado:
		return redirect('pres_jornada', pk=pk,)

	else:
		equipos = Equipo.objects.filter(competicion=pk)
		num_equipos = len(equipos)
		mod_equipos = num_equipos % 2
		return render(request, 'competicion/comp_detail.html',{'comp':comp, 'num_equipos':num_equipos, 'mod_equipos':mod_equipos})

def add_equipo(request,pk):
	if request.method == "POST":
		form_equipo = EquipoForm(request.POST, request.FILES)
		if form_equipo.is_valid():
			post = form_equipo.save(commit=False)
			post.competicion = Competicion.objects.get(pk=pk)
			post.save()
			return redirect("competicion_detail", pk=post.competicion.pk)
	else:
		form_equipo = EquipoForm()
	return render(request,"equipo/reg_equipo.html", {'form_equipo': form_equipo})

class ListarEquipos(APIView):
	def get(self,request,pk):
		equipos = Equipo.objects.filter(competicion=pk)
		equipos_json = EquipoSerializers(equipos, many = True)
		return Response(equipos_json.data)

def equipo_detail(request,id,pk):
	equipo = get_object_or_404(Equipo, pk=pk)
	competicion = Competicion.objects.get(pk=equipo.competicion.pk)
	return render(request, 'equipo/equipo_detail.html',{'equipo':equipo, 'competicion':competicion})

def add_jugador(request,pk):
	if request.method == "POST":
		form = JugadorForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.equipo = Equipo.objects.get(pk=pk)
			post.save()
			return redirect("equipo_detail", pk=post.equipo.pk, id=post.equipo.competicion.pk)
	else:
		form = JugadorForm()
	return render(request,"jugador/reg_jugador.html", {'form': form})

class ListarJugadores(APIView):
	def get(self,request,pk):
		jugadores = Jugador.objects.filter(equipo=pk)
		jugadores_json = JugadorSerializers(jugadores, many = True)
		return Response(jugadores_json.data)

def jugador_detail(request,id,pk,cl):
	jugador = get_object_or_404(Jugador, pk=cl)
	return render(request, 'jugador/jugador_detail.html',{'jugador':jugador})

def gen_jornada(request, pk):
	teams = list(Equipo.objects.filter(competicion = pk))
	#teams = [1,2,3,4,5,6,7,8]
	count = len(teams)
	
	if count % 2 or count < 4:
		return HttpResponseRedirect(reverse('competicion_detail',args=(pk,)))

	else:
		rounds = count - 1 
		schedule = []

		if count % 2:
			#teams.insert(0, None)
			teams.append(None)

		for turn in range(rounds):
			pairings = []
			for i in range(int(count / 2)):
				pairing = ( (teams[i],teams[count - i - 1]) )
				if i == 0 and turn % 2 :
					pairing = pairing[::-1]
				if schedule and None not in pairing:
					previous_round = list(sum(schedule[-1], ()))
					for team in pairing:
						if team in previous_round and pairing[previous_round.index(team) % 2] == team:
							pairing = pairing[::-1]
				pairings.append(pairing)
			teams.insert(1,teams.pop())
			schedule.append(pairings)

		#print(schedule)
		comp = Competicion.objects.get(pk=pk)
		#print(competicion)
		for ronda in schedule:
			#print(ronda)
			for par in ronda:
				#print(par)
				equi1 = Equipo.objects.get(nombre = par[0])
				equi2 = Equipo.objects.get(nombre = par[1])
				print(str(equi1) + ' ' + str(equi2))
				Jornada.objects.create(equipo1=equi1,nom_eq1=par[0],equipo2=equi2,nom_eq2=par[1],competicion=comp)

		jornada = Jornada.objects.filter(competicion=comp)
		comp.programado = True
		comp.save()
		print(jornada)

		return render(request,"competicion/jornada_detail.html", {'comp': comp, 'jornada': jornada})

def pres_jornada(request,pk):
	comp = Competicion.objects.get(pk=pk)
	jornada = Jornada.objects.filter(competicion=comp)
	return render(request,"competicion/jornada_detail.html", {'comp': comp, 'jornada': jornada})

class ListarJornada(APIView):
	def get(self,request,pk):
		jornada = Jornada.objects.filter(competicion=pk)
		jornada_json = JornadaSerializers(jornada, many = True)
		return Response(jornada_json.data)

def delete_equipo(request,pk):
	id_comp = Equipo.objects.get(pk = pk).competicion.pk
	print (id_comp)
	print(pk)
	Equipo.objects.get(pk = pk).delete()
	pk = id_comp
	return HttpResponseRedirect(reverse('competicion_detail',args=(pk,)))

def resultado_partido(request,pk):
	partido = Jornada.objects.get(pk=pk)
	if request.method == "POST":
		form = JornadaForm(request.POST, instance=partido)
		if form.is_valid():
			form.save()
			return redirect('pres_jornada', pk=partido.competicion.pk,)
	else:
		form = JornadaForm(instance=partido)
	return render(request,"competicion/update_partido.html", {'form': form, 'partido': partido})
