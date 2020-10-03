class Radio:

    def __init__(self, estado = "APAGADO", cancion = "NINGUNA CANCIÓN"):
        self.estado = estado
        self.cancion = cancion

    def encender(self):
        self.estado = "ENCENDIDO"
        self.cancion = "Tchaikovsky - Dance of the Sugar Plum Fairy (The Nutcracker Suite)"

    def apagar(self):
        self.estado = "APAGADO"
        self.cancion = "NINGUNA CANCIÓN"

    def sumergirloAlAgua(self):
        self.estado = "AVERIADO"
        self.cancion = "BURBUJAS"

    def verEstado(self):
        print("El radio está", self.estado + ", está reproduciendo", self.cancion, "\n")
