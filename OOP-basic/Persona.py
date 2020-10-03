class Estudiante:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera

    def presentacion(self):
        print("Mi nombre es", self.nombre, "soy estudiante de", self.carrera, end=', ')


class Musico:
    def __init__(self, instrumento, estiloPrincipal):
        self.instrumento = instrumento
        self.estiloPrincipal = estiloPrincipal

    def presentacion(self):
        print("mi instrumento es", self.instrumento + ", mi estilo principal es como", self.estiloPrincipal)


class Jean(Estudiante, Musico):
    def __init__(self):
        Estudiante.__init__(self, "Jean Carlos", "sistemas")
        Musico.__init__(self, "guitarra eléctrica", "solista")

    def presentacion(self):
        Estudiante.presentacion(self)
        Musico.presentacion(self)
