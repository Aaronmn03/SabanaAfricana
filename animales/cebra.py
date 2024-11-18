import random
import time
from animales.animal import Animal


class Cebra(Animal):
    def __init__(self, id, entorno, manada, posicion_inicial):
        super().__init__(id, entorno, manada, self.velocidad_random(), posicion_inicial)
    
    def run(self):
        time.sleep(self.velocidad)
        while self.activo:
            with self.posicion.lock:                
                super().mover() 
            time.sleep(self.velocidad) 
        

    def notificar_caza(self):
        self.manada.eliminar_animal(self)

    def velocidad_random(self):
        return random.uniform(2.75, 3.75)