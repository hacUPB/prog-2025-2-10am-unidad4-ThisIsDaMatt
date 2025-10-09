aeronaves = [
    ("C172 Skyhawk", 30, 212),
    ("Airbus A320-200", 2300, 27200),
    ("Boeing 737-800", 3200, 26000),
    ("Airbus A380-800", 17400, 320000)
]

fases_vuelo = [
    ("Despegue", 1.2),
    ("Ascenso", 1.15),
    ("Crucero", 1.0),
    ("Descenso", 0.85),
    ("Aterrizaje", 0.9)
]

opciones = {"A": 0, "B": 1, "C": 2, "D": 3}

print("Listas usadas:")
print("Aeronaves:")
for aeronave in aeronaves:
    print(f"  {aeronave[0]} - Consumo: {aeronave[1]} kg/h, Capacidad: {aeronave[2]} kg")

print("Fases de vuelo:")
for fase, factor in fases_vuelo:
    print(f"  {fase} - Factor: {factor}")

print("Diccionarios usados:")
print("Opciones:")
for clave, valor in opciones.items():
    print(f"  {clave}: {valor}")