from Model.conexion import BaseDeDatos

bd=BaseDeDatos()

class Alarm(object):
    def __init__(self):
        super(Alarm, self).__init__()
        self.dic={"LUNES":bd.initAlarm("LUNES"),"MARTES":bd.initAlarm("MARTES"),
                "MIERCOLES":bd.initAlarm("MIERCOLES"),"JUEVES":bd.initAlarm("JUEVES"),
                 "VIERNES":bd.initAlarm("VIERNES"),"SABADO":bd.initAlarm("SABADO"),
                  "DOMINGO":bd.initAlarm("DOMINGO")}

        self.urls={"LUNES":bd.initAlarmUrls("URL_LUNES"),"MARTES":bd.initAlarmUrls("URL_MARTES"),"MIERCOLES":bd.initAlarmUrls("URL_MIERCOLES"),
                    "JUEVES":bd.initAlarmUrls("URL_JUEVES"),"VIERNES":bd.initAlarmUrls("URL_VIERNES"),"SABADO":bd.initAlarmUrls("URL_SABADO"),
                    "DOMINGO":bd.initAlarmUrls("URL_DOMINGO")}

        self.Finalinter={"LUNES":[[],[]],"MARTES":[[],[]],"MIERCOLES":[[],[]],"JUEVES":[[],[]],
                        "VIERNES":[[],[]],"SABADO":[[],[]],"DOMINGO":[[],[]]}

        self.horas={"LUNES":[],"MARTES":[],"MIERCOLES":[],"JUEVES":[],
                    "VIERNES":[],"SABADO":[],"DOMINGO":[]}

        self.arr={"LUNES":[],"MARTES":[],"MIERCOLES":[],"JUEVES":[],
                "VIERNES":[],"SABADO":[],"DOMINGO":[]}

        self.intervalo={"LUNES":[],"MARTES":[],"MIERCOLES":[],"JUEVES":[],
                "VIERNES":[],"SABADO":[],"DOMINGO":[]}

        self.intervaloDual={"LUNES":[[],[]],"MARTES":[[],[]],"MIERCOLES":[[],[]],"JUEVES":[[],[]],
                        "VIERNES":[[],[]],"SABADO":[[],[]],"DOMINGO":[[],[]]}
