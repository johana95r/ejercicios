
#Dada la identifiacion, nombre y la nota definitiva de 4 materias de cada estudiante perteneciente a un
#grupo de ing financiera; realice un algoritmo que permita calcular y dar como salida el promedio
#de notas de cada estudiante y al final se desea conocer el promedio general del grupo

numest = int(input("Ingrese numero de estudiantes: " ))
estudiante = []
grupo = []
numnotas = 4
sumaind = 0
sumagrupal = 0
promind = 0
promgeneral = 0
promeind = []

if (numest > 0):

    for numero in range(0,numest):
	idest = int(input("Ingrese numero de identificacion del estudiante: " ))
	estudiante.append(idest)
	nombrest = input("Ingrese nombre del estudiante: " )
	estudiante.append(nombrest)
	notadef = float(input("Ingrese nota definitiva del estudiante"))
	estudiante.append(notadef)
	print notadef

	grupo.append(estudiante)

for notind in range(0,len(grupo)):
		for x in range(0,numnotas):

			sumaind += grupo[notind][2][x]

		promedioind = float(sumaind/numnotas)
		promeind.append(promind)

		print("El promedio personal de " + str(grupo[notind][0]) + " es " + str(promind))

for promgrup in range(0,len(promindi)):
		
		sumagrupal += promindi[promgrup]

promgeneral = sumagrupal/len(promindi)

print("Promedio general del grupo: " + str(promgeneral))



