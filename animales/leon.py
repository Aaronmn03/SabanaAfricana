import random
import time

from colorama import Fore, Style

from animales.animal import Animal
from animales.cebra import Cebra


class Leon(Animal):
    def __init__(self, id, entorno, manada, posicion_inicial):
        super().__init__(id, entorno, manada, self.velocidad_random(), posicion_inicial)

    def run(self):

        time.sleep(self.velocidad)
        while self.activo:
            with self.posicion.lock:
                posibles_presas = self.comprobar_adyacentes_caza()
                if not len(posibles_presas) == 0:
                    self.cazar(posibles_presas)
                else:
                    super().mover() 
            time.sleep(self.velocidad) 
        
    def cazar(self, posibles_presas):
        casilla = random.choice(posibles_presas)
        presa = casilla.animal
        if isinstance(presa, Cebra):
            presa.notificar_caza()
            with self.manada.lock:
                self.manada.aumentar_puntuacion(1)
            casilla.vaciar()
            self.posicion.vaciar()
            self.posicion = casilla
            self.posicion.anadir_animal(self)
            for casilla in posibles_presas:
                casilla.desbloquear()
            print("Animal: " + super().__str__() + " ha cazado")
        else:
            print("No era una cebra wtf?")

    def comprobar_adyacentes_caza(self):
        lista_posibles_movimientos = self.entorno.casillas_adyacente(self.posicion)
        lista_caza = []
        for casilla in lista_posibles_movimientos:
            if not casilla.es_bloqueada() and self.entorno.existe_casilla(casilla.x, casilla.y) and casilla.hay_cebra():
                casilla.bloquear()
                lista_caza.append(casilla)
        return lista_caza      

    def velocidad_random(self):
        return random.uniform(1.5, 2.5)

    def __str__(self):
        return f"{Fore.YELLOW}{super().__str__()}{Style.RESET_ALL}"