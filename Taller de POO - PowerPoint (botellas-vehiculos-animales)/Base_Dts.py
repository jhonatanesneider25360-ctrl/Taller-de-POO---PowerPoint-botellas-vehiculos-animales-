class BaseDatos:
    def _init_(self):
        self.botellas = []

    def agregar(self, botella):
        self.botellas.append(botella)
        print("Botella agregada correctamente.")
        
        
    def listar(self):
        if len(self.botellas) == 0:
            print("No hay botellas registradas.")
        else:
            for i, botella in enumerate(self.botellas):
                print("Índice:", i)
                botella.mostrar_info()


    def actualizar(self, index, nueva_capacidad):
        if 0 <= index < len(self.botellas):
            self.botellas[index].capacidad = nueva_capacidad
            print("Capacidad actualizada.")
        else:
            print("Índice inválido.")


    def eliminar(self, index):
        if 0 <= index < len(self.botellas):
            self.botellas.pop(index)
            print("Botella eliminada.")
        else:
            print("Índice inválido.")