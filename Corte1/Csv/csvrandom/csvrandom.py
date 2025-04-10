import csv
import random

# Generar 10 números aleatorios entre 0 y 1
numeros = [[random.random()] for _ in range(10)]

# Guardar en un archivo CSV
with open('numeros_random.csv', 'w', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['numero'])  # Encabezado
    escritor.writerows(numeros)

# Leer y mostrar el contenido del archivo CSV
with open('numeros_random.csv', 'r') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)