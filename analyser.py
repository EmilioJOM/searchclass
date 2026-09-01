import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt

def analyser(url):
    print(url)

    try:
        response = requests.get(url)

        if response.status_code == 200:

            html_content = response.text  
            soup = BeautifulSoup(html_content, "html.parser")
            aula = soup.find("h5").text.split(" ")[1]
            output = [aula,"","","","","","","","","",""]
            aa = soup.find_all("h4")
            bb = soup.find_all("h3")

            '''print("\n\nH4\n")
            for i in soup.find_all("h4"):
                print(i.text)
            print("\n\nH3\n")
            for i in soup.find_all("h3"):
                print(i.text)
            print()'''
            def dentroHorario(soup):
                horario = 0 
                c = True    
                indice = 0

                for a in aa:
                    if a.text[0].isdecimal():
                        print("horario:",a.text)
                        if a.text == "08:15 a 12:15" or a.text == "07:45 a 11:45":
                            print("turno mañana")
                            horario = 0
                        elif a.text == "14:00 a 18:00" or a.text == "13:30 a 17:30":
                            print("turno tarde")
                            horario = 2
                        elif a.text == "18:30 a 22:00" or a.text == "18:00 a 21:00" or a.text == "18:30 a 22:00":
                            print("turno noche")
                            horario = 4
                        elif c:
                            print("extra1")
                            horario = 6
                            c = False
                        else:
                            print("extra2")
                            horario = 8
                        continue

                    if len(bb) <= 1 or len(bb) < indice+1:
                        continue
                    elif "Sede" in bb[indice].text:
                        indice += 1
                    else:
                        output[1+horario] = bb[indice].text
                        print(bb[indice].text)
                        indice = indice + 1
                    
                    if a.text == "Docentes:":
                        continue
                    print("profesor:",a.text)
                    output[2+horario] = output[2+horario]+" "+(a.text)
                    

                print(output)
                return output
            def fueraHorario(soup):
                b=False
                horario = 0 
                c = True    
                indice = 0
                for a in aa:
                    if a.text[0].isdecimal():
                        print("horario:",a.text)
                        if a.text == "08:15 a 12:15" or a.text == "07:45 a 11:45":
                            print("turno mañana")
                            horario = 0
                        elif a.text == "14:00 a 18:00":
                            print("turno tarde")
                            horario = 2
                        elif a.text == "18:30 a 22:00" or a.text == "18:00 a 21:00":
                            print("turno noche")
                            horario = 4
                        elif c:
                            print("extra1")
                            horario = 6
                            c = False
                        else:
                            print("extra2")
                            horario = 8

                        b = True
                        continue
                    
                    if b:
                        print("materia:",a.text)
                        output[1+horario] = a.text
                        b = False
                        continue
                    if not b:
                        print("profesor:",a.text)
                        output[2+horario] = output[2+horario]+" "+(a.text)
                    

                print(output)
                return output

            if "Docentes:" in [i.text for i in aa]:
                return dentroHorario(soup)
            else:
                return fueraHorario(soup)

        else:
            print(f"Error al acceder a la página: {response.status_code}")
            return None
    except:
        return None
    
# analyser(f"https://www.webcampus.uade.edu.ar/QrAula/5ZqpEJNjISs%3d-MjE3")
# analyser(f"https://www.webcampus.uade.edu.ar/QrAula/357SLmXZK8g%3d-MjY%3d")

