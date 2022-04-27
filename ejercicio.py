import matplotlib.pyplot as plt
import pandas as pd
from math import sqrt

class Ejercicio:
    def __init__(self,datos):
        self.datos = pd.read_csv(datos)
        self.N = self.datos["Cantidad de votantes(Ni)"].sum()
    def calculo_media(self):
        suma = self.datos["Productos(Ni*Xi)"].sum()
        
        return suma/self.N

    def calculo_desvi(self):
        suma_desvi = self.datos["Ni* ((Xi-media)^2)"].sum()
        
        return sqrt(suma_desvi/self.N)
    
    
ejercicio = Ejercicio("Cine1c.csv")
print(ejercicio.calculo_media())
print(ejercicio.calculo_desvi())