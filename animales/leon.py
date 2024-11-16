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
    
    def comprobar_adyacentes_caza(self):
        encontrado = False
        while not encontrado:
            lista_posibles_movimientos = self.entorno.casillas_adyacente(self.posicion)
            lista_cazas = []
            for casilla in lista_posibles_movimientos:
                if not casilla.es_bloqueada() and self.entorno.existe(casilla) and self.entorno.es_vacia(casilla):
                    casilla.bloquear()
                    lista_movimientos.append(casilla)
                    encontrado = True
            if len(lista_movimientos) == 0:
                time.sleep(0.4)
        return lista_movimientos

    def __str__(self):
        return f"{Fore.YELLOW}{super().__str__()}{Style.RESET_ALL}"