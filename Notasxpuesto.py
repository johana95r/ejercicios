
num = int(input("Ingrese numero de estudiantes: " ))

promedioind = []
promediofin = 0
contadorpuest = 0

for numero in range(0,num):
        nombrest = input("Ingrese nombre del estudiante: " )
	prom = float(input("Ingrese numero del promedio del estudiante: " ))
	promedioind.append(prom)

for n in range (0,num):
	promediofin+=promedioind [n]

promediofin /=num

print ("El promedio general del grupo es " + str(promediofin))

promedioind.sort(reverse=True)
for nota in (promedioind):
    print (nota)

