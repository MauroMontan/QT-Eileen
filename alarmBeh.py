
import sqlite3
from scripts.Alarm import Alarm
import datetime
from PySide2.QtCore import *
from time import strftime
import schedule
import time
import sys
import random



alarm = Alarm()

class selector(object):

    """ esta clase es la encargada de filtrar los intervalos de horario"""

    def __init__(self):
        super(selector, self).__init__()
        self.dias=["LUNES","MARTES","MIERCOLES","JUEVES","VIERNES","SABADO","DOMINGO"]
        self.today_Day=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

        self.horaActual= datetime.datetime.now()
        self.hora=strftime('%H%M')
        self.hora=int(self.hora)
        self.DISPLAY=None






    def initIntervalos(self):

        for dia in self.dias:
            for materia in alarm.dic[dia]:
                alarm.horas[dia].append(materia)


        for dia in self.dias:
            for intervalo in alarm.horas[dia]:
                alarm.arr[dia].append(intervalo[0])


        for i in range(len(alarm.arr[dia])):
            for dia in self.dias:
                alarm.intervalo[dia].append(alarm.arr[dia][i].replace(":","").replace("-",""))

                alarm.intervaloDual[dia][0].append(alarm.intervalo[dia][i][0:4])
                alarm.intervaloDual[dia][1].append(alarm.intervalo[dia][i][4:10])

        for dia in self.dias:
            for i in range(2):
                for string in alarm.intervaloDual[dia][i]:
                    if(string !=""):
                        alarm.Finalinter[dia][i].append(int(string))

        URLSLUNES=[]
        for string in alarm.urls["LUNES"]:
            if(string !=""):
                URLSLUNES.append(string)
        URLSMARTES=[]
        for string in alarm.urls["MARTES"]:
            if(string !=""):
                URLSMARTES.append(string)
        URLSMIERCOLES=[]
        for string in alarm.urls["MIERCOLES"]:
            if(string !=""):
                URLSMIERCOLES.append(string)
        URLSJUEVES=[]
        for string in alarm.urls["JUEVES"]:
            if(string !=""):
                URLSJUEVES.append(string)
        URLSVIERNES=[]
        for string in alarm.urls["VIERNES"]:
            if(string !=""):
                URLSVIERNES.append(string)
        URLSSABADO=[]
        for string in alarm.urls["SABADO"]:
            if(string !=""):
                URLSSABADO.append(string)
        URLSDOMINGO=[]
        for string in alarm.urls["DOMINGO"]:
            if(string !=""):
                URLSDOMINGO.append(string)

        print(len(URLSLUNES))
        print(len(alarm.Finalinter["LUNES"][0]))

        if (self.horaActual.strftime("%a")=="Mon"):
            for i in range(len(alarm.Finalinter["LUNES"][0])):
                if(alarm.Finalinter["LUNES"][0][i]<=self.hora<alarm.Finalinter["LUNES"][1][i]):
                    return URLSLUNES[i]

        if (self.horaActual.strftime("%a")=="Tue"):
            for i in range(len(alarm.Finalinter["MARTES"][0])):
                if(alarm.Finalinter["MARTES"][0][i]<=self.hora<alarm.Finalinter["MARTES"][1][i]):
                    return URLSMARTES[i]

        if (self.horaActual.strftime("%a")=="Wed"):
            for i in range(len(alarm.Finalinter["MIERCOLES"][0])):
                if(alarm.Finalinter["MIERCOLES"][0][i]<=self.hora<alarm.Finalinter["MIERCOLES"][1][i]):
                    return URLSMIERCOLES[i]

        if (self.horaActual.strftime("%a")=="Thu"):
            for i in range(len(alarm.Finalinter["JUEVES"][0])):
                if(alarm.Finalinter["JUEVES"][0][i]<=self.hora<alarm.Finalinter["JUEVES"][1][i]):
                    return URLSJUEVES[i]

        if (self.horaActual.strftime("%a")=="Fri"):
            for i in range(len(alarm.Finalinter["VIERNES"][0])):
                if(alarm.Finalinter["VIERNES"][0][i]<=self.hora<alarm.Finalinter["VIERNES"][1][i]):
                    return URLSVIERNES[i]

        if (self.horaActual.strftime("%a")=="Sat"):
            for i in range(len(alarm.Finalinter["SABADO"][0])):
                if(alarm.Finalinter["SABADO"][0][i]<=self.hora<alarm.Finalinter["SABADO"][1][i]):
                    try:
                        return URLSSABADO[i]
                    except:
                        pass

        if (self.horaActual.strftime("%a")=="Sun"):
            for i in range(len(alarm.Finalinter["DOMINGO"][0])):
                if(alarm.Finalinter["DOMINGO"][0][i]<=self.hora<alarm.Finalinter["DOMINGO"][1][i]):
                    return URLSDOMINGO[i]





alarma=selector()

def hola():

    return alarma.initIntervalos()
