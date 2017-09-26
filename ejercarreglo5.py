#La electrificadora de la ciudad de Girardot desea un programa que le permita calcular el consumo de 
#un determinado número de clientes, teniendo en cuenta las lecturas actual y anterior, dichas lecturas 
#son digitadas por el usuario. El valor del vatio es ingresado por teclado y al final se desea conocer: 
#Consumo de cada cliente junto con su total a pagar y el promedio general de consumo del grupo de clientes


cantclientes = int(input("cantidad de Clientes: " ))

valorvatio = int(input("valor del vatio: "))
verificarnumpos(valorvatio, valorvatio)


consumoprom = 0
sumaconsumo = 0

consumoClientes = []

if (cantClientes > 0):
	
	for cliente in range(0,cantClientes):

		lectatual = int(input("Ingrese lectura actual: " ))
		verificarnumpos(lectactual, lectactual)
		lectanterior = int(input("Ingrese lectura anterior: " ))
		verificarnumpos(lectanterior, lectanterior)

		
		consumo = lectatual - lectanterior
		
		TotalAPagar = consumo * valorvatio

		print("El consumo es " + str(consumo) + " kwH")
		print("El total apagar es " + str(TotalAPagar) + " pesos")

		consumoclientes.append(consumo)

	
	for consumo in range(0,len(consumoclientes)):
		sumaconsumo += consumoclientes[consumo]

	consumoprom = sumaConsumo/cantclientes

	print("El consumo promedio es " + str(consumoprom) + " kwH")
