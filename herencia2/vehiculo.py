# vehiculo.py (agregar a las clases)
import csv

class Vehiculo:
    def __init__(self, marca, modelo, numero_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.numero_ruedas = numero_ruedas

    def guardar_datos_csv(self):
        with open('vehiculos.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([str(self.__class__), str(self.__dict__)])

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, numero_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

class Particular(Automovil):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, numero_puestos):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.numero_puestos = numero_puestos

class Carga(Automovil):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, numero_ruedas, tipo):
        super().__init__(marca, modelo, numero_ruedas)
        self.tipo = tipo

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, numero_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, numero_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios

def leer_datos_csv():
    vehiculos = {'Particular': [], 'Carga': [], 'Bicicleta': [], 'Motocicleta': []}
    try:
        with open('vehiculos.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                tipo_vehiculo = row[0].split("'")[1]
                datos = eval(row[1])
                if tipo_vehiculo.endswith('Particular'):
                    vehiculos['Particular'].append(datos)
                elif tipo_vehiculo.endswith('Carga'):
                    vehiculos['Carga'].append(datos)
                elif tipo_vehiculo.endswith('Bicicleta'):
                    vehiculos['Bicicleta'].append(datos)
                elif tipo_vehiculo.endswith('Motocicleta'):
                    vehiculos['Motocicleta'].append(datos)
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

    return vehiculos

# main.py (agregar al final)
if __name__ == "__main__":
    particular = Particular("Ford", "Fiesta", "4", "180", "500", "5")
    carga = Carga("Daft Trucks", "G 38", "10", "120", "1000", "20000")
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    # Guardar datos
    for vehiculo in [particular, carga, bicicleta, motocicleta]:
        vehiculo.guardar_datos_csv()

    # Leer y mostrar datos
    vehiculos = leer_datos_csv()
    for tipo, datos in vehiculos.items():
        print(f"Lista de Vehiculos {tipo}")
        for dato in datos:
            print(dato)
