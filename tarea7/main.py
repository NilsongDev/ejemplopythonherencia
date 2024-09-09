while True:
    try:
        # Pedimos al usuario que ingrese su edad
        edad = int(input("Por favor, ingrese su edad: "))
        
        # Si es mayor o igual a 18, es adulto
        if edad >= 18:
            print("Es un adulto.")
        else:
            print("No es un adulto.")
        break  # Salimos del bucle si todo fue correcto

    except ValueError:
        # Capturamos la excepción si el usuario no ingresa un número entero
        print("Error: Por favor, ingrese un número válido para la edad.")
