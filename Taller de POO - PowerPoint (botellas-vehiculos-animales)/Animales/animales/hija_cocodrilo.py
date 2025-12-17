from Padre_Animales import Animal
class Cocodrilo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        print(f" {self.nombre} se arrastra o nada en el agua.")
    def alimentarse(self):
        print(f" {self.nombre} caza presas en el agua.")