"""
ESTE SCRIPT SIRVE PARA CONTROLAR LOS BOTONES DE LA BARRA SUPERIOR Y CONTROLAR LA VENTANA
"""
controlVentana = 0

from PySide2.QtCore import *

def cerrar(programa):
    programa.close()

def maximizarVentana(programa):
    programa.showMaximized()

def normalizarVentana(programa):
    programa.showNormal()

def minimizarVentana(programa):
    programa.showMinimized()

def estadoVentana(programa):
    global controlVentana
    if controlVentana:
        normalizarVentana(programa)
        controlVentana = 0
    else:
        maximizarVentana(programa)
        controlVentana = 1
