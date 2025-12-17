from Padre_Animales import Animal
class Pez(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        print(f"{self.nombre} nada en el agua.")
    def comunicarse(self):
        print(f"{self.nombre} usa vibraciones y colores para comunicarse.")