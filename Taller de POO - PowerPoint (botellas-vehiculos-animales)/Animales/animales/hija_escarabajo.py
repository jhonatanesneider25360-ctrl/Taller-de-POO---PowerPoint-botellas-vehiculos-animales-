from Padre_Animales import Animal
class Escarabajo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        print(f" {self.nombre} camina o vuela corto distancia.")
    def adaptacion(self):
        print(f" {self.nombre} tiene exoesqueleto para protegerse.")