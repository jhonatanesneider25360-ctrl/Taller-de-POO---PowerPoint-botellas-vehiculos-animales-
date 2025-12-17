from padre import botella
from hija_1_plastico import Botella_Plastico
from hija_2_vidrio import Botella_Vidrio

class Base_Dts:
    def __init__(self):
        self.botellas = []

    def agregar(self, botella):
        self.botellas.append(botella)

    def listar(self):
        for i, b in enumerate(self.botellas):
            print(f"{i}: {b}")

    def actualizar(self, index, nueva_capacidad):
        if 0 <= index < len(self.botellas):
            self.botellas[index].capacidad = nueva_capacidad

bd = Base_Dts()
print("Porfavor elije una opcion y interactua con el programa. \n ")
while True:
    opcion = input("1. añadir botella de Vidrio\n2. añadir botella de Plástico\n3. Listar\n4. Actualizar\n5. Salir\nElige: ")

    if opcion == "1":
        capacidad = int(input("Capacidad (ml): "))
        forma = input("Forma: ")
        reutilizable = input("¿Es reutilizable? (Si/No): ")
        botella = Botella_Vidrio(capacidad, forma, reutilizable)
        bd.agregar(botella)
        print(" Botella creada.")

    elif opcion == "2":
        capacidad = int(input("Capacidad (ml): "))
        forma = input("Forma: ")
        reciclable = input("¿Es reciclable? (Si/No): ")
        botella = Botella_Plastico(capacidad, forma, reciclable)
        bd.agregar(botella)
        print("Botella creada.")

    elif opcion == "3":
        bd.listar()

    elif opcion == "4":
        index = int(input("Indice: "))
        nueva_capacidad = int(input("Nueva capacidad: "))
        bd.actualizar(index, nueva_capacidad)
        print("Capacidad actualizada.")

    elif opcion == "5":
        print("Adios..")
        break
    else:
        print(" Opción no válida. Inténtar de nuevo.")