from Padre_Animales import Animal
class Pato(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        print(f" {self.nombre} nada y vuela.")
    def comunicarse(self):
        print(f" {self.nombre} hace 'cuac cuac'.")