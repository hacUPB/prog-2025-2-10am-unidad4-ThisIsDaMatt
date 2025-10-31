'''
Generar una lista con 100 numeros aleatorios entre 100 y 1000 (hecho)
Calcular el promedio de los valores de la lista
Calcular el mayor y el menor de los numeros
'''
import random
numeros = []

for i in range(100):
    aleatorio = random.randint(100, 1000)
    numeros.append(aleatorio)
print(numeros)

suma = 0
for i in numeros:
    suma += i

# for i in range(len(numeros))
#   suma += numeros[i]

prom = suma / len(numeros)
print(f"Promedio = {prom}")

mayor = max(numeros)
menor = min(numeros)

print(mayor)
print(menor)