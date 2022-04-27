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
