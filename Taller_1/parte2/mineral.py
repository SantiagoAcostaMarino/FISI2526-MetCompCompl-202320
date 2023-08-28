{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Parte 2 taller"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "CLASE MINERAL"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Mineral:\n",
    "    def init(self,nombre,dureza,ilustre,rompimiento_por_fractura,color,composicion,sistema_cristalino,specific_gravity):\n",
    "        self.nombre=nombre\n",
    "        self.dureza=dureza\n",
    "        self.ilustre=ilustre\n",
    "        self.rompimiento_por_fractura=rompimiento_por_fractura\n",
    "        self.color=color\n",
    "        self.composicion=composicion\n",
    "        self.sistema_cristalino=sistema_cristalino\n",
    "        self.specific_gravity=specific_gravity\n",
    "    \n",
    "    def silicato(self):\n",
    "        if \"Si\" in self.composicion and \"O\" in self.composicion:\n",
    "            silicato=True\n",
    "        else:\n",
    "            silicato=False\n",
    "        \n",
    "        return silicato\n",
    "    def calcular_densidad_(self):\n",
    "        densidad= float(self.specific_gravity)*997\n",
    "        return densidad+\"kg/m^3\"\n",
    "    def mostrar_color(self):\n",
    "        x = []\n",
    "        y = []\n",
    "\n",
    "        # Crear una figura y un eje\n",
    "        fig, ax = plt.subplots()\n",
    "\n",
    "        # Establecer el color de fondo\n",
    "        ax.set_facecolor(self.color)\n",
    "        ax.set_title('Color más frecuente de'+self.nombre)\n",
    "        plt.show()\n",
    "    def impresion_(self):\n",
    "        dureza=self.dureza\n",
    "        if self.rompimiento_por_fractura==False:\n",
    "            rompimiento=\"Escisión\"\n",
    "        else:\n",
    "            rompimiento=\"Fractura\"\n",
    "        organizacion=self.sistema_cristalino\n",
    "        print(dureza,rompimiento,rompimiento)\n",
    "    \n",
    "    \n",
    "\n",
    "\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "No handles with labels found to put in legend.\n"
     ]
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "def create_colored_plot(background_color):\n",
    "    # Crear datos de ejemplo\n",
    "    x = []\n",
    "    y = []\n",
    "\n",
    "    # Crear una figura y un eje\n",
    "    fig, ax = plt.subplots()\n",
    "\n",
    "    # Establecer el color de fondo\n",
    "    ax.set_facecolor(background_color)\n",
    "\n",
    "    # Agregar datos al gráfico\n",
    "    \n",
    "\n",
    "    # Agregar etiquetas y título\n",
    "\n",
    "    ax.set_title('Gráfico con Fondo de Color')\n",
    "\n",
    "    # Agregar leyenda\n",
    "    ax.legend()\n",
    "\n",
    "    # Mostrar el gráfico\n",
    "    plt.show()\n",
    "create_colored_plot(\"#E8DE35\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
