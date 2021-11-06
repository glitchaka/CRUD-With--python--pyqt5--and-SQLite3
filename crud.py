from PyQt5 import QtWidgets, uic 
from PyQt5.QtWidgets import *
import sys
import conexion


def agregar():
    print("Agregar")
    nombre = ventana.txtNombre.text()
    correo = ventana.txtCorreo.text()
    print (nombre, correo)

    objContactos = conexion.contactos()
    contactos = objContactos.crearContacto((nombre, correo))
    consultar()

def eliminar():
    print("eliminar")

def modificar():
    print("modificar")

def cancelar():
    print("cancelar")

def consultar():
    ventana.tblContacto.setRowCount(0)
    indiceControl = 0

    objContactos = conexion.contactos()
    contactos = objContactos.leerContactos()
    for contacto in contactos:
        ventana.tblContacto.setRowCount(indiceControl + 1)
        ventana.tblContacto.setItem(indiceControl,0, QTableWidgetItem(str(contacto[0])))
        ventana.tblContacto.setItem(indiceControl,1, QTableWidgetItem(str(contacto[1])))
        ventana.tblContacto.setItem(indiceControl,2, QTableWidgetItem(str(contacto[2])))
        indiceControl += 1

aplicacion = QtWidgets.QApplication([])
ventana = uic.loadUi("ventana.ui")
ventana.show()

ventana.tblContacto.setHorizontalHeaderLabels(['ID', 'Nombre', 'Correo'])
ventana.tblContacto.setEditTriggers(QTableWidget.NoEditTriggers)
ventana.tblContacto.setSelectionBehavior(QTableWidget.SelectRows)


ventana.btnAgregar.clicked.connect(agregar)
ventana.btnEliminar.clicked.connect(eliminar)
ventana.btnModificar.clicked.connect(modificar)
ventana.btnCancelar.clicked.connect(cancelar)

sys.exit(aplicacion.exec())