# Definir una excepción personalizada
class RangoSalarioError(Exception):
    def __init__(self, salario):
        self.salario = salario
        super().__init__(f"{salario} -> Salario no está definido en el rango (1000 a 2000)")

# Función para pedir el salario
def pedir_salario():
    try:
        salario = int(input("Ingrese el salario: "))
        
        # Comprobar si el salario está en el rango
        if salario < 1000 or salario > 2000:
            raise RangoSalarioError(salario)
        
        print(f"Salario válido: {salario}")
    
    except RangoSalarioError as e:
        # Mostrar el mensaje personalizado de la excepción
        print(e)

    except ValueError:
        print("Error: Debe ingresar un número entero válido para el salario.")

# Llamar a la función
pedir_salario()
