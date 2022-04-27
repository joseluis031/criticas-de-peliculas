from collections import Counter
from math import *
import matplotlib.pyplot as plt
import csv
class ejercicio:
    def __init__(self,datos):
        self.datos = datos
        
    def calculo_media(self):
        with open('calificaciones.csv') as self.File:
            reader = csv.reader(self.File, delimiter=';')
            next(reader, None)
            for i in reader:
                