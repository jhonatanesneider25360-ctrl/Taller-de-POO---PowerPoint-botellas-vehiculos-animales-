from padre import botella

class Botella_Vidrio(botella):
    def __init__(self, capacidad, forma, reutilizable):
        super().__init__(
            capacidad=capacidad,
            material="Vidrio",
            forma=forma,
            diseño="Liso",
            tapa="Blanca",
            grabados="Nombre"
        )
        self.reutilizable = reutilizable

    def imprimir_info(self):
        super().imprimir_info()
        print("Reutilizable:", self.reutilizable)