
import numpy as np
import matplotlib.pyplot as plt
from mineral import Mineral 

def crear_objetos():
    with open('minerales.txt', 'r', encoding='utf-8' ) as fichero:
        minerales =[]  # Crear un arreglo vacío
        lineas = fichero.readlines()[1:18]
        for linea in lineas:
            campos = linea.strip().split('\t')  # Dividir la línea en campos
            material = Mineral(*campos)  # Crear un objeto Material con los campos
            minerales.append(material)
            materiales_array = np.array(minerales)
    return materiales_array

def contar_silicatos_en_array(minerales_array):
    contador_silicatos = 0
    for mineral in minerales_array:
        if mineral.silicato():
            contador_silicatos += 1
    return contador_silicatos

def calcular_densidad_promedio(minerales_array):
    densidad_total = 0
    for mineral in minerales_array:
        densidad_total+= mineral.calcular_densidad_()
        densidad_promedio=densidad_total/len(minerales_array)
    return(round(densidad_promedio,2))


    


