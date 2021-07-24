
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

def validar(LINEHORARIO,LINEURL,BOTON):
    control=True
    if LINEHORARIO.text() =="":
        LINEHORARIO.setStyleSheet("border:null;")
        LINEURL.setEnabled(False)
        LINEURL.setText("")
    if LINEHORARIO.text() != "":
        LINEURL.setEnabled(True)
    for i in LINEHORARIO.text():
        if i in "abcdefghijklmnñopqrstuvwxyz!''%?¡;/#*+<>ABCDEFGHIJKLMNÑOPQRSTUVWXYZ|@|°¬":
            control = False
        if control:
            LINEHORARIO.setStyleSheet("border:2px solid green;")
            BOTON.show()
        else:
            LINEHORARIO.setStyleSheet("border:2px solid red;")
            LINEHORARIO.setToolTip(QCoreApplication.translate("MainWindow", u"respeta este formato 00:00-00:00", None))
            BOTON.hide()


def materiaValidar(MATERIALINE,BOTON):
    control=True
    if MATERIALINE.text() =="":
        control=False

    if control:
        MATERIALINE.setStyleSheet("border:2px solid green;")
        BOTON.show()
    else:
        MATERIALINE.setStyleSheet("border:2px solid red;")
        BOTON.hide()
