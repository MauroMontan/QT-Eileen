from .conexion import BaseDeDatos
from PySide2.QtWidgets import QTableWidgetItem

bd = BaseDeDatos()

def cargarTabla(tabla):
    global bd

    datos = bd.getDatos()
    tabla.setRowCount(len(datos))
    tabla.setColumnCount(9)
    for fila in range(len(datos)):
        for columna in range(len(datos[fila])):
            tabla.setItem(fila, columna, QTableWidgetItem(str(datos[fila][columna])))
