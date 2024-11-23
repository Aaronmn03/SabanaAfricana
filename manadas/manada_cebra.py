from manadas.manada import Manada


class ManadaCebra(Manada):
    numero_manadas = 0
    def __init__(self, entorno ,posicion_inicial,numero_animales):
        super().__init__(entorno ,posicion_inicial,numero_animales, 'C')
        

    def eliminar_animal(self, animal):
        animal.activo = False
        animal.join()
        print("Animal matado: " + animal.__str__())
        self.posicion_inicial = self.entorno.casilla_aleatoria_vacia()
        print("Posicion decidida")
        with self.entorno.ganador_lock:
            print("Acceso al entorno dado")
            if self.entorno.ganador is None and self.entorno.is_running:
                print("Añadiendo la cebra...")
                new_animal = super().anadir_animal(self.posicion_inicial)
                print("Se ha creado una nueva cebra" + new_animal.__str__() + "en: " + self.posicion_inicial.__str__())
            else:
                print("Si")
