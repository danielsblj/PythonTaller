 def insertarFecha(self, archivo):
        if archivo is None:
            print("No se encontro el archivo")
        else:
            linea = []
            with open(archivo) as aux:
                for i, puntero in enumerate(aux.readlines()):
                    linea.append(puntero)
            print(len(linea))

            for i, lista in enumerate(linea):
                fecha = re.findall("(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2})", linea[i])
                if len(fecha) == 0:
                    continue
                else:
                    print(fecha[0])

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
                    print(final)



    def insertarRegistro(self, file):
        linea = []
        archivo = "log_trabajoya_prod.log"
        with open(archivo) as aux:
            for i, line in enumerate(aux.readlines()):
                if i == 20:
                    break
                linea.append(line)
        len(linea)

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
                print(final)

    def insertarMensaje(self, archivo):
        lines = []
        with open(archivo) as aux:
            for i, line in enumerate(aux.readlines()):
                if i == 20:
                    break
                lines.append(line)
        len(lines)

        for i, lista in enumerate(lines):
            mensaje = re.findall("[A-Z]\w*", lines[i])
            print(mensaje[:1][0])

    def insertarLinea(self, file):
        linea = []
        archivo = "log_trabajoya_prod.log"
        with open(archivo) as aux:
            for i, line in enumerate(aux.readlines()):
                linea.append(line)
        len(linea)

        for i, lista in enumerate(linea):
            generado = re.findall(
                "([\d{4}\-\d{1,2}\-\d{1,2}\s\d{1,2}:\d{1,2}]+[[a-z0-9.:\~\!\@\#\$\%\^\&\*\(\)_\-\=\+\\\/\?\.\:\;\,]*])",
                linea[i])
            if len(generado) == 0:
                continue
            else:
                final = re.findall("[0-9]+", generado[1])
                print(final)
                return





if __name__ == "__main__" :
    file = "log_trabajoya_prod.log"
    ar = Archivo()
    #ar.insertarFecha(file)
    print('*************************************')
    ar.insertarMensaje(file)
    print('*************************************')
    #ar.insertarRegistro(file)
    print('*************************************')
   # ar.insertarLinea(file)