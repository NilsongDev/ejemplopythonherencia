# Definición de las clases base
class A:
    def __init__(self):
        print("Pertenezco a la clase A")
    
    def metodo_a(self):
        print("Método heredado de A")

class B:
    def __init__(self):
        print("Clase B")
    
    def metodo_b(self):
        print("Método heredado de B")

# Definición de la clase C con herencia múltiple de A y B
class C(A, B):
    def __init__(self):
        # Llamar al constructor de la clase B para mostrar "Clase B"
        B.__init__(self)
        # Llamar al constructor de la clase A para mostrar "Pertenezco a la clase A"
        A.__init__(self)
    
    def metodo_c(self):
        print("Método de clase C")

# Crear una instancia de la clase C
objeto_c = C()

# Acceder a los métodos de la instancia
objeto_c.metodo_a()  # Método heredado de A
objeto_c.metodo_b()  # Método heredado de B
objeto_c.metodo_c()  # Método de clase C
