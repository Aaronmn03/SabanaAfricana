import threading
from animales.hiena import Hiena
from manadas.manada import Manada


class ManadaHiena(Manada):
    numero_manadas = 0
    def __init__(self, entorno ,posicion_inicial,numero_animales):
        super().__init__(entorno ,posicion_inicial,numero_animales, 'H')
        self.puntuacion = 0
        self.lock = threading.Lock() 

    def aumentar_puntuacion(self, aumento):
        self.puntuacion += aumento
        print("Manada: " + self.__str__())
        if self.puntuacion >= 20:
            with self.entorno.ganador_lock:
                self.entorno.confirmar_ganador(self)
            

    def eliminar_animal(self, animal):
        animal.activo = False
        animal.join()
        self.entorno.eliminar_animal(animal)
    
    def __str__(self):
        return super().__str__() + " con: " + str(self.puntuacion) + " pts."