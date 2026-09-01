import radar
import get_result

comando = ""
while (comando != "exit") and (comando != "salir"):
    print("ingrese un comando o help para tener ayuda")
    comando = input("> ")
    if comando == "escanear":
        radar.escanear()
    if comando == "aulas":
        get_result.aulas()
    elif comando.split(" ")[0] == "aulas":
        get_result.aulasDia(comando.split(" ")[-1])
    
    argumento = " ".join(comando.split(" ")[2:])

    if comando.split(" ")[:2] == ["buscar","aula"]:
        print("buscando")
        get_result.buscarAula(argumento)
    if comando.split(" ")[:2] == ["buscar","materia"]:
        get_result.buscarMateria(argumento)
    if comando.split(" ")[:2] == ["buscar","profesor"]:
        get_result.buscarProfesor(argumento)

    if comando.split(" ")[:2] == ["buscar","piso"]:
        tempArg = argumento.split(" ")
        if len(tempArg) == 2:
            get_result.buscarPiso(tempArg[0], tempArg[1])
        else:
            get_result.buscarPiso(piso=argumento)
    if comando.split(" ")[:2] == ["buscar","edificio"]:
        tempArg = argumento.split(" ")
        if len(tempArg) == 2:
            get_result.buscarEdificio(tempArg[0], tempArg[1])
        else:
            get_result.buscarEdificio(edificio=argumento)

    if comando.split(" ")[:2] == ["buscar","aulaVacia"]:
        tempArg = argumento.split(" ")
        print (tempArg)
        turno = tempArg[0]
        piso = None
        dia = None
        try:
            piso = tempArg[1]
        except:
            pass
        try:
            dia = tempArg[2]
        except:
            pass

        get_result.buscar_AulasVacias(turno, piso, dia)


    if comando == "help" or comando == "ayuda":
        print("""
escanear                    escanea todos las aulas y actualiza la 
                            informacion de las clases del dia de hoy
                            Warning: hacerlo en la mañana, ya que a 
                            medida que pasa el dia, las clases pasadas 
                            no se registran

buscar aula [numero]        devuelve las clases que se dan en dicha aula
              
buscar materia [materia]  devuelve las aulas donde se dan dicha materia
              
buscar profesor [profesor]  devuelve las aulas donde esta el profesor

buscar piso [nro piso] [dia]

buscar edificio [nro edificio] [dia]

buscar aulaVacia [turno] [nro piso] [dia]

aulas                       devuelve una lista con todos los salones registrados
              
help | ayuda                devuelve este mensaje
        
exit | salir                cierra el programa
""")