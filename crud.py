from PyQt5 import QtWidgets, uic 
from PyQt5.QtWidgets import *
import sys
import conexion

aplicacion = QtWidgets.QApplication([])
ventana = uic.loadUi("ventana.ui")
ventana.show()

def agregar():
    print("Agregar")
    objContactos = conexion.contactos()
    objContactos.iniciarConexion()

def eliminar():
    print("eliminar")

def modificar():
    print("modificar")

def cancelar():
    print("cancelar")

ventana.tblContacto.setHorizontalHeaderLabels(['ID', 'Nombre', 'Correo'])
ventana.tblContacto.setEditTriggers(QTableWidget.NoEditTriggers)
ventana.tblContacto.setSelectionBehavior(QTableWidget.SelectRows)

ventana.btnAgregar.clicked.connect(agregar)
ventana.btnEliminar.clicked.connect(eliminar)
ventana.btnModificar.clicked.connect(modificar)
ventana.btnCancelar.clicked.connect(cancelar)

sys.exit(aplicacion.exec())