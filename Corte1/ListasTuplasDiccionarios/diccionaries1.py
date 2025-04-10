# Diccionario de sensores (habitaciones y temperatura)
sensores = {"sala": 21, "cocina": 23, "dormitorio": 20, "despensa": 22}
print(sensores)

# Diccionario de cámaras por ubicación
num_camaras = {"patio trasero": 6, "garaje": 2, "entrada": 1}
print(num_camaras)

# Traducciones élfico ↔ español
traducciones = {"montaña": "orod", "pan": "bass", "amigo": "mellon", "caballo": "roch"}
print(traducciones)

# Diccionario con claves que ahora son tuplas (válidas e inmutables)
potencias = {(1, 2, 4, 8, 16): 2, (1, 3, 9, 27, 81): 3}
print(potencias)

# Diccionario con listas como valores
hijos = {
    "von Trapp": ["Johannes", "Rosmarie", "Eleonore"],
    "Corleone": ["Sonny", "Fredo", "Michael"]
}
print(hijos)

# Diccionario vacío
diccionario_vacio = {}
print(diccionario_vacio)

# Menú de un café
menu = {"avena": 3, "tostada de aguacate": 6, "jugo de zanahoria": 5, "muffin de arándanos": 2}
print("Antes:", menu)
menu["cheesecake"] = 8  # Agregamos un nuevo ítem
print("Después:", menu)

# Sobrescribimos todo el diccionario con un nuevo valor
animales_en_zoo = {"dinosaurios": 0}
animales_en_zoo = {"caballos": 2}
print(animales_en_zoo)

# Agregar múltiples habitaciones al diccionario de sensores
sensores = {"sala": 21, "cocina": 23, "dormitorio": 20}
print("Antes:", sensores)
sensores.update({"despensa": 22, "cuarto de invitados": 25, "patio": 34})
print("Después:", sensores)

# Diccionario de usuarios con sus ID
usuarios = {"teraCoder": 9018293, "proProgramador": 119238}
print("Antes:", usuarios)
usuarios.update({"elBucleador": 138475, "reinaDeCadenas": 85739})
print("Después:", usuarios)

# Actualización de valores en el menú
menu = {"avena": 3, "tostada de aguacate": 6, "jugo de zanahoria": 5, "muffin de arándanos": 2}
print("Antes:", menu)
menu["avena"] = 5  # Se modifica el valor de avena
print("Después:", menu)

# Diccionario de ganadores del Oscar
ganadores_oscar = {"Mejor Película": "La La Land","Mejor Actor": "Casey Affleck","Mejor Actriz": "Emma Stone","Película Animada": "Zootopia"}
print("Antes:", ganadores_oscar)
print()
ganadores_oscar.update({"Actriz de Reparto": "Viola Davis"})
print("Después (1):", ganadores_oscar)
print()
ganadores_oscar["Mejor Película"] = "Moonlight"
print("Después (2):", ganadores_oscar)

# Crear diccionario con comprensión (combinando nombres y alturas)
nombres = ['Jenny', 'Alexus', 'Sam', 'Grace']
alturas = [61, 70, 67, 64]

# Mostramos el resultado del zip como lista
print("Pares nombre-altura:", list(zip(nombres, alturas)))

# Comprehensión de diccionario
estudiantes = {nombre: altura for nombre, altura in zip(nombres, alturas)}
print("Diccionario de estudiantes:", estudiantes)

# Otro ejemplo: bebidas y cafeína
bebidas = ["espresso", "chai", "descafeinado", "filtrado"]
cafeina = [64, 40, 0, 120]
print("Bebidas y cafeína:", list(zip(bebidas, cafeina)))

bebidas_cafeina = {bebida: cantidad for bebida, cantidad in zip(bebidas, cafeina)}
print("Diccionario de cafeína:", bebidas_cafeina)

# Diccionario de canciones reproducidas
canciones = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
reproducciones = [78, 29, 44, 21, 89, 5]

# Comprehensión de diccionario
repro = {cancion: cantidad for cancion, cantidad in zip(canciones, reproducciones)}
print("Reproducciones:", repro)

# Actualización de canciones
repro.update({"Purple Haze": 1})  # Nueva canción
repro.update({"Respect": 94})    # Se actualiza el número de reproducciones
print("Después de actualizar:", repro)

# Biblioteca musical con listas de reproducción
biblioteca = {"Las Mejores Canciones": repro, "Domingos Tranquilos": {}}
print("Biblioteca musical:", biblioteca)