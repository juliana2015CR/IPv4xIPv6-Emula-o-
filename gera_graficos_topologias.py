
# coding: utf-8

# In[2]:

from glob import glob
import pandas as pd
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


# In[ ]:




# In[ ]:




# In[ ]:




# In[6]:

def calc(df):
    mean = df[0].mean()
    std = df[0].std()
    margemdeerro = 1.96 * (std / np.sqrt(len(df[0]))) 
    return mean, margemdeerro


# In[ ]:




# In[13]:

def gera_graficos(topologia,cont_total):
    cont=0
    for caminho in arquivos:
        print (caminho)
        arquivos3 = glob(caminho+"*")
        arquivos4 = glob(arquivos2[cont]+"*")
        arquivos3.sort()
        arquivos4.sort()
       
        
        lista = []
        lista.append(pd.read_csv(arquivos3[0], header=None))
        lista.append(pd.read_csv(arquivos4[0], header=None))
        lista.append(pd.read_csv(arquivos3[1], header=None))
        lista.append(pd.read_csv(arquivos4[1], header=None))
        lista.append(pd.read_csv(arquivos3[2], header=None))
        lista.append(pd.read_csv(arquivos4[2], header=None))
        
        print (arquivos3[1],arquivos3[1])
            
        lista2 = []
        for i in lista:
            print (lista2)
            lista2.append(calc(i))
        #x = np.arange(6)
        x = [0,11,21]
        cliente = caminho.split("/")[2].split("-")[0]
        intervalo = float(caminho.split("/")[2].split("-")[1])/100
        labels=['1000 Bytes','1500 Bytes', '2000 Bytes']
        plt.errorbar(0,lista2[0][0], yerr=lista2[1][1], linestyle='', capsize=6,elinewidth="1", marker='o',fmt='o', label="IPv4", color='k' )
        plt.errorbar(0.9,lista2[1][0], yerr=lista2[1][1], linestyle='',capsize=6,elinewidth="1",marker='o', fmt='o', label="IPv6", color='r')
        plt.errorbar(11,lista2[2][0], yerr=lista2[2][1], linestyle='',capsize=6,elinewidth="1",marker='o', fmt='o',color='k')
        plt.errorbar(11.9,lista2[3][0], yerr=lista2[3][1], linestyle='',capsize=6,elinewidth="1",marker='o', fmt='o',color='r')
        plt.errorbar(21,lista2[4][0], yerr=lista2[4][1], linestyle='',capsize=6,elinewidth="1",marker='o', fmt='o',color='k')
        plt.errorbar(21.9,lista2[5][0], yerr=lista2[5][1], linestyle='',capsize=6,elinewidth="1",marker='o', fmt='o',color='r')
        plt.xticks(x,labels)
        plt.legend()
    

        #plt.plot(x, lista, marker="o")
        #plt.plot(x, teste2[0])
    
        plt.title("Gráfico "+str(cont_total)+" - "+topologia+" - Ida e Volta de pacotes\n UDP com "+cliente+" cliente(s) e intervalo de "+str(intervalo)+"s")
        plt.savefig(topologia+"/Graficos IdaeVolta/Gráfico "+str(cont_total)+" - Envio de pacotes UDP com "+cliente+" cliente(s) e intervalo de "+str(intervalo)+"s.png")
        cont_total+=1
        cont+=1
        plt.show()
    return cont_total


# In[15]:

cont_total=1
listaarq=['Halteres','Manhattan','RNP','Internet2']
for i in listaarq:
        arquivos = glob(i+"/IPv4/*/")
        arquivos2 = glob(i+"/IPv6/*/")
        arquivos.sort()
        arquivos2.sort()
        cont_total = gera_graficos(i,cont_total)
        


# In[ ]:



