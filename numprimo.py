#Proceso numeroprimo
print( 'escriba numero' )
n=int(input())
i=2
while (i<n) and  (n % i != 0):
	i = i+1
if i == n: 
	print( 'El numero ' + str(n) +' es primo' )
else:
	print( 'El numero '+ str(n) +' no es primo')
