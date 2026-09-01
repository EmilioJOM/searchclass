import csv
import os
from datetime import datetime

def diaActual():
    i = datetime.weekday(datetime.date(datetime.today()))
    hoy = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"][i]
    return hoy

def iniciarGrabacion():
    carpeta = "BBDD/"
    dia = diaActual()
    registro(dia)
    archivo = carpeta + dia + ".csv"
    if archivo not in os.listdir():
        print("OMG!!!! dia nunca escaneado!")
    open(archivo,"w").close()
    return open(archivo,"a")

def guardarDato(dato, file):
    csv.writer(file).writerow(dato)


def registro(dia): 
    datos = []
    open("registro.csv","w").close()
    registro = open("registro.csv","r")
    datos = list(csv.reader(registro))
    registro.close()

    actualizado = False
    for row in datos:
        if row[0] == dia:
            row[1] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Actualizar la fecha
            actualizado = True
            break
    if not actualizado:
        datos.append([dia, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
        
    registro = open("registro.csv","w")
    newLog = csv.writer(registro)
    newLog.writerows(datos)
    registro.close()