print("########## Listas #########")

mi_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']

print(mi_lista)
print(type(mi_lista))               # Muestra el tipo de estructura (list)
print(mi_lista[2])                  # Accede al tercer elemento

print("Tamaño de mi_lista: ", len(mi_lista))  # Tamaño de la lista
print(mi_lista[0:2])               # Elementos del índice 0 al 1
print(mi_lista[:2])                # Otra forma de hacer lo mismo

mi_lista.append('Blanco')         # Agrega elemento al final
print(mi_lista)

mi_lista.insert(3, 'Negro')       # Inserta 'Negro' en el índice 3
print(mi_lista)

mi_lista.extend(['Marrón', 'Gris'])  # Añade varios elementos al final
print(mi_lista)

print(mi_lista.index('Azul'))     # Devuelve el índice de 'Azul'

# mi_lista.remove('Magenta')     # Esto daría error si no existe
mi_lista.remove('Marrón')         # Elimina el primer 'Marrón' que encuentra
print(mi_lista)

mi_lista.insert(8, 'Marrón')      # Inserta 'Marrón' en el índice 8
print(mi_lista)

print("Elemento eliminado con pop():", mi_lista.pop())  # Elimina el último
tamaño = len(mi_lista)
print("Tamaño final = ", tamaño)

mi_lista_3 = mi_lista * 3         # Repite la lista 3 veces
print("mi_lista_3: ", mi_lista_3)

print("Ordenar lista alfabéticamente:")
mi_lista.sort()                   # Ordena la lista alfabéticamente
print(mi_lista)

# Lista de números
mi_lista_numeros = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Ordenando mi_lista_numeros: ")
mi_lista_numeros.sort()
print(mi_lista_numeros)

# Ordenando de mayor a menor
mi_lista_numeros.sort(reverse=True)
print("De mayor a menor: ", mi_lista_numeros)

## TUPLAS ##

# Las tuplas son estructuras similares a listas, pero son inmutables


print("########## TUPLAS #########")


# Convertir lista a tupla
mi_tupla = tuple(mi_lista)
print("mi_tupla: ", mi_tupla)

print(mi_tupla[0])
print(mi_tupla[2])

# Verificar si un elemento existe en la tupla
print('Rojo' in mi_tupla)
print("Cantidad de veces que aparece 'Rojo':", mi_tupla.count('Rojo'))

# Tupla con un solo elemento (debe llevar coma para que sea tupla)
mi_tupla_unitaria = ('Blanco',)
print("Tupla unitaria:", mi_tupla_unitaria)

# Empaquetado de tupla (sin paréntesis)
mi_tupla = 'Gaspar', 5, 8, 1999
print("Tupla empaquetada:", mi_tupla)

# Desempaquetado de tupla
nombre, dia, mes, año = mi_tupla
print(nombre)
print(dia)
print(mes)
print(año)

print("Nombre:", nombre, "- Día:", dia, "- Mes:", mes, "- Año:", año)

# Convertir tupla en lista
mi_lista2 = list(mi_tupla)
print("Tupla convertida en lista:", mi_lista2)