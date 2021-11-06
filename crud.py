from PyQt5 import QtWidgets, uic 
from PyQt5.QtWidgets import *
import sys
import conexion

aplicacion = QtWidgets.QApplication([])
ventana = uic.loadUi("ventana.ui")
ventana.show()

def agregar():
    print("Agregar")
   


def eliminar():
    print("eliminar")

def modificar():
    print("modificar")

def cancelar():
    print("cancelar")

def consultar():
    ventana.tblContactos.setRowCount(0)
    indiceControl = 0

    objContactos = conexion.Contactos()
    objContactos.leerContactos()
    for contacto in objContactos.listaContactos:
        ventana.tblContactos.setRowCount(indiceControl + 1)
        ventana.tblContactos.setItem(indiceControl,0, QTableWidgetItem(str(contacto[0])))
        ventana.tblContactos.setItem(indiceControl,1, QTableWidgetItem(str(contacto[1])))
        ventana.tblContactos.setItem(indiceControl,2, QTableWidgetItem(str(contacto[2])))
        indiceControl += 1


ventana.tblContacto.setHorizontalHeaderLabels(['ID', 'Nombre', 'Correo'])
ventana.tblContacto.setEditTriggers(QTableWidget.NoEditTriggers)
ventana.tblContacto.setSelectionBehavior(QTableWidget.SelectRows)

ventana.btnAgregar.clicked.connect(agregar)
ventana.btnEliminar.clicked.connect(eliminar)
ventana.btnModificar.clicked.connect(modificar)
ventana.btnCancelar.clicked.connect(cancelar)

sys.exit(aplicacion.exec())