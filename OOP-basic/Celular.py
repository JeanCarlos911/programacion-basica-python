from Radio import Radio


class Celular(Radio):

    def encender(self):
        self.estado = "DESBLOQUEADO"

    def apagar(self):
        self.estado = "BLOQUEADO"

    def verEstado(self):
        print("El celular está", self.estado, "\n")


class Smartphone(Celular):

    def __init__(self, estado="CON GARANTÍA", cancion="una imagen con un bloqueo"):
        super().__init__(estado, cancion)
