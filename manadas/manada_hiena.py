from animales.hiena import Hiena
from manadas.manada import Manada


class ManadaHiena(Manada):
    numero_manadas = 0
    def __init__(self, entorno ,posicion_inicial,numero_animales):
        super().__init__(entorno ,posicion_inicial,numero_animales, 'H')
        self.puntuacion = 0

    def eliminar_animal(self, animal):
        pass
