acujugador=[]
acutecni=[]
acumedic=[]
acuhinchas=[]
class info_basica():
	def basic (self):
		nombre = input("Ingrese nombre: ")
		apellido = input("Ingrese apellido: ")
		direccion = input("Ingrese nacionalidad: ")
		edad = input("Ingrese edad: ")
		sexo = input("Ingrese sexo: ")
		partidos_asis = input("Ingrese numero de partidos asistidos: ")
		return("Nombre: "+nombre+" Apellido: "+apellido+" Nacionalidad: "+direccion+" Edad: "+edad+" Sexo: "+sexo+" Part-asist: "+partidos_asis)


class jugadores(info_basica):
	def operar(self):
		medicostot=int(input("Escriba la cantidad de jugadores que desea contratar: "))
		for x in range (1,medicostot+1):
			infor = self.basic()
			numju=input("Numero de jugador: ")
			pos=input("Posicion que ocupa en el equipo: ")
			contra=input("Ingrese finalizacion de contrato :")
			tarje=input("Numero de tarjetas: ")
			acujugador.append (infor+"Numero de jugador : "+numju+"Posicion de juego : "+pos+"Fin de contrato : "+contra+"Numero de tarjetas : "+tarje)
		print()
		print (acujugador)

class Equipo_tecnicos(info_basica):
	def operar(self):
		medicostot=int(input("Escriba la cantidad de equipos tecnicos que desea contratar: "))
		for x in range (1,medicostot+1):
			infor = self.basic()
			partga=input("Partidos ganados: ")
			partper=input("Partidos perdidos: ")
			desc=input("Numero de tarjetas: ")
			acutecni.append(infor+"Partidos ganados: "+partga+" Partidos perdidos: "+partper+"Numero de tarjetas: "+desc)
		print()
		print (acutecni)


class Medicos(info_basica):
	def operar(self):
		medicostot=int(input("Escriba la cantidad de medicos que desea contratar: "))
		for x in range (1,medicostot+1):
			infor = self.basic()
			Jugasis=input("Esciba la cantidad de jugadores asistidos: ")
			acumedic.append (infor+"Jugadores Asistidos: "+Jugasis)
		print()
		print(acumedic)


class Hinchas(info_basica):
	def operar(self):
		medicostot=int(input("Escriba la cantidad de hinchas: "))
		for x in range (1,medicostot+1):
			infor = self.basic()
			equfav=input("Equipo favorito: ")
			parasis=input("Jugador favorito: ")
			acuhinchas.append (infor+"Jugadores favorito: "+parasis+" Equipo favorito: "+equfav)
		print()
		print(acuhinchas)

def ejecucion():
	opcion="0"
	while opcion != "Salir":
		print("         ocupaciones en el equipo             ")
		print()
		print("          - Futbolista                         ")
		print("          - Equipo tecnico                    ")
		print("          - Medico                             ")
		print("          - Hincha                             ")
		print("          - Salir                             ")
		print()
		opcion = input("señor usuario por favor seleccione su ocupacion en el equipo: ")
		print()
		if ((opcion == "Futbolista") or (opcion == "futbolista")):
			jugador1 = jugadores()
			jugador1.operar()
		else:
			if ((opcion == "Equipo tecnico") or (opcion == "equipo tecnico")):
				equiptec1 = Equipo_tecnicos()
				equiptec1.operar()
			else:
				if ((opcion == "Medico") or (opcion == "medico")):
					Medic1 = Medicos()
					Medic1.operar()
				else:
					if ((opcion == "Hincha") or (opcion == "hincha")):
						hincha1 = Hinchas()
						hincha1.operar()




ejecucion()
x=input()
