# #### Obtener un valor con una clave
# Puedes acceder a los valores en un diccionario proporcionando la clave:

alturas_edificios = {
    "Burj Khalifa": 828,
    "Torre de Shanghái": 632,
    "Abraj Al Bait": 601,
    "Ping An": 599,
    "Lotte World Tower": 554.5,
    "One World Trade": 541.3
}
print(alturas_edificios["Burj Khalifa"])  # Imprime 828
print(alturas_edificios["Ping An"])       # Imprime 599

elementos_zodiaco = {
    "agua": ["Cáncer", "Escorpio", "Piscis"],
    "fuego": ["Aries", "Leo", "Sagitario"],
    "tierra": ["Tauro", "Virgo", "Capricornio"],
    "aire": ["Géminis", "Libra", "Acuario"]
}
print(elementos_zodiaco["tierra"])
print(elementos_zodiaco["fuego"])

# ## Obtener una clave no válida de forma segura
clave_a_buscar = "Landmark 81"

if clave_a_buscar in alturas_edificios:
    print(alturas_edificios[clave_a_buscar])
else:
    print(f"{clave_a_buscar} no se encuentra en el diccionario.")

# Agregar y verificar una nueva clave
elementos_zodiaco["energía"] = "No es un elemento del zodiaco"

if "energía" in elementos_zodiaco:
    print(elementos_zodiaco["energía"])

# ## Obtener una clave con .get()
print(alturas_edificios.get("Torre de Shanghái"))  # devuelve 632
print(alturas_edificios.get("Mi Casa"))            # devuelve None

usuarios_id = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384
}
print(usuarios_id.get("teraCoder"))  # 100019

id_tc = usuarios_id.get("teraCoder", 1000)
print(id_tc)

id_stack = usuarios_id.get("superStackSmash", 100000)
print(id_stack)

# ## Eliminar una clave
rifa = {
    223842: "Osito de peluche",
    872921: "Boletos para concierto",
    320291: "Canasta de regalo",
    412123: "Collar",
    298787: "Máquina de pasta"
}
print(rifa.pop(320291, "Sin premio"))  # Canasta de regalo
print(rifa)
print(rifa.pop(100000, "Sin premio"))  # Sin premio
print(rifa)
print(rifa.pop(872921, "Sin premio"))  # Boletos para concierto
print(rifa)

# ## Usar pop para sumar puntos de salud
objetos_disponibles = {
    "poción de salud": 10,
    "pastel curativo": 5,
    "elixir verde": 20,
    "sándwich de fuerza": 25,
    "granos de resistencia": 15,
    "estofado poderoso": 30
}
puntos_salud = 20

puntos_salud += objetos_disponibles.pop("granos de resistencia", 0)
puntos_salud += objetos_disponibles.pop("estofado poderoso", 0)
puntos_salud += objetos_disponibles.pop("pan místico", 0)

print(objetos_disponibles)
print(puntos_salud)

# ## Obtener todas las claves
notas = {
    "Grace": [80, 72, 90],
    "Jeffrey": [88, 68, 81],
    "Sylvia": [80, 82, 84],
    "Pedro": [98, 96, 95],
    "Martin": [78, 80, 78],
    "Dina": [64, 60, 75]
}
print(list(notas))

for estudiante in notas.keys():
    print(estudiante)

lecciones = {
    "funciones": 10,
    "sintaxis": 13,
    "flujo de control": 15,
    "bucles": 22,
    "listas": 19,
    "clases": 18,
    "diccionarios": 18
}

print(usuarios_id.keys())
print(lecciones.keys())

# ## Obtener todos los valores
for lista_notas in notas.values():
    print(lista_notas)

total_ejercicios = sum(lecciones.values())
print(total_ejercicios)

# ## Obtener todos los pares clave-valor
marcas_mas_grandes = {
    "Apple": 184,
    "Google": 141.7,
    "Microsoft": 80,
    "Coca-Cola": 69.7,
    "Amazon": 64.8
}

for empresa, valor in marcas_mas_grandes.items():
    print(f"{empresa} tiene un valor de {valor} mil millones de dólares.")

porc_mujeres_ocupacion = {
    "CEO": 28,
    "Gerente de Ingeniería": 9,
    "Farmacéutico/a": 58,
    "Médico/a": 40,
    "Abogado/a": 37,
    "Ingeniero/a Aeroespacial": 9
}

for ocupacion, porcentaje in porc_mujeres_ocupacion.items():
    print(f"Las mujeres representan el {porcentaje}% de los/as {ocupacion}s.")