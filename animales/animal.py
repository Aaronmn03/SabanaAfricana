import random
from threading import Thread
import time


class Animal(Thread):
    def __init__(self, id, entorno, manada, velocidad, posicion_inicial):
        super().__init__()
        self.id = id
        self.entorno = entorno
        self.descanso = 0
        self.manada = manada
        self.velocidad = velocidad
        self.posicion = posicion_inicial
        self.activo = True
    
    def run():
        pass

    def mover(self):
        
        lista_movimientos = self.comprobar_adyacentes()
        movimiento = random.choice(lista_movimientos)
        #print("Soy: " + str(self.id) + " y me he movido a:( " + str(self.posicion.x) + ", " + str(self.posicion.y) + ")")
        #self.posicion.__str__()        
        self.posicion.vaciar()
        self.posicion = movimiento
        self.posicion.anadir_animal(self)
        for casilla in lista_movimientos:
            casilla.desbloquear()
        

    def descansar():
        pass

    def comprobar_adyacentes(self):
        encontrado = False
        while not encontrado:
            lista_posibles_movimientos = self.entorno.casillas_adyacente(self.posicion)
            lista_movimientos = []
            #print("Casilla actual: " + self.posicion.__str__())
            for casilla in lista_posibles_movimientos:
                #print(casilla.__str__() + str(casilla.es_bloqueada()) + " " + str(self.entorno.existe_casilla(casilla.x, casilla.y)) + " "  + str(casilla.es_vacia()))
                if not casilla.es_bloqueada() and self.entorno.existe_casilla(casilla.x, casilla.y) and casilla.es_vacia():
                    casilla.bloquear()
                    lista_movimientos.append(casilla)
                    encontrado = True
            if len(lista_movimientos) == 0:
                time.sleep(0.4)
        return lista_movimientos

    def __str__(self):
        return self.id
        