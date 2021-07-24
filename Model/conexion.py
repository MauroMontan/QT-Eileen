import sqlite3
from datetime import datetime
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtWidgets import *

class BaseDeDatos:

    def __init__(self):
        self.conexion = sqlite3.connect("Model/db.db")
        self.cursor = self.conexion.cursor()

    def getDatos(self):
        self.cursor.execute("SELECT * FROM HORARIO")
        datos = self.cursor.fetchall()

        return datos
    def getOne(self):
        self.cursor.execute("SELECT * FROM HORARIO WHERE ID= (SELECT MAX(ID) FROM HORARIO)")
        datos = self.cursor.fetchone()

        return datos

    def crearMateria(self,Grupo,Materia,Lunes,Martes,Miercoles,Jueves,Viernes,Sabado,Domingo,URL_Lunes,URL_Martes,URL_Miercoles,URL_Jueves,URL_Viernes,URL_Sabado,URL_Domingo):
        self.cursor.execute("INSERT INTO HORARIO VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',NULL)".format(Grupo,Materia,Lunes,Martes,Miercoles,Jueves,Viernes,Sabado,Domingo,URL_Lunes,URL_Martes,URL_Miercoles,URL_Jueves,URL_Viernes,URL_Sabado,URL_Domingo))
        datos = self.cursor.fetchone()
        self.conexion.commit()


    def buscarNombreMateria(self):
        self.cursor.execute("SELECT MATERIA FROM HORARIO")
        datos = self.cursor.fetchall()
        self.conexion.commit()
        MateriasNombres=[]
        for materia in datos:
            MateriasNombres.append(materia)

        arrMaterias=[]
        for intervalo in MateriasNombres:
            arrMaterias.append(intervalo[0])
        return arrMaterias

    def Update(self,Materia,MATERIA,Grupo,Lunes,Martes,Miercoles,Jueves,Viernes,Sabado,Domingo,URL_Lunes,URL_Martes,URL_Miercoles,URL_Jueves,URL_Viernes,URL_Sabado,URL_Domingo):
        self.cursor.execute(f"UPDATE HORARIO SET GRUPO='{Grupo}', MATERIA='{Materia}', LUNES='{Lunes}', MARTES='{Martes}', MIERCOLES='{Miercoles}', JUEVES='{Jueves}', VIERNES='{Viernes}', SABADO='{Sabado}', DOMINGO='{Domingo}', URL_LUNES='{URL_Lunes}', URL_MARTES='{URL_Martes}', URL_MIERCOLES='{URL_Miercoles}', URL_JUEVES='{URL_Jueves}', URL_VIERNES='{URL_Viernes}', URL_SABADO='{URL_Sabado}', URL_DOMINGO='{URL_Domingo}' WHERE MATERIA LIKE '{MATERIA}' ")

        self.conexion.commit()

    def delete(self,MATERIA):
        self.cursor.execute(f"DELETE FROM HORARIO WHERE MATERIA ='{MATERIA}'")
        self.conexion.commit()

    def setEntrys(self,Materia,MATERIA,GRUPO,LUNES,MARTES,MIERCOLES,JUEVES,VIERNES,SABADO,DOMINGO,URL_LUNES,URL_MARTES,URL_MIERCOLES,URL_JUEVES,URL_VIERNES,URL_SABADO,URL_DOMINGO):
        self.cursor.execute("SELECT * FROM HORARIO WHERE MATERIA = '{}' ".format(Materia))
        datos = self.cursor.fetchall()
        self.conexion.commit()

        for materia in datos:
            MATERIA.setText(str(materia[1]))
            GRUPO.setText(str(materia[0]))
            LUNES.setText(str(materia[2]))
            MARTES.setText(str(materia[3]))
            MIERCOLES.setText(str(materia[4]))
            JUEVES.setText(str(materia[5]))
            VIERNES.setText(str(materia[6]))
            SABADO.setText(str(materia[7]))
            DOMINGO.setText(str(materia[8]))
            URL_LUNES.setText(str(materia[9]))
            URL_MARTES.setText(str(materia[10]))
            URL_MIERCOLES.setText(str(materia[11]))
            URL_JUEVES.setText(str(materia[12]))
            URL_VIERNES.setText(str(materia[13]))
            URL_SABADO.setText(str(materia[14]))
            URL_DOMINGO.setText(str(materia[15]))

    def initAlarm(self,DIA):
        self.cursor.execute(f"SELECT {DIA} FROM HORARIO")
        ARREGLO=self.cursor.fetchall()
        self.conexion.commit()

        return ARREGLO



    def initAlarmUrls(self,DIA):
        self.cursor.execute(f"SELECT {DIA} FROM HORARIO")
        arrUrls=self.cursor.fetchall()
        self.conexion.commit()

        URLS=[]
        for url in arrUrls:
            URLS.append(url[0])

        return URLS
