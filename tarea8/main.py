import os

# Nombre del archivo
filename = "informacion.dat"

# Verificar si el archivo ya existe
if os.path.exists(filename):
    print(f"El archivo '{filename}' ya existe.")
else:
    # Crear y escribir contenido en el archivo si no existe
    with open(filename, 'w') as file:
        file.write("Datos de información en la línea 1\n")
        file.write("Datos de información en la línea 2\n")
        file.write("Datos de información en la línea 3\n")
        file.write("Datos de información en la línea 4\n")
        file.write("Datos de información en la línea 5\n")
    print(f"El archivo '{filename}' ha sido creado con éxito.")
