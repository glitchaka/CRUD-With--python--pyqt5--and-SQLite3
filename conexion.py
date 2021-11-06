from os import error
import sqlite3
from sqlite3.dbapi2 import connect

class contactos:
    def iniciarConexion(self):
        conexion = sqlite3.connect("sistema.s3db")
        conexion.text_factory = lambda b: b.decode(errors="ignore")

        cursor = conexion.cursor()
        sentenciaSQL = "SELECT * FROM contactos"
        cursor.execute(sentenciaSQL)
        print(cursor.fetchall())