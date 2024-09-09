def reemplazar_y_contar(filename, texto_antiguo, texto_nuevo):
    # Leer el contenido del archivo
    with open(filename, 'r') as file:
        contenido = file.read()
    
    # Contar cuántas veces aparece el texto antiguo
    cantidad_reemplazos = contenido.count(texto_antiguo)
    
    # Reemplazar el texto antiguo por el nuevo
    contenido = contenido.replace(texto_antiguo, texto_nuevo)
    
    # Escribir el contenido actualizado en el archivo
    with open(filename, 'w') as file:
        file.write(contenido)
    
    return cantidad_reemplazos

# Nombre del archivo
filename = "informacion.dat"

# Llamar a la función para reemplazar "Información" por "Procesamiento"
reemplazos = reemplazar_y_contar(filename, "Información", "Procesamiento")

# Mostrar el número de reemplazos realizados
print(f"Se realizaron: {reemplazos} reemplazos")

# Leer y mostrar el contenido del archivo actualizado
with open(filename, 'r') as file:
    print("\nEl contenido del archivo es:")
    print(file.read())
