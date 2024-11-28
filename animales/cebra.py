import random
import time
from animales.animal import Animal


class Cebra(Animal):
    def __init__(self, id, entorno, manada, posicion_inicial):
        super().__init__(id, entorno, manada, self.velocidad_random(), posicion_inicial)
    
    def run(self):
        time.sleep(self.velocidad)
        if self.activo:
            while self.activo:
                debo_descansar = random.random() < 0.2
                if debo_descansar:           
                    time.sleep(random.uniform(4, 6))                         
                if not self.posicion.es_bloqueada():
                    self.posicion.bloquear() 
                    if self.activo:                       
                        posicion_aux = self.posicion   
                        super().mover() 
                    time.sleep(self.velocidad) 
        

    def notificar_caza(self):
        self.manada.eliminar_animal(self)

    def velocidad_random(self):
        return random.uniform(2.75, 3.75)
    
    def __str__(self):
        return super().__str__()