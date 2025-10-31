# Analisis del reto
Este archivo Markdown tiene la finalidad de explicar como se usaron los conceptos que aprendí en esta unidad, la unidad 4, 
los cuales no solo fueron utiles, sino fundamentales en la realizacion y programación de este reto
## Conceptos usados de las unidades
### Unidades pasadas
Las cosas que se usaron que no corresponden a esta unidad, sino a pasadas (pero que vale la pena recalcar) son: 
- Condicionales if, if not, else.
- Definir funciones para mejorar la legibilidad y la optimización del codigo.
- Bucles for y while para el funcionamiento de todo el flujo y del menú.
- Funciones upper() and lower() para manejar mas facil selecciones del usuario y datos de archivos.
### Unidad 4
Lo que corresponde a la unidad 4, se usó:
- Listas en todo el flujo, se necesitaban añadir listas vacias para los archivos csv y txt que el modulo os los encontrara-
- Se usa la funcion append() para añadirlos a las listas, las cuales mostrarian los archivos encontrados y dejaría al usuario elegir el archivo a analizar.
- Se usaron ciclos for en diversas listas para navegar por ellas y mostrar en consola su contenido, navegando elemento por elemento.
- Se usaron tambien funciones como enumerate() para enumerar elementos de la lista y mostrarlos en consola mas limpiamente-
- Se usó split() para convertir strings de texto a listas, lo que me fue sumamente util para contar palabras en una archivo, porque separa
el string palabra por palabra.
- Se usó len() para contar tanto caracteres en el archivo como elementos de la lista, permitiendome contar, respectivamente, caracteres y palabras.
- Se usó tambien la función values() para retornar los valores de un diccionario.
- Ademas, se usó la funcion keys() para retornar las claves de los diccionarios.
### Unidad 5
Los elementos aprendidos en la unidad 5 usados fueron:
- Gestión de recursos con la instrucción with, para no tener que abrir y cerrar los archivos constantemente.
- Se usó la función open() junto a with para abrir los archivos necesarios, usando entre "r" para leer y "w" para escribir, y el encoding utf-8
para evitar problemas con los caracteres.
- Se usó la función read() para leer el contenido de los archivos y "dejarlos" como una variable que se usaría despues.
- Además, se uso la función write() para escribir y sobreescribir el contenido nuevo que el usuario seleccionó.
- Se usó tambien la función replace(), que permitió que el usuario, eligiendo una palabra a reemplazar y la nueva palabra, editara el texto.
- Se usó la función reader() con los archivos .csv para leerlos y analizarlos.
- Se usaron las librerias os y matplotlib, para navegar archivos y rutas y graficar datos, respectivamente.
