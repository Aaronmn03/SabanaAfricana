import random
import time
from animales.animal import Animal
from colorama import Fore, Style

from animales.cebra import Cebra

class Hiena(Animal):
    def __init__(self, id, entorno, manada, posicion_inicial):
        super().__init__(id, entorno, manada, self.velocidad_random(), posicion_inicial)

    def run(self):

        time.sleep(self.velocidad)
        while self.activo:
            if not self.posicion.es_bloqueada():
                posicion_aux = self.posicion
                print(self.__str__() + "Esta intentando acceder a su posicion")            
                self.posicion.bloquear() 
                print("Tengo mi posicion bloqueada y estoy haciendo cosas: " + self.__str__())
                posibles_presas = self.comprobar_adyacentes_caza()
                if not len(posibles_presas) == 0:
                    print("Voy a cazar " + self.__str__())
                    self.cazar(posibles_presas)
                else:            
                    print("No tengo caza posible, voy a moverme" + self.__str__())
                    super().mover() 
                time.sleep(self.velocidad) 
        
    def cazar(self, posibles_presas):
        casilla = random.choice(posibles_presas)
        presa = casilla.animal
        if isinstance(presa, Cebra):
            if self.comprobar_si_caza(casilla):
                #print("Caza")
                posicion_aux = self.posicion
                casilla.vaciar()
                self.posicion.vaciar()
                posicion_aux.desbloquear()
                self.posicion = casilla
                self.posicion.anadir_animal(self)
                presa.notificar_caza()
                print("Animal: " + super().__str__() + " ha cazado a: " + presa.__str__())                         
                for casilla in posibles_presas:
                    casilla.desbloquear()  
                    print(self.__str__() + " -> " + casilla.__str__() + " Desbloqueada")              
                with self.manada.lock:
                    self.manada.aumentar_puntuacion(1)

            else:
                #print("No puede cazar, inferioridad numerica")
                self.posicion.desbloquear()
                for casilla in posibles_presas:
                    casilla.desbloquear()  
                    print(self.__str__() + " -> " + casilla.__str__() + " Desbloqueada")
                    

    def comprobar_adyacentes_caza(self):
        lista_posibles_movimientos = self.entorno.casillas_adyacente(self.posicion)
        lista_caza = []
        for casilla in lista_posibles_movimientos:
            if not casilla.es_bloqueada() and self.entorno.existe_casilla(casilla.x, casilla.y) and casilla.hay_cebra():
                casilla.bloquear()
                print(self.__str__() + " -> " + casilla.__str__() + " Bloqueada")
                lista_caza.append(casilla)
        return lista_caza 

    def comprobar_si_caza(self, casilla):
        n_apoyo = self.entorno.num_animales_cercanos(self.posicion)
        n_otros = self.entorno.num_animales_cercanos(casilla)
        #print(self.__str__() + " Hienas: " + str(n_apoyo) + " vs Cebras: " + str(n_otros))
        return n_apoyo > n_otros
    
    def notificar_caza(self):
        self.manada.eliminar_animal(self)

    def velocidad_random(self):
        return random.uniform(4, 5)
    
    def __str__(self):
        return f"{Fore.LIGHTBLACK_EX}{super().__str__()}{Style.RESET_ALL}"