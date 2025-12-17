from Padre_Animales import Animal
from hija_caballo import Caballo
from hija_cocodrilo  import Cocodrilo
from hija_pez import Pez
from hija_escarabajo import Escarabajo
from hija_pato import Pato

class Gestor_Animales:
    def __init__(self):
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)
        print(f" {animal.nombre} ha sido agregado al sistema.")

    def listar_animales(self):
        if not self.animales:
            print(" No hay animales registrados.")
            return
        print("\n" + "="*50)
        print(" LISTA DE ANIMALES ")
        print("="*50)
        for i, animal in enumerate(self.animales, 1):
            print(f"{i}. {animal}")

    def ejecutar_metodo(self, indice, metodo):
        if 1 <= indice <= len(self.animales):
            animal = self.animales[indice - 1]
            if hasattr(animal, metodo):
                getattr(animal, metodo)()
            else:
                print(f" El método '{metodo}' no existe para {animal.nombre}.")
        else:
            print("Número de animal inválido.")

def main():
    gestor = Gestor_Animales()

    print("Porfavor elije una opcion y interactua con el programa. \n")

    while True:
        print("\n" + "="*50)
        print("   MENÚ DEL SISTEMA DE ANIMALES ")
        print("="*50)
        print("1. Crear un Caballo")
        print("2. Crear un Cocodrilo")
        print("3. Crear un Pez")
        print("4. Crear un Escarabajo")
        print("5. Crear un Pato")
        print("6. Listar todos los animales")
        print("7. Ejecutar un método de un animal")
        print("8. Salir")
        print("-"*50)

        opcion = input("Elige una opción (1-8): ").strip()

        if opcion == "1":
            nombre = input("Nombre del caballo: ")
            edad = int(input("Edad: "))
            habitat = input("Hábitat (ej. pradera): ")
            dieta = input("Dieta (ej. herbívoro): ")
            tamaño = input("Tamaño (ej. grande): ")
            color = input("Color: ")
            animal = Caballo(nombre, edad, habitat, dieta, tamaño, color)
            gestor.agregar_animal(animal)

        elif opcion == "2":
            nombre = input("Nombre del cocodrilo: ")
            edad = int(input("Edad: "))
            habitat = input("Hábitat (ej. pantano): ")
            dieta = input("Dieta (ej. carnívoro): ")
            tamaño = input("Tamaño (ej. muy grande): ")
            color = input("Color: ")
            animal = Cocodrilo(nombre, edad, habitat, dieta, tamaño, color)
            gestor.agregar_animal(animal)

        elif opcion == "3":
            nombre = input("Nombre del pez: ")
            edad = int(input("Edad: "))
            habitat = input("Hábitat (ej. océano): ")
            dieta = input("Dieta (ej. omnívoro): ")
            tamaño = input("Tamaño (ej. pequeño): ")
            color = input("Color: ")
            animal = Pez(nombre, edad, habitat, dieta, tamaño, color)
            gestor.agregar_animal(animal)

        elif opcion == "4":
            nombre = input("Nombre del escarabajo: ")
            edad = int(input("Edad: "))
            habitat = input("Hábitat (ej. bosque): ")
            dieta = input("Dieta (ej. herbívoro): ")
            tamaño = input("Tamaño (ej. diminuto): ")
            color = input("Color: ")
            animal = Escarabajo(nombre, edad, habitat, dieta, tamaño, color)
            gestor.agregar_animal(animal)

        elif opcion == "5":
            nombre = input("Nombre del pato: ")
            edad = int(input("Edad: "))
            habitat = input("Hábitat (ej. lago): ")
            dieta = input("Dieta (ej. omnívoro): ")
            tamaño = input("Tamaño (ej. mediano): ")
            color = input("Color: ")
            animal = Pato(nombre, edad, habitat, dieta, tamaño, color)
            gestor.agregar_animal(animal)

        elif opcion == "6":
            gestor.listar_animales()

        elif opcion == "7":
            gestor.listar_animales()
            if not gestor.animales:
                continue
            try:
                indice = int(input("\n Número del animal: "))
                metodo = input("Método a ejecutar (ej. moverse, alimentarse, comunicarse): ").strip()
                gestor.ejecutar_metodo(indice, metodo)
            except ValueError:
                print(" Por favor, ingresa un número válido.")

        elif opcion == "8":
            print("\n ¡Gracias por usar el Sistema de Animales! ¡Hasta pronto!")
            break

        else:
            print("\n Opción no válida. Por favor, elige una opción del 1 al 8.")

if __name__ == "__main__":
    main()