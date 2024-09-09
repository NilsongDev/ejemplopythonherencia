# clases base
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

# clase C con herencia múltiple de A y B
class C(A, B):
    def __init__(self):
        
        B.__init__(self)
      
        A.__init__(self)
    
    def metodo_c(self):
        print("Método de clase C")

# Crear una instancia de la clase C
objeto_c = C()

# Acceder a los métodos de la instancia
objeto_c.metodo_a()  
objeto_c.metodo_b()  
objeto_c.metodo_c()  
