import os
import time
from animales.cebra import Cebra
from animales.leon import Leon
from juego import Juego


def main():  
    
    juego = Juego()
    juego.comenzar()
    """
    juego = Juego()
    juego.entorno[0][0].animal = Cebra("C", juego, None, juego.entorno[0][0])
    juego.entorno[1][0].animal = Cebra("C", juego, None, juego.entorno[1][1])
    juego.entorno[2][0].animal = Cebra("C", juego, None, juego.entorno[2][2])
    juego.entorno[3][0].animal = Cebra("C", juego, None, juego.entorno[2][2])
    juego.entorno[0][3].animal = Cebra("C", juego, None, juego.entorno[2][2])
    juego.entorno[0][1].animal = Leon("L", juego, None, juego.entorno[2][2])
    juego.entorno[0][2].animal = Leon("L", juego, None, juego.entorno[2][2])
    juego.entorno[0][3].animal = Leon("L", juego, None, juego.entorno[2][2])
    juego.entorno[2][3].animal = Leon("L", juego, None, juego.entorno[2][2])
    print(str(juego.__str__()))
    print(juego.num_animales_cercanos(juego.entorno[0][1]))
    """

    
    
if __name__ == "__main__":
    main()