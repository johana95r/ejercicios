num = int(input("Ingrese un numero"))

contador = 0
suma = 0

for numero in range (1,num+1):
    print (numero)
    if (num%numero == 0):
        suma += numero
        contador +=1

print ("Hay: " + str (contador) + "submultiplos")
Promedio = contador/suma
print ("Promedio: " + str (Promedio))
