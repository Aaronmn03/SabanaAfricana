import os
import time
from animales.leon import Leon
from juego import Juego
from tablero.casilla import Casilla


def main():  
    fps = 1
    juego = Juego()
    try:
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print(str(juego))
            time.sleep(1/fps) 
    except KeyboardInterrupt:
        os.system("cls" if os.name == "nt" else "clear")
        print("Juego interrumpido por el usuario. Esperando matar hilos")   
        juego.finalizar()      
        print(str(juego))
    
    
if __name__ == "__main__":
    main()