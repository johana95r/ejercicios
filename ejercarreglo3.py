
#Dado un grupo de "n" numeros (Diferentes a 0), realice un algoritmo que permita determinar
#y dar como salida lo siguiente:
# Numero mayor y numero menor encontrado en el grupo
#Cantidad de numeros mayor a 150
#Cantidad de numeros negativos
#Promedio de los positivos encontrados



cantnum = int(input("ingrese la cantidad de numeros: "))

may150 = 0
cantpos = 0 
cantneg = 0
sumapos = 0
numeros = []

if (cantnum > 0):

	for num in range(0,cantnum):

		numeroing = int(input("Ingrese el numero: "))
		numeros.append(numeroing)

		
	mayor, menor = numeros[0], numeros[0]

	for numero in range(1,cantnum):
		
		if (numeros[numero] > mayor):
			mayor = numeros[numero]
		
		elif (numeros[numero] < menor):
			menor = numeros[numero]
		
		if (numeros[numero] > 0):
			
			cantpos += 1
			sumapos += numeros[numero]

		
			if (numeros[numero] > 150):
				may150 += 1
		else:
			
			cantneg += 1

	
	PromPos = sumapos / float(cantpos)


	print("Mayor: " + str(mayor))
    print("Menor: " + str(menor)) 
    print("Promedio de Positivos: " + str(PromPos))
    print("Cantidad de Negativos: " + str(cantneg))
