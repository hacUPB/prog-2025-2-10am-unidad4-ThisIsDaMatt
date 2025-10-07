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

print("=====================================================")
print("Ha entrado a la calculadora de Consumo de Combustible")
print("=====================================================")
print("A. Cessna 172 Skyhawk")
print("B. Airbus A320-200")
print("C. Boeing 737-800")
print("D. Airbus A380-800")
print("=======================")

caso_b = (input("Seleccione una aeronave: ")).upper()

if caso_b in opciones:
    nombre, consumo, capacidad = aeronaves[opciones[caso_b]]
    
    combustible = int(input("Ingrese el combustible en kg: "))
    tiempo = 0
    historia = []
    
    if combustible <= capacidad:
        print("Simulando fases de vuelo...")
        for fase, factor in fases_vuelo:
            if combustible <= 0:
                break

            tiempo += 1
            consumo_fase = consumo * factor
            combustible -= consumo_fase

            if combustible < 0:
                combustible = 0
            
            historia.append((tiempo, combustible))
            print(f"Hora {tiempo} ({fase}): Quedan {combustible} kg")
        
        print("========================================")
        print(f"El {nombre} voló durante {tiempo} horas.")
        print("========================================")
        
    else:
        print("Combustible excede la capacidad maxima. Intente una cantidad menor.")
else:
    print("Opción de aeronave invalida.")

