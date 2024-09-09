# Nombre del archivo
filename = "informacion.dat"

# Contenido a agregar al archivo
contenido_agregar = """Hola Mundo
Este en una nueva línea en el archivo
agregando la segunda línea del archivo
finalizando la línea agregada"""

# Abrir el archivo en modo append para agregar contenido
with open(filename, 'a') as file:
    file.write("\n" + contenido_agregar)  # Agregar un salto de línea antes del nuevo contenido

print(f"Contenido agregado a '{filename}' con éxito.")
