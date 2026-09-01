import analyser
import save_result
import time

def escanear():
    file = save_result.iniciarGrabacion()
    with open("aulasLinks.txt","r") as aulasLinks:
        salon = aulasLinks.readline()[:-1]
        while salon != "":
            output = analyser.analyser(salon)
            if output != None:
                save_result.guardarDato(output,file)
            salon = aulasLinks.readline()[:-1]
    file.close()
