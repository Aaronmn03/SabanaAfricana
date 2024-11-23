import threading

from animales.cebra import Cebra
from animales.hiena import Hiena


class Casilla:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.lock = threading.Lock()    
        self.animal = None

    def bloquear(self):
        #print(self.__str__() + "Es bloqueada")
        self.lock.acquire() 
        
    def desbloquear(self):
        #print(self.__str__() + "Es desbloqueada")
        self.lock.release()

    def suma(self,dx,dy):
        self.x += dx
        self.y += dy

    def es_vacia(self):
        return self.animal == None
    
    def hay_cebra(self):
        return isinstance(self.animal, Cebra)
    
    def hay_hiena(self):
        return isinstance(self.animal, Hiena)
    
    def hay_presa(self):
        return self.hay_hiena() or self.hay_cebra()
    
    def __eq__(self, other):
        if isinstance(other, Casilla):
            return self.x == other.x and self.y == other.y
        return False
    
    def es_bloqueada(self):
        return self.lock.locked()
    
    def vaciar(self):
        self.animal = None
    
    def anadir_animal(self, animal):
        self.animal = animal

    def __str__(self):
        return "Soy ( " + str(self.x) + ", " + str(self.y) +") y tengo a " + str(self.animal)
    
    def __hash__(self):
        return hash((self.x, self.y))