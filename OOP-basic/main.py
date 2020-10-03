__author__ = "JeanCarlos911"

from Persona import Jean
from Celular import Celular, Smartphone
from Radio import Radio


class Grabadora(Radio):
    def __init__(self):
        super().__init__("ENCENDIDA", "UN RUIDO")

    def verEstado(self):
        print("La grabadora está", self.estado + ", está reproduciendo", self.cancion, "\n")


if __name__ == '__main__':
    miRadio = Radio()

    print("\nEstado inicial: ")
    miRadio.verEstado()

    miRadio.encender()
    print("Encencí la radio. Estado actual: ")
    miRadio.verEstado()

    miRadio.apagar()
    print("Apagué el radio. Estado actual: ")
    miRadio.verEstado()

    miRadio.sumergirloAlAgua()
    print("Sumergí el radio al agua. Estado final: ")
    miRadio.verEstado()

    miNuevoRadio = Radio("ENCENDIDO", "Slipknot - Despise (Demo)")
    print("Compré una nueva radio, su estado es:")
    miNuevoRadio.verEstado()

    miCelular = Celular()
    miCelular.sumergirloAlAgua()
    print("Compré un celular y lo sumergí al agua. Su estado:")
    miCelular.verEstado()

    miNuevoCelular = Celular()
    print("compré otro celular. Su estado:")
    miNuevoCelular.verEstado()

    miNuevoCelular.encender()
    print("Lo encendí. Su estado:")
    miNuevoCelular.verEstado()

    miNuevoSmartphone = Smartphone()
    print("Nuevo smartphone. Su estado:")
    miNuevoSmartphone.verEstado()

    miNuevaGrabadora = Grabadora()
    print("Nueva grabadora. Su estado:")
    miNuevaGrabadora.verEstado()

    jean = Jean()
    jean.presentacion()
