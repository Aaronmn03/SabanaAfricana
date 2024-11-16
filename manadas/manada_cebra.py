from manadas.manada import Manada


class ManadaCebra(Manada):
    numero_manadas = 0
    def __init__(self, entorno ,posicion_inicial,numero_animales):
        super().__init__(entorno ,posicion_inicial,numero_animales, 'C')

    def eliminar_animal(self, animal):
        pass