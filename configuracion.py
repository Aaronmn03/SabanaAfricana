class Configuracion:
    def __init__(self):
        """
        self.tamaño = input("Introduce el tamaño de la matriz: ")
        while not self.tamaño.isdigit() or int(self.tamaño) <= 3:
            print("Entrada inválida. Por favor, introduce un número entero o un numero más alto.")
            self.tamaño = input("Introduce el tamaño de la matriz: ")
        self.tamaño = int(self.tamaño)

        limite_leones = ((self.tamaño * self.tamaño) / 10)
        self.numero_leones = input("Introduce el número de leones: ")
        
        while not self.numero_leones.isdigit() or int(self.numero_leones) >= limite_leones:
            if not self.numero_leones.isdigit():
                print("Entrada inválida. Por favor, introduce un número entero.")
            else:
                print("Entrada inválida. Por favor, introduce un número menor de leones, no caben.")
            
            self.numero_leones = input("Introduce el número de leones: ")
        
        self.numero_leones = int(self.numero_leones) 

        self.manadas_leones = input("Introduce el número de manadas de leones: ")
        while not self.manadas_leones.isdigit() or int(self.manadas_leones) > self.numero_leones:
            if not self.manadas_leones.isdigit():
                print("Entrada inválida. Por favor, introduce un número entero.")
            else:
                print("Entrada inválida. Por favor, introduce un número menor de manadas que de leones.")
            self.manadas_leones = input("Introduce el número de manadas de leones: ")
        
        self.manadas_leones = int(self.manadas_leones)

        self.manadas_hienas = input("Introduce el número de manadas de hienas: ")
        while not self.manadas_hienas.isdigit() or int(self.manadas_hienas) > self.numero_leones * 3:
            if not self.manadas_hienas.isdigit():
                print("Entrada inválida. Por favor, introduce un número entero.")
            else:
                print("Entrada inválida. Por favor, introduce un número menor de manadas que de hienas.")
            self.manadas_hienas = input("Introduce el número de manadas de hienas: ")
        
        self.manadas_hienas = int(self.manadas_hienas)  

        self.manadas_cebras = input("Introduce el número de manadas de cebras: ")
        while not self.manadas_cebras.isdigit() or int(self.manadas_cebras) > self.numero_leones * 6:
            if not self.manadas_cebras.isdigit():
                print("Entrada inválida. Por favor, introduce un número entero.")
            else:
                print("Entrada inválida. Por favor, introduce un número menor de manadas que de cebras.")
            self.manadas_cebras = input("Introduce el número de manadas de cebras: ")
        
        self.manadas_cebras = int(self.manadas_cebras)
        self.numero_hienas = self.numero_leones * 3
        self.numero_cebras = self.numero_leones * 6          
        """
        self.tamaño = 4
        self.numero_leones = 1
        self.numero_hienas = self.numero_leones * 3
        self.numero_cebras = self.numero_leones * 6
        self.manadas_leones = 2
        self.manadas_hienas = 1
        self.manadas_cebras = 4
        