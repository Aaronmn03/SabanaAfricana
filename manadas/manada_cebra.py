from manadas.manada import Manada


class ManadaCebra(Manada):
    numero_manadas = 0
    def __init__(self, entorno ,posicion_inicial,numero_animales):
        super().__init__(entorno ,posicion_inicial,numero_animales, 'C')
        

    def eliminar_animal(self, animal):
        if animal.activo == True:
            animal.activo = False
            animal.join()
            self.entorno.eliminar_animal(animal)
            #print("Animal matado: " + animal.__str__())
            self.posicion_inicial = self.entorno.casilla_aleatoria_vacia()
            if self.entorno.ganador is None and self.entorno.is_running:
                new_animal = super().anadir_animal(self.posicion_inicial)
                print("Se ha creado una nueva cebra: " + new_animal.__str__() + " en: " + self.posicion_inicial.__str__())

