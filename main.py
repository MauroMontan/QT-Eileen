from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
import time
import subprocess
import pandas as pd

from E import Ui_MainWindow
from scripts.windowBeh import cerrar,minimizarVentana,estadoVentana
from scripts.crearMateria import guardar
from scripts.validar import validar, materiaValidar
from Model.conexion import BaseDeDatos
from Model.cargar import cargarTabla
from alarmBeh import hola
import subprocess as s
import webbrowser
import os
bd=BaseDeDatos()

xd=hola()





class TableW(QMainWindow):

    """docstring for TableW."""

    def __init__(self):
        global xd
        super(TableW, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.selectedItem = None

        self.controlVentana = 0
        self.ui.tableWidget.verticalHeader().hide()

        self.comboMaterias=bd.buscarNombreMateria()

        cargarTabla(self.ui.tableWidget)

        self.timer =QTimer()
        self.timer.timeout.connect(lambda:self.working())
        self.timer.start(1000)



        self.ui.pushButton.clicked.connect(lambda:cerrar(self))
        self.ui.pushButton_3.clicked.connect(lambda:minimizarVentana(self))
        self.ui.pushButton_2.clicked.connect(lambda:estadoVentana(self))
        self.ui.pushButton_13.clicked.connect(self.IndexCeropage)
        self.ui.pushButton_14.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_12.clicked.connect(lambda:QMessageBox.information(self,"Información","la sintaxis para los Horarios tiene que ser \n '00:00-00:00'\n en un formato de 24hrs"))
        self.ui.lineEdit_2.setEnabled(False)
        self.ui.lineEdit_3.setEnabled(False)
        self.ui.lineEdit_4.setEnabled(False)
        self.ui.lineEdit_5.setEnabled(False)
        self.ui.lineEdit_6.setEnabled(False)
        self.ui.lineEdit_7.setEnabled(False)
        self.ui.lineEdit_8.setEnabled(False)


        self.ui.comboBox_3.addItems(self.comboMaterias)
        self.ui.comboBox.addItems(self.comboMaterias)
        self.ui.pushButton_5.clicked.connect(self.refresh_)
        self.ui.comboBox.currentTextChanged.connect(self.on_combobox_func)

        self.ui.linLunes.textChanged.connect(lambda:validar(self.ui.linLunes,self.ui.lineEdit_2,self.ui.pushButton_5))
        self.ui.lineMartes.textChanged.connect(lambda:validar(self.ui.lineMartes,self.ui.lineEdit_3,self.ui.pushButton_5))
        self.ui.linMiercoles.textChanged.connect(lambda:validar(self.ui.linMiercoles,self.ui.lineEdit_4,self.ui.pushButton_5))
        self.ui.lineJueves.textChanged.connect(lambda:validar(self.ui.lineJueves,self.ui.lineEdit_5,self.ui.pushButton_5))
        self.ui.lineViernes.textChanged.connect(lambda:validar(self.ui.lineViernes,self.ui.lineEdit_6,self.ui.pushButton_5))
        self.ui.lineSabado.textChanged.connect(lambda:validar(self.ui.lineSabado,self.ui.lineEdit_7,self.ui.pushButton_5))
        self.ui.lineDomingo.textChanged.connect(lambda:validar(self.ui.lineDomingo,self.ui.lineEdit_8,self.ui.pushButton_5))
        self.ui.pushButton_7.setText("limpiar")
        self.ui.pushButton_7.clicked.connect(self.limpiar)
        self.ui.pushButton_6.clicked.connect(self.on_clicled)

        self.ui.pushButton_15.clicked.connect(self.recargarTabla)
        self.ui.pushButton_8.clicked.connect(self.clipboard)
        self.ui.lineEdit_17.textChanged.connect(lambda:materiaValidar(self.ui.lineEdit_17,self.ui.pushButton_5))

        self.ui.pushButton_9.clicked.connect(self.request)

        #eventos de ventana
        def moverVentana(event):
            if event.buttons() ==Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos=event.globalPos()
                event.accept()

        self.ui.header.mouseMoveEvent = moverVentana



    def refresh_(self):
        buttonReply=QMessageBox.question(self, '¿Has revisado bien?', "Estan correctos todos los datos?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:

            fila=self.ui.tableWidget.rowCount()
            guardar(self.ui.lineEdit_16.text(),self.ui.lineEdit_17.text(),self.ui.linLunes.text(),self.ui.lineMartes.text(),self.ui.linMiercoles.text(),self.ui.lineJueves.text(),self.ui.lineViernes.text(),self.ui.lineSabado.text(),self.ui.lineDomingo.text(),self.ui.lineEdit_2.text(),self.ui.lineEdit_3.text(),self.ui.lineEdit_4.text(),self.ui.lineEdit_5.text(),self.ui.lineEdit_6.text(),self.ui.lineEdit_7.text(),self.ui.lineEdit_8.text())

            self.ui.tableWidget.insertRow(fila)
            f=bd.getOne()
            columna = 0
            for item in f:
                self.ui.tableWidget.setItem(fila, columna, QTableWidgetItem(item))
                columna += 1

            self.comboMaterias.append(self.ui.lineEdit_17.text())
            self.ui.comboBox.addItem(self.ui.lineEdit_17.text())

            self.limpiar()



    def on_combobox_func(self, text):
        self.selectedItem= text

    def on_clicled(self):
        self.ui.pushButton_7.clicked.disconnect()
        self.ui.pushButton_7.clicked.connect(self.delete)
        self.ui.pushButton_7.setText("eliminar")
        self.ui.pushButton_7.setStyleSheet("color:white; background:red; border-radius:10px;")
        for i in range(len(self.comboMaterias)):
            if self.selectedItem ==self.comboMaterias[i]:
                bd.setEntrys(self.comboMaterias[i],self.ui.lineEdit_17,self.ui.lineEdit_16,self.ui.linLunes,self.ui.lineMartes,self.ui.linMiercoles,self.ui.lineJueves,self.ui.lineViernes,self.ui.lineSabado,self.ui.lineDomingo,self.ui.lineEdit_2,self.ui.lineEdit_3,self.ui.lineEdit_4,self.ui.lineEdit_5,self.ui.lineEdit_6,self.ui.lineEdit_7,self.ui.lineEdit_8)

        self.ui.pushButton_6.setText("cancelar")
        self.ui.pushButton_6.setStyleSheet("color:white; background:black; border-radius:10px;")
        self.ui.pushButton_6.clicked.disconnect()
        self.ui.pushButton_6.clicked.connect(self.limpiar)

        self.ui.pushButton_5.setText("Editar")
        self.ui.pushButton_5.setStyleSheet("color:white; background:rgb(114, 159, 207); border-radius:10px;")
        self.ui.pushButton_5.clicked.disconnect()
        self.ui.pushButton_5.clicked.connect(self.editButtonbeh)


    def delete(self):

        try:
            buttonReply=QMessageBox.question(self, '¿Has revisado bien?', f"Estas seguro de eliminar esta materia", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:

                for i in range(len(self.comboMaterias)):
                    if self.selectedItem ==self.comboMaterias[i]:
                        bd.delete(self.comboMaterias[i])
                        self.ui.comboBox.removeItem(self.ui.comboBox.currentIndex())
                        self.ui.comboBox.setCurrentIndex(self.comboMaterias.index(self.comboMaterias[i-1]))
                self.limpiar()


        except:
            print("error")

    def IndexCeropage(self):
        cargarTabla(self.ui.tableWidget)
        self.ui.stackedWidget.setCurrentIndex(0)

    def recargarTabla(self):
        self.close()

        try:
            subprocess.Popen("Eileen.exe")
        except:
            os.system("python3 main.py")

    def clipboard(self):
        df=pd.DataFrame([self.ui.lineEdit.text()])
        df.to_clipboard(index=False,header=False)



    def limpiar(self):
        self.ui.pushButton_7.clicked.disconnect()
        self.ui.pushButton_7.clicked.connect(self.limpiar)
        self.ui.pushButton_7.setText("limpiar")
        self.ui.pushButton_7.setStyleSheet("color:white;border-radius:10px;background:#3DCC8E;")
        self.ui.pushButton_5.setText("guardar")

        self.ui.pushButton_5.clicked.disconnect()
        self.ui.pushButton_5.clicked.connect(self.refresh_)
        self.ui.pushButton_6.setText("Buscar")
        self.ui.pushButton_6.clicked.connect(self.on_clicled)
        self.ui.pushButton_6.setStyleSheet("color:white;border-radius:10px;background:#3DCC8E;")
        self.ui.pushButton_5.setStyleSheet("color:white;border-radius:10px;background:#3DCC8E;")
        self.ui.linLunes.setText("")
        self.ui.lineMartes.setText("")
        self.ui.linMiercoles.setText("")
        self.ui.lineJueves.setText("")
        self.ui.lineViernes.setText("")
        self.ui.lineSabado.setText("")
        self.ui.lineDomingo.setText("")
        self.ui.lineEdit_2.setText("")
        self.ui.lineEdit_3.setText("")
        self.ui.lineEdit_4.setText("")
        self.ui.lineEdit_5.setText("")
        self.ui.lineEdit_6.setText("")
        self.ui.lineEdit_7.setText("")
        self.ui.lineEdit_8.setText("")
        self.ui.lineEdit_16.setText("")
        self.ui.lineEdit_17.setText("")
        self.ui.lineEdit_17.setStyleSheet("border:null;")
        self.ui.pushButton_5.show()



    def editButtonbeh(self):
        buttonReply=QMessageBox.question(self, '¿Has revisado bien?', "¿ingresaste bien tus datos?, recuerda que puedes volver a editar", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if buttonReply == QMessageBox.Yes:
            for i in range(len(self.comboMaterias)):
                if self.selectedItem ==self.comboMaterias[i]:
                    bd.Update(self.ui.lineEdit_17.text(),self.comboMaterias[i],self.ui.lineEdit_16.text(),self.ui.linLunes.text(),self.ui.lineMartes.text(),self.ui.linMiercoles.text(),self.ui.lineJueves.text(),self.ui.lineViernes.text(),self.ui.lineSabado.text(),self.ui.lineDomingo.text(),self.ui.lineEdit_2.text(),self.ui.lineEdit_3.text(),self.ui.lineEdit_4.text(),self.ui.lineEdit_5.text(),self.ui.lineEdit_6.text(),self.ui.lineEdit_7.text(),self.ui.lineEdit_8.text())


            self.ui.pushButton_5.clicked.disconnect()
            self.ui.pushButton_5.clicked.connect(self.refresh_)
            self.limpiar()
            self.ui.comboBox.clear()
            self.ui.comboBox.update()
            self.ui.comboBox.addItems(self.comboMaterias)




    def mousePressEvent(self,event):
        self.dragPos =event.globalPos()

    def working(self):

        self.ui.lineEdit.update()
        if str(xd) == "None":
            self.ui.lineEdit.setText("No hay Url asignado")
        else:
            self.ui.lineEdit.setText(str(xd))





    def request(self):
        valor=QMessageBox.question(self,"Información","quieres ingresar a esta reunión")

        if valor==QMessageBox.Yes:
             webbrowser.open(xd)




if __name__ == '__main__':


    app=QApplication(sys.argv)
    my_app=TableW()

    my_app.show()

    sys.exit(app.exec_())
