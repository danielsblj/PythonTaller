
import re
from base import isertar
archivo = 'log_trabajoya_prod.log'

class Archivo:
    def insertaDatos(self, archivo):
        if archivo is None:
            print("No se encontro el archivo")
        else:
            linea = []
            with open(archivo) as aux:
                for i, puntero in enumerate(aux.readlines()):
                    if i == 20:
                        break
                    linea.append(puntero)
            print(len(linea))


            #FECHA
            for i, lista in enumerate(linea):
                fecha = re.findall("(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2})", linea[i])
                if len(fecha) == 0:
                    continue


            #URL

            for i, lista in enumerate(linea):
                generado = re.findall(
                    "([\d{4}\-\d{1,2}\-\d{1,2}\s\d{1,2}:\d{1,2}]+[[a-z0-9.:\~\!\@\#\$\%\^\&\*\(\)_\-\=\+\\\/\?\.\:\;\,]*])",
                    linea[i])
                if len(generado) == 0:
                    continue
                else:
                    final = re.findall("[a-z._]+", generado[1])
                    if len(final) == 0:
                        continue
                   # print(final)
            #MENSSAJE
            for i, lista in enumerate(linea):
                mensaje = re.findall("[A-Z]\w*", linea[i])
                #print(mensaje[:1][0])


            #LINEA
            for i, lista in enumerate(linea):
                generado = re.findall(
                    "([\d{4}\-\d{1,2}\-\d{1,2}\s\d{1,2}:\d{1,2}]+[[a-z0-9.:\~\!\@\#\$\%\^\&\*\(\)_\-\=\+\\\/\?\.\:\;\,]*])",
                    linea[i])
                if len(generado) == 0:
                    continue
                else:
                    final2 = re.findall("[0-9]+", generado[1])
                    #print(final2)

        isertar(fecha[0],final[0],mensaje[:1][0],final2[0])


if __name__ == "__main__" :
    file = "log_trabajoya_prod.log"
    ar = Archivo()
    ar.insertaDatos(file)
