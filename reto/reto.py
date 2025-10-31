import csv, os
import matplotlib.pyplot as plt

while True:
    print("=================================================")
    print("Bienvenido al procesador de archivos")
    print("=================================================")
    print("Elija una opción:")
    print("=================================================")
    print("A. Listar archivos en la ruta o ingresar una ruta")
    print("B. Procesar archivo .txt")
    print("C. Procesar archivo .csv")
    print("Q. Salir")
    print("=================================================")

    caso = input("Ingrese su selección: ")
    caso = caso.upper()

    match caso:
        case "A":
            print("===============================")
            print("Ha seleccionado listar archivos")
            print("===============================")
            print("Elija una opción:")
            print("===============================")
            print("1. Buscar en la carpeta actual")
            print("2. Ingresar ruta para buscar")
            print("===============================")

            opcion_a = input("Ingrese su selección: ")
            opcion_a = opcion_a.upper()

            if opcion_a == "1":
                ruta = "."
            else:
                ruta = input("Ingrese la ruta: ")
            
            try:
                archivos = os.listdir(ruta)
                
                txts = []
                csvs = []

                for archivo in archivos:
                    if archivo.endswith(".txt"):
                        txts.append(archivo)
                    elif archivo.endswith(".csv"):
                        csvs.append(archivo)
                
                print("===============================")
                print("Archivos .txt encontrados:")
                print("===============================")
                if txts:
                    for i, f in enumerate(txts, 1):
                        print(f"{i}. {f}")
                else:
                    print("No se encontraron archivos .txt")
                print("===============================")
                print("Archivos .csv encontrados:")
                print("===============================")
                if csv:
                    for i, f in enumerate(csvs, 1):
                        print(f"{i}. {f}")
                else:
                    print("No se encontraron archivos .csv")

            except:
                print("No hay archivos .csv")

        case "B":
            print("================================================")
            print("Ha seleccionado procesar .txt")
            print("================================================")
            print("Elija una opción:")
            print("================================================")
            print("1. Contar palabras y caracteres")
            print("2. Reemplazar palabras")
            print("3. Generar histograma de ocurrencias de vocales")
            print("================================================")

            opcion_b = input("Ingrese su selección: ")
            opcion_b = opcion_b.upper()

            match opcion_b:
                case "1":
                    print("========================")
                    print("Palabras y caracteres")
                    print("========================")
                    print("Contenido de la carpeta:")
                    print("========================")
                    archivos = os.listdir(".")
                    archivos_txt = []

                    for f in archivos:
                        if f.endswith(".txt"):
                            archivos_txt.append(f)
                    
                    if not archivos_txt:
                        print("No se encontraron archivos .txt")
                    else:
                        for i, f in enumerate(archivos_txt, 1):
                            print(f"{i}. {f}")

                        
                        num = int(input("Selecciona un archivo: "))
                        archivo = archivos_txt[num - 1]

                        with open(archivo, "r", encoding="utf-8") as f:
                            contenido = f.read()

                        print("========================================")
                        print(f"Archivo: {archivo}")
                        print("========================================")
                        print(f"# de Caracteres: {len(contenido)}")
                        print(f"# de Caracteres sin Espacios: {len(contenido.replace(' ',''))}")
                        print(f"# de Palabras: {len(contenido.split())}")
                        print("========================================")

                case "2":
                    print("===================")
                    print("Reemplazar palabras")
                    print("===================")

                    archivos = os.listdir(".")
                    archivos_txt = []

                    for f in archivos:
                        if f.endswith(".txt"):
                            archivos_txt.append(f)

                    if not archivos_txt:
                        print("No se encontraron archivos .txt")
                    else:
                        for i, f in enumerate(archivos_txt, 1):
                            print(f"{i}. {f}")

                        num = int(input("Selecciona un archivo: "))
                        archivo = archivos_txt[num - 1]

                        with open(archivo, "r", encoding="utf-8") as f:
                            contenido = f.read()

                        print("===================")
                        print("Contenido original: ")
                        print("===================")
                        print(contenido)
                        print("===================")

                        reemplazada = input("Ingrese la palabra que desea reemplazar: ")
                        nueva = input("Ingrese la palabra nueva: ")

                        nuevo_contenido = contenido.replace(reemplazada, nueva)

                        print("========================")
                        print("Archivo .txt modificado:")
                        print("========================")
                        print(nuevo_contenido)
                        print("========================")

                        guardar = input("Desea guardar este nuevo contenido? S/N: ")
                        guardar = guardar.upper()

                        if guardar == "S":
                            with open(archivo, "w", encoding="utf-8") as f:
                                f.write(nuevo_contenido)
                            print("El archivo se ha guardado, revisa los cambios.")
                        else:
                            print("Cambios no guardados.")
                
                case "3":
                    print("====================================")
                    print("Histograma de ocurrencias de vocales")
                    print("====================================")
                    archivos = os.listdir(".")
                    archivos_txt = []

                    for f in archivos:
                        if f.endswith(".txt"):
                            archivos_txt.append(f)
                    
                    if not archivos_txt:
                        print("No se encontraron archivos .txt")
                    else:
                        for i, f in enumerate(archivos_txt, 1):
                            print(f"{i}. {f}")

                        num = int(input("Selecciona un archivo: "))
                        archivo = archivos_txt[num - 1]

                        with open(archivo, "r", encoding="utf-8") as f:
                            contenido = f.read()
                        
                        contenido_low = contenido.lower()
                        
                        vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
                        
                        for letra in contenido_low:
                            if letra in vocales:
                                vocales[letra] += 1
                        
                        print("==============================================")
                        print(f"Histograma de vocales - Archivo: {archivo}")
                        print("==============================================")
                        print("Generando grafico con MatPlotLib...")        
                        print("==============================================")
                        print(f"Total de vocales: {sum(vocales.values())}")
                        print("==============================================")

                        vocales_list = list(vocales.keys())
                        cantidades = list(vocales.values())
                        
                        plt.figure(figsize=(10, 6))
                        plt.bar(vocales_list, cantidades, color='skyblue', edgecolor='black', width=0.6)
                        plt.xlabel('Vocales', fontsize=12)
                        plt.ylabel('Cantidad de Ocurrencias', fontsize=12)
                        plt.title(f'Histograma de Vocales - {archivo}', fontsize=14, fontweight='bold')
                        plt.grid(axis='y', alpha=0.3, linestyle='--')
                        
                        for i, v in enumerate(cantidades):
                            plt.text(i, v + max(cantidades) * 0.02, str(v), ha='center', fontweight='bold')
                        
                        plt.tight_layout()
                        plt.show()
        case "C":
            print("======================================")
            print("Ha seleccionado procesar .csv")
            print("======================================")
            print("Elija una opción:")
            print("======================================")
            print("1. Mostrar 15 primeras filas")
            print("2. Calcular estadísticas")
            print("3. Graficar columna completa con datos")
            print("======================================")

            opcion_c = input("Ingrese su selección: ")
            opcion_c = opcion_c.upper()

            match opcion_c:
                case "1":
                    print("=========================")
                    print("Mostrar 15 primeras filas")
                    print("=========================")
                    archivos = os.listdir(".")
                    archivos_csv = []

                    for f in archivos:
                        if f.endswith(".csv"):
                            archivos_csv.append(f)

                    if not archivos_csv:
                        print("No se encontraron archivos .csv")
                    else:
                        for i, f in enumerate(archivos_csv, 1):
                            print(f"{i}. {f}")

                        num = int(input("Selecciona un archivo: "))
                        archivo = archivos_csv[num - 1]

                        with open(archivo, "r", encoding="utf-8") as f:
                            lector = csv.reader(f)

                            print("=============================")
                            print("Primeras 15 filas del archivo")
                            print("=============================")

                            for i, fila in enumerate(lector):
                                if i < 15:
                                    print(f"Fila {i+1}: {fila}")
                                else:
                                    break
                                
                            print("=============================")
                
                case "2":
                    print("=================================")
                    print("Calcular estadisticas del archivo")
                    print("=================================")
                    archivos = os.listdir(".")
                    archivos_csv = []

                    for f in archivos:
                        if f.endswith(".csv"):
                            archivos_csv.append(f)

                    if not archivos_csv:
                        print("No se encontraron archivos .csv")
                    else:
                        for i, f in enumerate(archivos_csv, 1):
                            print(f"{i}. {f}")
                        
                        num = int(input("Selecciona un archivo: "))
                        archivo = archivos_csv[num - 1]

                        with open(archivo, "r", encoding="utf-8") as f:
                            lector = csv.reader(f)
                            filas = list(lector)

                            print("=====================")
                            print("Columnas disponibles:")
                            print("=====================")
                            encabezados = filas[0]
                            for i, col in enumerate(encabezados):
                                print(f"{i}. {col}")
                            print("=====================")
                            
                            # Seleccionar columna
                            n_columna = int(input("Seleccione el número de columna: "))
                            nom_columna = encabezados[n_columna]

                            datos = []
                            for fila in filas[1:]:
                                if n_columna < len(fila):
                                    valor = fila[n_columna].strip()
                                    if valor.replace('.', '', 1).replace('-', '', 1).isdigit():
                                        datos.append(float(valor))

                            if datos:
                                n_datos = len(datos)
                                promedio = sum(datos) / n_datos
                                maximo = max(datos)
                                minimo = min(datos)
                                
                                datos_ordenados = sorted(datos)
                                if n_datos % 2 == 0:
                                    mediana = (datos_ordenados[n_datos//2 - 1] + datos_ordenados[n_datos//2]) / 2
                                else:
                                    mediana = datos_ordenados[n_datos//2]
                                
                                # Mostrar resultados
                                print("=================================")
                                print(f"Estadísticas de: {n_columna}")
                                print("=================================")
                                print(f"Número de datos: {n_datos}")
                                print(f"Promedio: {promedio:.2f}")
                                print(f"Mediana: {mediana:.2f}")
                                print(f"Valor máximo: {maximo:.2f}")
                                print(f"Valor mínimo: {minimo:.2f}")
                                print("=================================")
                            else:
                                print("No se encontraron datos numéricos en la columna seleccionada")
                
                case "3":
                    print("==========================")
                    print("Graficar columna con datos")
                    print("==========================")
                    archivos = os.listdir(".")
                    archivos_csv = []

                    for f in archivos:
                        if f.endswith(".csv"):
                            archivos_csv.append(f)

                    if not archivos_csv:
                        print("No se encontraron archivos .csv")
                    else:
                        for i, f in enumerate(archivos_csv, 1):
                            print(f"{i}. {f}")
                        
                        num = int(input("Selecciona un archivo: "))
                        archivo = archivos_csv[num - 1]

                        with open(archivo, "r", encoding="utf-8") as f:
                            lector = csv.reader(f)
                            filas = list(lector)

                        if not filas:
                            print("El archivo parece estar vacio, intente nuevamente")
                        else:
                            encabezados = filas[0]
                            print("=====================")
                            print("Columnas disponibles:")
                            print("=====================")
                            for i, col in enumerate(encabezados):
                                print(f"{i}. {col}")
                            print("=====================")

                            n_columna = int(input("Seleccione el número de columna a graficar: "))
                            nombre_columna = encabezados[n_columna]

                            datos = []
                            indices = []
                            for ind, fila in enumerate(filas[1:], start=1):
                                if n_columna < len(fila):
                                    valor = fila[n_columna].strip().replace(',', '.')
                                    if valor and valor.replace('.', '', 1).replace('-', '', 1).isdigit():
                                        datos.append(float(valor))
                                        indices.append(ind)

                            if datos:
                                plt.figure(figsize=(10, 6))
                                plt.scatter(indices, datos, color='#1f77b4', edgecolor='black', alpha=0.8)
                                plt.title(f'Gráfica de dispersión - {nombre_columna}', fontsize=14, fontweight='bold')
                                plt.xlabel('Número de fila', fontsize=12)
                                plt.ylabel(nombre_columna, fontsize=12)
                                plt.grid(alpha=0.3, linestyle='--')
                                plt.tight_layout()
                                plt.show()

                                print("==============================================")
                                print("Seleccione una columna para gráficar en barras")
                                print("==============================================")
                                
                                col_bar = int(input("Seleccione el número de columna: "))
                                nombre_columna_bar = encabezados[col_bar]

                                valores_bar = []
                                for fila in filas[1:]:
                                    if col_bar < len(fila):
                                        valor = fila[col_bar].strip().replace(',', '.')
                                        if valor and valor.replace('.', '', 1).replace('-', '', 1).isdigit():
                                            valores_bar.append(float(valor))

                                if valores_bar:
                                    bins = 8
                                    vmin = min(valores_bar)
                                    vmax = max(valores_bar)
                                    ancho = (vmax - vmin) / bins
                                    
                                    cuentas = [0] * bins
                                    etiquetas = []
                                    
                                    for i in range(bins):
                                        inicio = vmin + i * ancho
                                        fin = vmin + (i + 1) * ancho
                                        etiquetas.append(f"{inicio:.1f}-{fin:.1f}")
                                    
                                    for valor in valores_bar:
                                        if valor == vmax:
                                            cuentas[-1] += 1
                                        else:
                                            indice = int((valor - vmin) / ancho)
                                            if indice >= bins:
                                                indice = bins - 1
                                            cuentas[indice] += 1
                                    
                                    plt.figure(figsize=(10, 6))
                                    plt.bar(range(bins), cuentas, color='#2ca02c', edgecolor='black')
                                    plt.xticks(range(bins), etiquetas, rotation=45, ha='right')
                                    plt.title(f'Histograma - {nombre_columna_bar}', fontsize=14, fontweight='bold')
                                    plt.xlabel(nombre_columna_bar, fontsize=12)
                                    plt.ylabel('Frecuencia', fontsize=12)
                                    plt.grid(axis='y', alpha=0.3, linestyle='--')
                                    plt.tight_layout()
                                    plt.show()
                                else:
                                    print("No se encontraron datos numéricos")
                            else:
                                print("No se encontraron datos numéricos")

        case "Q":
            print("Saliendo del programa...")
            break

        case _:
            print("Opción incorrecta, ingrese una opción de nuevo.")