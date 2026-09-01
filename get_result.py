import csv
import os
import condicion

def buscar(condicion):
    output = []
    dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
    carpeta = "BBDD/"
    for dia in dias:
        ruta = os.path.join(carpeta, dia + ".csv")
        if os.path.exists(ruta):
            file = open(ruta,"r")
            reader = csv.reader(file)
            condicion.dia = dia
            for line in reader:
                condicion.linea = line
                if condicion.probar():
                    resultado = condicion.resultado
                    output.append(resultado)
    return output

def buscarAula(aula):
    condicionante = condicion.Condicion()
    condicionante.var = aula
    def funcion():
        if len(condicionante.linea) > 3:
            if str(condicionante.var) == condicionante.linea[0]:
                condicionante.resultado = condicionante.linea
                condicionante.resultado.append(condicionante.dia)
                return True
    condicionante.probar=funcion
    output = buscar(condicionante)

    with open("aulas link enum.txt","r") as file:
        file.readline()
        for line in file:
            if str(aula) in line:
                print(line)

    for line in output:
        print("<:",line[0],line[-1])
        print("turno mañana: ")
        print("    materia:",line[1])
        print("    profesor/es:",line[2])
        print("turno tarde: ")
        print("    materia:",line[3])
        print("    profesor/es:",line[4])
        print("turno noche: ")
        print("    materia:",line[5])
        print("    profesor/es:",line[6])
        print("turno extra1: ")
        print("    materia:",line[7])
        print("    profesor/es:",line[8])
        print("turno extra2: ")
        print("    materia:",line[9])
        print("    profesor/es:",line[10])


def aulas():
    condicionante = condicion.Condicion()
    
    def funcion():
        if condicionante.var != condicionante.dia:
            condicionante.var = condicionante.dia
            print(condicionante.var)
        if len(condicionante.linea) > 3:
            condicionante.resultado = condicionante.linea[0]
            return True
    condicionante.probar=funcion
    output = buscar(condicionante)
    for  i, line in enumerate(output):
        print("<:",i+1,line)
    print(len(output))

def aulasDia(dia):
    condicionante = condicion.Condicion()
    condicionante.var = dia
    def funcion():
        
        if (len(condicionante.linea) > 3) and (condicionante.var == condicionante.dia):
            condicionante.resultado = condicionante.linea[0]
            return True
    condicionante.probar=funcion
    output = buscar(condicionante)
    for  i, line in enumerate(output):
        print("<:",i+1,line)
    print(len(output))

def buscarMateria(materia):
    condicionante = condicion.Condicion()
    condicionante.var = materia
    def funcion():
        
        if len(condicionante.linea) > 3:
            for elemento in condicionante.linea:
                if str(condicionante.var) in elemento:
                    condicionante.resultado = condicionante.linea
                    return True
    condicionante.probar=funcion
    output = buscar(condicionante)
    for line in output:
        print("<:",line)

def buscarProfesor(profesor):
    condicionante = condicion.Condicion()
    condicionante.var = profesor
    def funcion():
        
        if len(condicionante.linea) > 3:
            for elemento in condicionante.linea:
                if str(condicionante.var) in elemento:
                    condicionante.resultado = condicionante.linea
                    return True
    condicionante.probar=funcion
    output = buscar(condicionante)
    for line in output:
        print("<:",line)

def buscarPiso(piso, dia=None):
    condicionante = condicion.Condicion()
    condicionante.var = (piso,dia)
    def funcion():
        
        if len(condicionante.linea) > 3:
            if condicionante.var[1] != None:
                if condicionante.var[0] == condicionante.linea[0][:-2] and condicionante.var[1] == condicionante.dia:
                    condicionante.resultado = condicionante.linea
                    return True
            else:
                if condicionante.var[0] == condicionante.linea[0][:-2]:
                    condicionante.resultado = condicionante.linea
                    return True
    condicionante.probar=funcion
    output = buscar(condicionante)
    for line in output:
        print("<:",line)

def buscarEdificio(edificio, dia=None):
    condicionante = condicion.Condicion()
    condicionante.var = (edificio,dia)
    def funcion():
        
        if len(condicionante.linea) > 3:
            if condicionante.var[1] != None:
                if condicionante.var[0] == condicionante.linea[0][-2] and condicionante.var[1] == condicionante.dia:
                    condicionante.resultado = condicionante.linea
                    return True
            else:
                if condicionante.var[0] == condicionante.linea[0][-2]:
                    condicionante.resultado = condicionante.linea
                    return True
    condicionante.probar=funcion
    output = buscar(condicionante)
    for line in output:
        print("<:",line)

def buscar_AulasVacias(turno, piso=None, dia=None):
    condicionante = condicion.Condicion()
    turnoDicc = {
            'mañana': 1,
            'tarde': 3,
            'noche': 5
        }

    condicionante.var = {
        'dia': dia,
        'piso': piso,
        'turno': turnoDicc[turno]
    }
    print(condicionante.var)
    def funcion():
        
        if len(condicionante.linea) < 3:
            return False
        if condicionante.var['piso'] != None and condicionante.var['piso'] != '':
            if condicionante.var['piso'] != condicionante.linea[0][-3]:
                return False
        if condicionante.var['dia'] != None and condicionante.var['dia'] != '':
            if condicionante.var['dia'] != condicionante.dia:
                return False
        if condicionante.linea[condicionante.var['turno']] != '':
            return False
        condicionante.resultado = condicionante.linea
        return True

    condicionante.probar=funcion
    output = buscar(condicionante)
    for line in output:
        print("<:",line)