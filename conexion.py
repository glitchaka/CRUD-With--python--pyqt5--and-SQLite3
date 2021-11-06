from os import error
import sqlite3
from sqlite3.dbapi2 import connect

class contactos:
    def iniciarConexion(self):
        conexion = sqlite3.connect("sistema.s3db")              
        conexion.text_factory = lambda b: b.decode(errors="ignore") # Para evitar problemas con caracteres especiales
        return conexion     # Retorna la conexion a la base de datos

    def leerContactos(self):
        conexion = self.iniciarConexion()
        cursor = conexion.cursor()                         # Crea un cursor
        sentencialSQL = "SELECT * FROM contactos"    
        cursor.execute(sentencialSQL)
        return cursor.fetchall()