# Diccionario vacío
aeronave = {}

# Diccionario con elementos
aeronave = {
    "modelo": "Boeing 787-9",
    "envergadura": 60.17,  # metros
    "longitud": 62.81,     # metros
    "mtow": 254000,        # kg
    "velocidad_max": 954   # km/h
}
aeronave["altura"] = 16.9
print(f"Modelo: {aeronave["modelo"]}, mide {aeronave["longitud"]} metros")

# Diccionario con diferentes tipos de datos como valores
vuelo = {
    "numero": "AA123",
    "origen": "KLAX",
    "destino": "KJFK",
    "distancia": 3983,
    "a_tiempo": True,
    "tripulacion": ["Capitán Smith", "F/O Johnson", "F/E Williams"]
}

# Imprimir el origen, el destino y la tripulación
print(f"El vuelo tiene como origen {vuelo["origen"]} y vuela hasta {vuelo["destino"]}, con estos miembros de tripulación: ")
for n in vuelo["tripulacion"]:
    print(n)

# Creación con dict()
motor = dict(fabricante="GE", modelo="GE9X", empuje=470, bypass_ratio=10)
