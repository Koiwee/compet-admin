from django.db import models

class Competicion(models.Model):
	admin = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	fecha_inicio = models.DateField(blank = False, null = False)
	fecha_fin = models.DateField(blank = False, null = False)
	nombre = models.CharField(max_length = 100, blank = False, null = False)
	descripcion = models.CharField(max_length = 100, blank = False, null = False)
	programado = models.BooleanField()

	def __str__(self):
		return self.nombre

class Equipo(models.Model):
	nombre = models.CharField(max_length = 80, blank = False, null = False)
	escudo = models.ImageField(upload_to = "img_escudos", blank = True, null = True)
	responsable = models.CharField(max_length = 80, blank = False, null = False)
	creacion = models.DateField(blank = False, null = False)
	competicion = models.ForeignKey("Competicion",on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre

class Jugador(models.Model):
	nombre = models.CharField(max_length=80,blank = False, null = False)
	posicion = models.CharField(max_length=30,blank = False, null = False)
	dorsal = models.CharField(max_length=3,blank = False, null = False)
	foto = models.ImageField(upload_to="img_jugadores",blank = True, null = True)
	equipo = models.ForeignKey("Equipo",on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre

class Jornada(models.Model):
	fecha = models.DateField(blank = True, null = True)
	equipo1 = models.ForeignKey("Equipo",on_delete=models.CASCADE, related_name="local")
	nom_eq1 = models.CharField(max_length = 100, blank = False, null = False, default = "Nombre equipo")
	equipo2 = models.ForeignKey("Equipo",on_delete=models.CASCADE, related_name="foraneo")
	nom_eq2 = models.CharField(max_length = 100, blank = False, null = False, default = "Nombre equipo")
	ptsEq1 = models.IntegerField(blank = True, null = True)
	ptsEq2 = models.IntegerField(blank = True, null = True)
	victoria = models.CharField(max_length = 100, blank = True, null = True)
	competicion = models.ForeignKey("Competicion",on_delete=models.CASCADE)
	btn_result = models.CharField(max_length = 20, blank = False, null = False,default = "AGREGAR")

	def ganador(self):
		return self.victoria

