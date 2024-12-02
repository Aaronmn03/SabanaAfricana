from queue  import Queue
import os
import pygame
import random
import threading
import time
from animales.cebra import Cebra
from animales.hiena import Hiena
from manadas.manada_cebra import ManadaCebra
from manadas.manada_hiena import ManadaHiena
from manadas.manada_leon import ManadaLeon
from tablero.casilla import Casilla

pygame.init()
fps = 30
ANCHO = 1200 
ALTO = 1000

class Juego:
    def __init__(self, configuracion):
        self.configuracion = configuracion
        self.entorno = self.crear_entorno()
        self.ganador = None
        self.ganador_lock = threading.Lock()
        self.leones = []
        self.cebras = []
        self.hienas = []
        self.is_running = True
        self.TAM_CELDA = (ALTO - 50) // self.configuracion.tamaño
        self.ventana = pygame.display.set_mode((ANCHO, ALTO))
        self.comenzar()

    def crear_entorno(self):
        matriz_aux = []
        fila = []
        x = 0
        y = 0
        for y in range(self.configuracion.tamaño):
            fila = []
            for x in range(self.configuracion.tamaño):
                fila.append(Casilla(x,y))
            matriz_aux.append(fila)    
        return matriz_aux
                    

    def comenzar(self):
        self.crear_animales()
        while True:
            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.is_running = False
                        break                
                #os.system("cls" if os.name == "nt" else "clear")
                #print(str(self))        
                self.ventana.fill((255, 255, 255))
                self.dibujar_grid()
                self.dibujar_animales()
                pygame.display.flip()
                time.sleep(1/fps) 
                
                with self.ganador_lock:
                    if self.ganador is not None:
                        self.mostrar_ganador()
                        pygame.display.flip()
                        print("El ganador es: " + self.ganador.__str__())
                        time.sleep(5)
                        self.finalizar()
                        break
            except KeyboardInterrupt:
                #os.system("cls" if os.name == "nt" else "clear")
                print("Juego interrumpido por el usuario. Esperando matar hilos")   
                self.finalizar()      
                pygame.quit()
                print(str(self))            

    def dibujar_grid(self):
        margen = 25
        for fila in range(self.configuracion.tamaño):
            for columna in range(self.configuracion.tamaño):
                pygame.draw.rect(self.ventana, (0, 0, 0), (columna * self.TAM_CELDA + margen, fila * self.TAM_CELDA + margen, self.TAM_CELDA, self.TAM_CELDA), 1)

    def dibujar_animales(self):
        for fila in self.entorno:
            for casilla in fila:
                if casilla.animal is not None:
                    imagen = None
                    color = None
                    animal = casilla.animal
                    if isinstance(animal, Cebra):
                        imagen = pygame.image.load("images/cebra.png")
                        color = (0, 0, 0)
                    elif isinstance(animal, Hiena):
                        imagen = pygame.image.load("images/hiena.png")
                        color = (100, 100, 100)
                    else:
                        imagen = pygame.image.load("images/leon.png")
                        color = (130, 130, 0)
                    imagen = pygame.transform.scale(imagen, (self.TAM_CELDA , self.TAM_CELDA))
                                           
                    pos_x = casilla.x * self.TAM_CELDA + 25
                    pos_y = casilla.y * self.TAM_CELDA + 25
                    self.ventana.blit(imagen, (pos_x, pos_y))    

                    fuente = pygame.font.Font(None, self.TAM_CELDA // 6)  
                    texto = fuente.render(f" {str(animal.id)}", True, color)  
                    texto_ancho, texto_alto = texto.get_size()
                    pos_x_texto = (0.15 + casilla.x) * self.TAM_CELDA + self.TAM_CELDA - texto_ancho
                    pos_y_texto = (0.15 + casilla.y) * self.TAM_CELDA + self.TAM_CELDA - texto_alto
                    self.ventana.blit(texto, (pos_x_texto,pos_y_texto)) 
                
    def mostrar_ganador(self):
        fuente = pygame.font.Font(None, 86)  
        texto = fuente.render(f"¡El ganador es {self.ganador.__str__()}!", True, (0, 0, 0)) 
        texto_rect = texto.get_rect(center=(ANCHO // 2, ALTO // 2)) 
        self.ventana.blit(texto, texto_rect)

    def crear_animales(self):
        self.manadas_leones = []
        self.manadas_hienas = []
        self.manadas_cebras = []
        leonesxmanada = self.configuracion.numero_leones // self.configuracion.manadas_leones
        restoleones = self.configuracion.numero_leones % self.configuracion.manadas_leones
        hienasxmanada = self.configuracion.numero_hienas // self.configuracion.manadas_hienas
        restohienas = self.configuracion.numero_hienas % self.configuracion.manadas_hienas 
        cebrasxmanada = self.configuracion.numero_cebras // self.configuracion.manadas_cebras
        restocebras = self.configuracion.numero_cebras % self.configuracion.manadas_cebras     
        
        for _ in range(self.configuracion.manadas_leones):
            nleones = leonesxmanada
            if restoleones > 0:
                nleones += 1
                restoleones -= 1
            self.manadas_leones.append(ManadaLeon(self,self.casilla_aleatoria_vacia(), nleones))
        for _ in range(self.configuracion.manadas_hienas):
            nhienas = hienasxmanada
            if restohienas > 0:
                nhienas += 1
                restohienas -= 1
            self.manadas_hienas.append(ManadaHiena(self,self.casilla_aleatoria_vacia(), nhienas)) 

        for _ in range(self.configuracion.manadas_cebras):
            ncebras = cebrasxmanada
            if restocebras > 0:
                ncebras += 1
                restocebras -= 1
            self.manadas_cebras.append(ManadaCebra(self,self.casilla_aleatoria_vacia(), ncebras)) 

    def eliminar_animal(self, animal):
        if isinstance(animal, Cebra):
            self.cebras.remove(animal)
        elif isinstance(animal, Hiena):  
            self.hienas.remove(animal)  
        else:
            print("El animal no es ni una cebra ni una hiena")
            
    def finalizar(self):
        self.is_running = False
        listas_animales = [self.leones, self.cebras, self.hienas]
        
        for lista in listas_animales:
            for animal in lista:
                animal.activo = False
                #print(animal.__str__() + "Su casilla esta bloqueada: " + str(animal.posicion.es_bloqueada()))
                
        for lista in listas_animales:
            for animal in lista:
                animal.join()              
                print("Animal  muerto: " + animal.__str__())                 

        todos_terminados = all(not animal.is_alive() for animal in self.leones + self.cebras + self.hienas)
        if todos_terminados:
            print("Todos los hilos han sido detenidos correctamente.")
            print("El ganador ha sido: " + self.ganador.__str__())
            exit()
        else:
            print("Algunos hilos no se han detenido correctamente.")                    

    def confirmar_ganador(self, manada):
            if self.ganador == None:
                self.ganador = manada

    def obtener_casilla_adyacente_vacia(self, casilla):
        while True:
            casilla_aux  = random.choice(self.casillas_adyacente(casilla))
            if self.casilla_existe_vacia(casilla_aux) and not casilla.__eq__(casilla_aux):
                return casilla_aux

    def casilla_aleatoria_vacia(self):
        while True:
            x = random.randint(0,self.configuracion.tamaño - 1)
            y = random.randint(0,self.configuracion.tamaño - 1)
            casilla = self.buscar_casilla(x,y)
            if self.casilla_existe_vacia(casilla):
                return casilla

    def casilla_existe_vacia(self, casilla):
        return self.existe_casilla(casilla.x, casilla.y) and casilla.es_vacia()
    
    def existe_casilla(self, x,y):
        return x >= 0 and x < self.configuracion.tamaño and y >= 0 and y < self.configuracion.tamaño

    def casillas_adyacente(self,casilla):
        casillas_adyacentes = []
        posibles_movimientos = [(0,0),(-1, -1), (-1, 0), (-1, 1),(0, -1),(0, 1),(1, -1), (1, 0), (1, 1)]  
        random.shuffle(posibles_movimientos)      
        for dx, dy in posibles_movimientos:
            x = casilla.x
            y = casilla.y            
            if self.existe_casilla(x + dx, y + dy):
                casillas_adyacentes.append(self.buscar_casilla(x + dx, y + dy))
        return casillas_adyacentes
    
    def buscar_casilla(self,x,y):
        return self.entorno[y][x]
    
    def obtener_casilla_manada_vacia(self, posicion_inicial, posiciones_ocupadas):
        visitadas = set()
        cola = Queue()
        cola.put(posicion_inicial)
        
        while not cola.empty():
            posicion_actual = cola.get()
            if posicion_actual not in visitadas:
                visitadas.add(posicion_actual)
                
                # Verificar si la casilla actual es válida
                if self.casilla_existe_vacia(posicion_actual) and posicion_actual not in posiciones_ocupadas:
                    return posicion_actual
                
                # Añadir las casillas adyacentes a la cola para seguir buscando
                for vecina in self.casillas_adyacente(posicion_actual):  # Aseguramos que devuelve una lista
                    if vecina not in visitadas:
                        cola.put(vecina)
        
        # Si no se encuentra ninguna casilla válida, puedes lanzar una excepción o manejarlo de otro modo
        raise ValueError("No hay casillas vacías disponibles cerca de la posición inicial.")
        
    
    def num_animales_cercanos(self, posicion, visitadas=None):
        if visitadas is None:
            visitadas = set()

        contador = 0
        lista_posibilidades = self.casillas_adyacente(posicion)
        while len(lista_posibilidades) != 0:
            posicion_aux = lista_posibilidades.pop()
            if posicion_aux in visitadas:
                continue
            else:
                visitadas.add(posicion_aux)
            if posicion_aux.animal is not None:
                if isinstance(posicion_aux.animal,type(posicion.animal)):
                    contador += 1
                    contador += self.num_animales_cercanos(posicion_aux, visitadas)
        return contador

    def __str__(self):
        matriz_str = ""
        tamaño = self.configuracion.tamaño
        matriz_str += "—" * (6 * tamaño) + "\n" 

        for fila in self.entorno:
            fila_str = " | ".join(f"{casilla.animal if casilla.animal else '   '}" for casilla in fila)
            matriz_str += f"| {fila_str} |\n"
            matriz_str += "—" * (6 * tamaño) + "\n"
        return matriz_str
                 