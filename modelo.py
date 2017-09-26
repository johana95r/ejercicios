
cantidad = int(input("ingrese la cantidad de edades: " ))


edades = []


sumaedades = 0


for estudiante in range (0,cantidad):
	edad = float(input("ingrese la edad "))
	edades.append(edad)


for c in range(0,cantidad):
	sumaedades += edades[c]


promedio = sumaedades/cantidad

print("El promedio general es " + str(promedio))

