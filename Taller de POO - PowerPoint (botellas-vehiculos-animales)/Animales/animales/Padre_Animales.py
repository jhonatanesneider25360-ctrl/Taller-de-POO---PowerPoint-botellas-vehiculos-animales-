class Animal:
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamaño = tamaño
        self.color = color

    def moverse(self):
        print(f"{self.nombre} se está moviendo.")
    def comunicarse(self):
        print(f"{self.nombre} está comunicándose.")
    def reproducirse(self):
        print(f"{self.nombre} está reproduciéndose.")
    def alimentarse(self):
        print(f"{self.nombre} está alimentándose.")
    def adaptacion(self):
        print(f"{self.nombre} tiene adaptaciones para su hábitat: {self.habitat}.")
    def instinto(self):
        print(f"{self.nombre} sigue sus instintos naturales.")
    def descanso(self):
        print(f"{self.nombre} está descansando.")
    def sueño(self):
        print(f"{self.nombre} está durmiendo.")
    def interaccion_social(self):
        print(f"{self.nombre} está interactuando socialmente.")
    def __str__(self):
        return f"{self.nombre} | Edad: {self.edad} | Hábitat: {self.habitat} | Dieta: {self.dieta}"