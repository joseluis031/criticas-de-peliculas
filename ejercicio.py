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
    
    def calculo_porcino_68(self):
        intervalo = []
        inferior = self.calculo_media() - self.calculo_desvi()
        superior = self.calculo_media() + self.calculo_desvi()
        for i in range(6):
            if self.datos["Opinion(Xi)"][i]>inferior and self.datos["Opinion(Xi)"][i]<superior:
                intervalo.append(self.datos["Cantidad de votantes(Ni)"][i])
        suma_intervalo = sum(intervalo)
        return print("El porcentaje es {}%".format(suma_intervalo/self.N))
    
    def calculo_porcino_95(self):
        intervalo = []
        inferior = self.calculo_media() - 2*self.calculo_desvi()
        superior = self.calculo_media() + 2*self.calculo_desvi()
        for i in range(6):
            if self.datos["Opinion(Xi)"][i]>inferior and self.datos["Opinion(Xi)"][i]<superior:
                intervalo.append(self.datos["Cantidad de votantes(Ni)"][i])
        suma_intervalo = sum(intervalo)
        return print("El porcentaje es {}%".format(suma_intervalo/self.N))
    
    def calculo_porcino_99_7(self):
        intervalo = []
        inferior = self.calculo_media() - 3*self.calculo_desvi()
        superior = self.calculo_media() + 3*self.calculo_desvi()
        for i in range(6):
            if self.datos["Opinion(Xi)"][i]>inferior and self.datos["Opinion(Xi)"][i]<superior:
                intervalo.append(self.datos["Cantidad de votantes(Ni)"][i])
        suma_intervalo = sum(intervalo)
        return print("El porcentaje es {}%".format(suma_intervalo/self.N))


ejercicio = Ejercicio("Cine1c.csv")
print("La media es: " ,ejercicio.calculo_media())
print("La desviacion tipica es: " ,ejercicio.calculo_desvi())
ejercicio.calculo_porcino_68()
ejercicio.calculo_porcino_95()
ejercicio.calculo_porcino_99_7()