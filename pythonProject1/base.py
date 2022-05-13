import sqlite3
from sqlite3 import Error

def isertar(fecha, tipo_mensaje, archivo, linea):
    conexion = sqlite3.connect('pythonBD.db')
    cur = conexion.cursor()
    sentencia= f"INSERT INTO file( fecha,tipo_mensaje, archivo,linea) VALUES ('{fecha}', '{tipo_mensaje}', '{archivo}','{linea}')"
    print(sentencia)
    cur.execute(sentencia)
    conexion.commit()
    conexion.close()

