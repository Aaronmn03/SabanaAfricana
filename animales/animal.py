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
        self.posicion.__str__()        
        self.entorno.eliminar_animal(self.posicion)
        self.posicion.vaciar()
        self.posicion = movimiento
        self.entorno.anadir_animal(self, self.posicion)
        for casilla in lista_movimientos:
            casilla.desbloquear()
        

    def descansar():
        pass

    def comprobar_adyacentes(self):
        encontrado = False
        while not encontrado:
            lista_posibles_movimientos = self.entorno.casillas_adyacente(self.posicion)
            lista_movimientos = []
            for casilla in lista_posibles_movimientos:
                if not casilla.es_bloqueada() and self.entorno.existe(casilla) and self.entorno.es_vacia(casilla):
                    casilla.bloquear()
                    lista_movimientos.append(casilla)
                    encontrado = True
            if len(lista_movimientos) == 0:
                time.sleep(0.4)
        return lista_movimientos

    def __str__(self):
        return self.id
        