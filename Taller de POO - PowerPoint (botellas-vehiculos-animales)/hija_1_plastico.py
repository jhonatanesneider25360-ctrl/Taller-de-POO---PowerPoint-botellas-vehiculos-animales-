from padre import botella

class Botella_Plastico(botella):
    def _init_(self, capacidad, forma, reciclable):
        super()._init_(capacidad, forma)
        self.reciclable = reciclable

    def mostrar_info(self):
        print("Botella de Plástico")
        super().mostrar_info()
        print("Reciclable:", self.reciclable)