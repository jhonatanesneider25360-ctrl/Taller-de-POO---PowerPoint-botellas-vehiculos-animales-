class botella:
    def __init__(self, capacidad, material, forma, diseño, tapa, grabados):
        self.capacidad = capacidad
        self.material = material
        self.forma = forma
        self.diseño = diseño
        self.tapa = tapa
        self.grabados = grabados

    def imprimir_info(self):
        print("Datos de lal botellas: \n ")
        print("Capacidad:", self.capacidad)
        print("Material:", self.material)
        print("Forma:", self.forma)
        print("Diseño:", self.diseño)
        print("Tapa:", self.tapa)
        print("Grabados:", self.grabados)