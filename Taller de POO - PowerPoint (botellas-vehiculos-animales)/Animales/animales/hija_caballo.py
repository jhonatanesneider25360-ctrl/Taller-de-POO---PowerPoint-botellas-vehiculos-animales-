from Padre_Animales import Animal
class Caballo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        print(f" {self.nombre} galopa por el campo.")
    def comunicarse(self):
        print(f" {self.nombre} relincha para comunicarse.")