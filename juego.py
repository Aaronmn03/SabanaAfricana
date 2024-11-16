import random
from animales.leon import Leon
from configuracion import Configuracion
from manadas.manada_cebra import ManadaCebra
from manadas.manada_hiena import ManadaHiena
from manadas.manada_leon import ManadaLeon
from tablero.casilla import Casilla


class Juego:
    def __init__(self):
        self.configuracion = Configuracion()
        self.entorno = self.crear_entorno()
        self.ganador = False
        self.leones = []
        self.cebras = []
        self.hienas = []
        self.crear_animales()

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
                    

    def comenzar():
        pass

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
    def finalizar(self):
        listas_animales = [self.leones, self.cebras, self.hienas]
        for lista in listas_animales:
            for animal in lista:
                animal.activo = False
                
        for lista in listas_animales:
            for animal in lista:
                animal.join()                               

        todos_terminados = all(not animal.is_alive() for animal in self.leones + self.cebras + self.hienas)
        if todos_terminados:
            print("Todos los hilos han sido detenidos correctamente.")
        else:
            print("Algunos hilos no se han detenido correctamente.")                    


    def confirmar_ganador():
        pass

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

    def __str__(self):
        matriz_str = ""
        tamaño = self.configuracion.tamaño
        matriz_str += "—" * (6 * tamaño) + "\n" 

        for fila in self.entorno:
            fila_str = " | ".join(f"{casilla.animal if casilla.animal else '   '}" for casilla in fila)
            matriz_str += f"| {fila_str} |\n"
            matriz_str += "—" * (6 * tamaño) + "\n"
        return matriz_str
                 