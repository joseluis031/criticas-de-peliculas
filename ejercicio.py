import matplotlib.pyplot as plt
import pandas as pd

class Ejercicio:
    def __init__(self,datos):
        self.datos = pd.read_csv(datos)
        
    def calculo_media(self):
        suma = self.datos["Productos(Ni*Xi)"].sum()
        N = self.datos["Cantidad de votantes(Ni)"].sum()
        return suma/N

ejercicio = Ejercicio("Cine1c.csv")
print(ejercicio.calculo_media())