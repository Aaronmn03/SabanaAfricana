import random
import time
from animales.animal import Animal


class Cebra(Animal):
    def __init__(self, id, entorno, manada, posicion_inicial):
        super().__init__(id, entorno, manada, self.velocidad_random(), posicion_inicial)
    
    def run(self):
        time.sleep(self.velocidad)
        while self.activo:
            super().mover() 
            time.sleep(self.velocidad) 
        

    def notificar_caza():
        pass

    def velocidad_random(self):
        return random.uniform(2.75, 3.75)