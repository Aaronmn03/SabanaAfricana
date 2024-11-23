import random
import time

from colorama import Fore, Style

from animales.animal import Animal
from animales.cebra import Cebra
from animales.hiena import Hiena


class Leon(Animal):
    def __init__(self, id, entorno, manada, posicion_inicial):
        super().__init__(id, entorno, manada, self.velocidad_random(), posicion_inicial)

    def run(self):
        time.sleep(self.velocidad)
        while self.activo:
            debo_descansar = random.random() < 0.4
            if debo_descansar:
                print(self.__str__() + " -> Esta descansando")
                time.sleep(random.uniform(4, 6))
                print(self.__str__() + " -> Ha dejado de descansar")
            posicion_aux = self.posicion
            #print(self.__str__() + "Esta intentando acceder a su posicion")
            self.posicion.bloquear()    
            #print(self.__str__() + "Ha accedido al mutex de la posicion")
            posibles_presas = self.comprobar_adyacentes_caza()
            if not len(posibles_presas) == 0:
                #print("Voy a cazar" + self.__str__())
                self.cazar(posibles_presas)
            else:
                super().mover() 
            time.sleep(self.velocidad)
        
    def cazar(self, posibles_presas):
        try:
            casilla = random.choice(posibles_presas)
            presa = casilla.animal
            puntos = 0
            #print(type(presa).__name__ + " - >" + str(presa.__str__()))
            if isinstance(presa, Cebra):
                puntos = 1
            if isinstance(presa, Hiena):
                puntos = 2
                if not self.comprobar_si_caza(casilla):
                    self.posicion.desbloquear()
                    return
            casilla.vaciar()
            self.posicion.vaciar()
            posicion_aux = self.posicion
            self.posicion = casilla
            posicion_aux.desbloquear()
            self.posicion.anadir_animal(self)
            presa.notificar_caza()
            with self.manada.lock:
                self.manada.aumentar_puntuacion(puntos)
            #print("Animal: " + super().__str__() + " ha cazado")
        finally:
            for casilla in posibles_presas:
                casilla.desbloquear()
        

    def comprobar_adyacentes_caza(self):
        lista_posibles_movimientos = self.entorno.casillas_adyacente(self.posicion)
        lista_caza = []
        for casilla in lista_posibles_movimientos:
            if self.entorno.existe_casilla(casilla.x, casilla.y) and casilla.hay_presa():
                casilla.bloquear()
                lista_caza.append(casilla)
        return lista_caza      
    
    def comprobar_si_caza(self, casilla):
        n_apoyo = self.entorno.num_animales_cercanos(self.posicion)
        n_otros = self.entorno.num_animales_cercanos(casilla)
        return n_apoyo >= n_otros    

    def velocidad_random(self):
        return random.uniform(1.5, 2.5)

    def __str__(self):
        return f"{Fore.YELLOW}{super().__str__()}{Style.RESET_ALL}"