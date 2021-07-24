from Model.conexion import BaseDeDatos
bd=BaseDeDatos()


def guardar(GRUPO,MATERIA,Lunes,Martes,Miercoles,Jueves,Viernes,Sabado,Domingo,URL_Lunes,URL_Martes,URL_Miercoles,URL_Jueves,URL_Viernes,URL_Sabado,URL_Domingo):

    bd.crearMateria(GRUPO,MATERIA,Lunes,Martes,Miercoles,Jueves,Viernes,Sabado,Domingo,URL_Lunes,URL_Martes,URL_Miercoles,URL_Jueves,URL_Viernes,URL_Sabado,URL_Domingo)
