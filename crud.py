from PyQt5 import QtWidgets, uic 
from PyQt5.QtWidgets import *
import sys
import conexion

def agregar():
    print("Agregar")
    nombre = ventana.txtNombre.text()
    correo = ventana.txtCorreo.text()
    
    objContactos = conexion.contactos()
    contactos = objContactos.crearContacto((nombre, correo))
    consultar()

def eliminar():
    print("eliminar")
    id = ventana.txtId.text()
    objContactos = conexion.contactos()
    contactos = objContactos.borrarContacto(id)
    consultar()
    

def modificar():
    print("modificar")
    id = ventana.txtId.text()
    nombre = ventana.txtNombre.text()
    correo = ventana.txtCorreo.text()
    
    objContactos = conexion.contactos()
    contactos = objContactos.modificarContacto((nombre, correo,id))
    consultar()

def cancelar():
    print("cancelar")
    consultar()

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

    ventana.txtId.setText("")
    ventana.txtNombre.setText("")
    ventana.txtCorreo.setText("")

    ventana.btnAgregar.setEnabled(True)
    ventana.btnEliminar.setEnabled(False)
    ventana.btnModificar.setEnabled(False)
    ventana.btnCancelar.setEnabled(False)

def seleccionar():
    id=ventana.tblContacto.selectedIndexes()[0].data()  #obtiene el id del contacto seleccionado
    nombre =ventana.tblContacto.selectedIndexes()[1].data()
    correo =ventana.tblContacto.selectedIndexes()[2].data()

    print(id, nombre, correo)

    ventana.txtId.setText(id)
    ventana.txtNombre.setText(nombre)
    ventana.txtCorreo.setText(correo)

    ventana.btnAgregar.setEnabled(False)
    ventana.btnEliminar.setEnabled(True)
    ventana.btnModificar.setEnabled(True)
    ventana.btnCancelar.setEnabled(True)


aplicacion = QtWidgets.QApplication([])
ventana = uic.loadUi("ventana.ui")
ventana.show()
consultar()

ventana.tblContacto.setHorizontalHeaderLabels(['ID', 'Nombre', 'Correo'])
ventana.tblContacto.setEditTriggers(QTableWidget.NoEditTriggers)
ventana.tblContacto.setSelectionBehavior(QTableWidget.SelectRows)

ventana.tblContacto.cellClicked.connect(seleccionar)

ventana.btnAgregar.clicked.connect(agregar)
ventana.btnEliminar.clicked.connect(eliminar)
ventana.btnModificar.clicked.connect(modificar)
ventana.btnCancelar.clicked.connect(cancelar)

sys.exit(aplicacion.exec())