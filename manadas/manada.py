from animales.cebra import Cebra
from animales.hiena import Hiena
from animales.leon import Leon


class Manada:

    def __init__(self, entorno, posicion_inicial, numero_animales, id_tipo):
        self.animales = []
        self.posicion_inicial = posicion_inicial
        self.numero_animales = numero_animales
        self.entorno = entorno
        self.puntuacion = 0
        self.id = str(self.__class__.numero_manadas) + id_tipo
        self.__class__.numero_manadas += 1
        self.id_tipo = id_tipo
        self.numero_creadas= 0

        for i in range(numero_animales):
            animal = self.anadir_animal( self.posicion_inicial)
            self.posicion_inicial = self.entorno.obtener_casilla_adyacente_vacia(self.posicion_inicial)  
                 

    def anadir_animal(self, posicion):
        animal = None
        id = self.id + str(self.numero_creadas)
        if self.id_tipo == 'H':
            animal = Hiena(id, self.entorno, self, posicion) 
            self.entorno.hienas.append(animal)
        elif self.id_tipo == 'L':
            animal = Leon(id, self.entorno, self, posicion)
            self.entorno.leones.append(animal)
        else:
            animal = Cebra(id, self.entorno, self, posicion)
            self.entorno.cebras.append(animal)
        self.numero_creadas += 1   
        print("Obteniendo acceso a la posicion... " + self.posicion_inicial.__str__() + str(self.posicion_inicial.lock.locked())) 
        with self.posicion_inicial.lock:    
            print("Acceso obtenido")
            self.posicion_inicial.anadir_animal(animal)
        self.animales.append(animal)
        animal.start()
        return animal
    
    def __str__(self):
        return self.id
    

