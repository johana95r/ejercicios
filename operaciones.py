res = 0

n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))

class suma ():
	def calcular(self,n1,n2):
		resultado = n1 + n2
		print (str(n1), "+ " + str(n2), "= " +str(resultado))

class resta ():
	def calcular(self,n1,n2):
		resultado = n1 - n2
		print (str(n1), "- " + str(n2), "= " +str(resultado))

class multiplicacion ():
	def calcular(self,n1,n2):
		resultado = n1 * n2
		print (str(n1), "* " + str(n2), "= " +str(resultado))

class division ():
	def calcular(self,n1,n2):
		if (n2 !=0):
			resultado = n1 / n2
			print (str(n1), "/ " + str(n2), "= " +str(resultado))
		else:
			print ("No se puede")

Operacion = input ("¿Que operacion desea hacer? ")
if ((Operacion == "Suma")) or ((Operacion == "suma")) or ((Operacion == "SUMA")):
	Toperacion = suma()
	Toperacion.calcular(n1,n2)
elif ((Operacion == "Resta")) or ((Operacion == "resta")) or ((Operacion == "RESTA")):
	Toperacion = resta()
	Toperacion.calcular(n1,n2)
elif ((Operacion == "Multiplicacion")) or ((Operacion == "Multiplicación")) or ((Operacion == "multiplicacion")) or ((Operacion == "multiplicación")) or ((Operacion == "MULTIPLICACION")) or ((Operacion == "MULTIPLICACIÓN")):
	Toperacion = multiplicacion()
	Toperacion.calcular(n1,n2)
elif ((Operacion == "Division")) or ((Operacion == "División")) or ((Operacion == "division")) or ((Operacion == "división")) or ((Operacion == "DIVISION")) or ((Operacion == "DIVISIÓN")):
 	Toperacion = division()
 	Toperacion.calcular(n1,n2)

else:
	print ("Lo siento... Adiós :(")
