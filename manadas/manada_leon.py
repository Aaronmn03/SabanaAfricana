from manadas.manada import Manada


class ManadaLeon(Manada):
    numero_manadas = 0
    def __init__(self, entorno ,posicion_inicial,numero_animales):
        super().__init__(entorno ,posicion_inicial,numero_animales, 'L')
        self.puntuacion = 0


