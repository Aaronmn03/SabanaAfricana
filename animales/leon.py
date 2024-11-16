import random
import time

from colorama import Fore, Style

from animales.animal import Animal


class Leon(Animal):
    def __init__(self, id, entorno, manada, posicion_inicial):
        super().__init__(id, entorno, manada, self.velocidad_random(), posicion_inicial)

    def run(self):
        time.sleep(self.velocidad)
        while self.activo:
            super().mover() 
            time.sleep(self.velocidad) 
        
    def cazar():
        pass

    def velocidad_random(self):
        return random.uniform(1.5, 2.5)

    def __str__(self):
        return f"{Fore.YELLOW}{super().__str__()}{Style.RESET_ALL}"