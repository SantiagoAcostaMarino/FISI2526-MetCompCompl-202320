
import numpy as np
import matplotlib.pyplot as plt
from mineral  import Mineral





class ExpansionTermicaMineral(Mineral):
    def __init__(self,archivo):
        self.archivo=archivo
    def carga_archivo(self):
        with open (self.archivo,'r',encoding='utf-8') as fichero:
            Temp=[]
            Vol=[]
            lineas = fichero.readlines()[1:]
            for linea in lineas:
                Temp.append(float(linea.strip().split(',')[0]))
                Vol.append(float(linea.strip().split(',')[1]))   
        Temp_array=np.array(Temp)
        Vol_array=np.array(Vol)
        
        return [Temp_array,Vol_array]
    def alpha(self):
        
        datos_D=ExpansionTermicaMineral.carga_archivo(self)
        Temp=datos_D[0]
        temp_Alphas  =  Temp[:-1]
        Vol=datos_D[1]
        alphas=np.array([])
        error=0
        for i in range(0,len(datos_D[0])-1):
            
            derivadacentral= ((Vol[i+1])-Vol[i])/((Temp[i+1]-Temp[i]))           
            alphas=np.append(alphas,(1/Vol[i]*derivadacentral))
        
        error=np.std(alphas)/np.sqrt(len(alphas))
        
        fig,axs=plt.subplots(nrows=1,ncols=2,figsize=(18,4.5))
        axs[0].scatter(Temp,Vol,c='r')
        axs[0].set_ylabel(r'Volumen cm^3')
        axs[0].set_xlabel('Temperatura °C')
        axs[0].set_title('V vs T')
        axs[1].scatter(temp_Alphas,alphas,c='g')
        axs[1].set_ylabel(r'Coeficiente dilatacion °C^-1')
        axs[1].set_xlabel('Temperatura °C')
        axs[1].set_title('a vs T')
        return np.mean(alphas),error,fig
        
        


        

    
        
        
    






