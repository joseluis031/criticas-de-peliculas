# criticas-de-peliculas

El link de este repositorio es el siguiente:[GitHub](https://github.com/joseluis031/criticas-de-peliculas.git)

## El codigo del ejercicio es el siguiente
```
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


```

## El codigo del main es el siguiente:
```
if __name__ == "__main__":
        main = int(input("Que quieres calcular:la media(1),la desviacion tipica(2),68%(3),95%(4) o 99.7%(5):"))
        from Clases.ejercicio import *
        ejercicio = Ejercicio("Cine1c.csv")
        if main == 1:
            print("La media es: " ,ejercicio.calculo_media())
        elif main == 2:
            print("La desviacion tipica es: " ,ejercicio.calculo_desvi())
        elif main == 3:
            ejercicio.calculo_porcino_68()
        elif main == 4:
            ejercicio.calculo_porcino_95()
        elif main == 5:
            ejercicio.calculo_porcino_99_7()
```
