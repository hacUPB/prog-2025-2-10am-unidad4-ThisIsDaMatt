from modulos.mod_funciones import *

def main():
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
                listar_archivos()

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
                        contar_palabras_caracteres()
                    case "2":
                        reemplazar_palabras()
                    case "3":
                        histograma_vocales()

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
                        mostrar_15_filas()
                    case "2":
                        calcular_estadisticas()
                    case "3":
                        graficar_columna()

            case "Q":
                print("Saliendo del programa...")
                break

            case _:
                print("Opción incorrecta, ingrese una opción de nuevo.")

if __name__ == "__main__":
    main()