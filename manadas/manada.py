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

        for i in range(numero_animales):
            id_animal = self.id + str(i)
            animal = self.anadir_animal(id_animal, self.posicion_inicial)
            self.posicion_inicial = self.entorno.obtener_casilla_adyacente_vacia(self.posicion_inicial)       

    def anadir_animal(self, id, posicion):
        animal = None
        if self.id_tipo == 'H':
            animal = Hiena(id, self.entorno, self, posicion) 
            self.entorno.hienas.append(animal)
        elif self.id_tipo == 'L':
            animal = Leon(id, self.entorno, self, posicion)
            self.entorno.leones.append(animal)
        else:
            animal = Cebra(id, self.entorno, self, posicion)
            self.entorno.cebras.append(animal)
        animal.start()
        self.posicion_inicial.anadir_animal(animal)
        self.animales.append(animal)
        return animal
    
    def __str__(self):
        return self.id
    

