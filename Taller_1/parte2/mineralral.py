
# Parte 2 taller



import numpy as np
import matplotlib.pyplot as plt



# CLASE MINERAL


class Mineral:
    def __init__(self, nombre, dureza, rompimiento_por_fractura, color, composicion, lustre, specific_gravity, sistema_cristalino):
        self.nombre = nombre
        self.dureza = dureza
        self.rompimiento_por_fractura = rompimiento_por_fractura
        self.color = color
        self.composicion = composicion
        self.lustre = lustre
        self.specific_gravity = specific_gravity
        self.sistema_cristalino = sistema_cristalino
    
    def silicato(self):
        if "Si" in self.composicion and "O" in self.composicion:
            silicato=True
        else:
            silicato=False
        
        return silicato
    def calcular_densidad_(self):
        densidad= float(self.specific_gravity)*997
        return densidad+"kg/m^3"
    def mostrar_color(self):
       

     # Crear una figura y un eje
        fig, ax = plt.subplots()

        # Establecer el color de fondo
        ax.set_facecolor(self.color)
        ax.set_title('Color más frecuente de'+self.nombre)
        plt.show()
    def impresion_(self):
        if self.rompimiento_por_fractura==False:
            rompimiento="Escisión"
        else:
            rompimiento="Fractura"
        print(f"{self.nombre}tiene dureza de {self.dureza},tipo de rompimiento de {rompimiento},y tiene sistema de organización{self.sistema_cristalino}")
        
    
    


        
