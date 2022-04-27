import matplotlib.pyplot as plt
import pandas as pd

class ejercicio:
    def __init__(self,datos):
        self.datos = pd.read_csv(datos)
        
    def calculo_media(self):
        suma = self.datos["Productos(Ni*Xi)"].sum()
        N = self.datos["Cantidad de votantes(Ni)"].sum()
