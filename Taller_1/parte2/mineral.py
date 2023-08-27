# %% [markdown]
# Parte 2 taller

# %%
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# CLASE MINERAL

# %%
class Mineral:
    def init(self,nombre,dureza,ilustre,rompimiento_por_fractura,color,composicion,sistema_cristalino,specific_gravity):
        self.nombre=nombre
        self.dureza=dureza
        self.ilustre=ilustre
        self.rompimiento_por_fractura=rompimiento_por_fractura
        self.color=color
        self.composicion=composicion
        self.sistema_cristalino=sistema_cristalino
        self.specific_gravity=specific_gravity
    
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
        x = []
        y = []

        # Crear una figura y un eje
        fig, ax = plt.subplots()

        # Establecer el color de fondo
        ax.set_facecolor(self.color)
        ax.set_title('Color más frecuente de'+self.nombre)
        plt.show()
    def impresion_(self):
        dureza=self.dureza
        if self.rompimiento_por_fractura==False:
            rompimiento="Escisión"
        else:
            rompimiento="Fractura"
        organizacion=self.sistema_cristalino
        print(dureza,rompimiento,rompimiento)
    
    


        

