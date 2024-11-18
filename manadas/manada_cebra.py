from manadas.manada import Manada


class ManadaCebra(Manada):
    numero_manadas = 0
    def __init__(self, entorno ,posicion_inicial,numero_animales):
        super().__init__(entorno ,posicion_inicial,numero_animales, 'C')

    def eliminar_animal(self, animal):
        animal.activo = False
        animal.join()
        id_aux = animal.id
        self.posicion_inicial = self.entorno.casilla_aleatoria_vacia()
        new_animal = super().anadir_animal(id_aux, self.posicion_inicial)
        print("Se ha creado una nueva cebra en: " + self.posicion_inicial.__str__())
