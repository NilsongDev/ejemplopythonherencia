import os

# Nombre del archivo
filename = "informacion.dat"

# Función para crear el archivo si no existe
def crear_archivo():
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            file.write("Datos de información en la línea 1\n")
            file.write("Datos de información en la línea 2\n")
            file.write("Datos de información en la línea 3\n")
            file.write("Datos de información en la línea 4\n")
            file.write("Datos de información en la línea 5\n")
        print(f"El archivo '{filename}' ha sido creado con éxito.")
    else:
        print(f"El archivo '{filename}' ya existe, ha sido creado previamente.")

# Función para leer el contenido del archivo
def leer_archivo():
    if os.path.exists(filename):
        print(f"El archivo '{filename}' ya existe, ha sido creado previamente")
        with open(filename, 'r') as file:
            contenido = file.read()
            print(contenido)
    else:
        print(f"El archivo '{filename}' no existe.")

# Llamada a las funciones
crear_archivo()  # Se crea el archivo si no existe
leer_archivo()   # Se lee el contenido del archivo
