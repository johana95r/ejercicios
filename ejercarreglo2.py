#Dada la identificacion, nombre y la nota definitiva de un determinado numero de estudiantes de la
#falcultad  de ingenieria, realice un algoritmo que permita calcular y dar como salida lo siguiente:
#La cantidad de alumnos aprobados 
#La cantidad de alumnos reprobados
#El promedio general de notas
#Nota: En la UPC , un estudiante aprueba on una calificacion igual o superior a 3.0 y 
#en un rango de calificacion entre 1.0 y 5.0

num = int(input("Ingrese numero de estudiantes: " ))
estudiante = []
sumadef = 0
aprob= 0
grupest= []


for numero in range(0,num):
	idest = int(input("Ingrese numero de indentificacion del estudiante: " ))
	estudiante.append(idest)
	nombrest = input("Ingrese nombre del estudiante: " )
	estudiante.append(nombrest)
	notadef = float(input("Ingrese nota definitiva del estudiante"))
	while (notadef < 1 or notadef > 5):

		print("la nota ingresada esta fuera del rango")
		notadef = float(input("reingrese la nota definitiva: "))
	estudiante.append(notadef)

	grupest.append(estudiante)

for x in range(0,num):
	if (grupest[x][2] >= 3 and grupest[x][2] <= 5):
		aprob =+ 1

	sumadef += grupest[x][2]

promedio = sumadef/num

reprobados = num - aprob

print("Aprobados: " + str(aprob) + ". Reprobados: " + str(reprobados) + ". Promedio General: " + str(promedio))

