usuarios = {'001': 'Marca', '002': 'Mónica', '003': 'Jacob'}
id_usuario = '004'

try:
    # Intentamos acceder al valor de la clave '004'
    print(usuarios[id_usuario])
except KeyError:
    # Si se produce un KeyError, mostramos el mensaje e insertamos la clave
    print(f"La clave {id_usuario} no está en el diccionario. Agregando clave...")
    usuarios[id_usuario] = "Ninguno"

# Imprimimos el diccionario actualizado
print(usuarios)
