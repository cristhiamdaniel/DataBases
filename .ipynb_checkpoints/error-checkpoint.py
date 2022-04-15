import mysql.connector
from mysql.connector import Error

'''
try:
    mi_conexion = mysql.connector.connect(
        host = input("introduce la IP: "),
        user = input("introduce el usuario: "),
        passwd = input("introduce la contrasenia: "))

    mi_cursor = mi_conexion.cursor()
    mi_cursor.execute("SHOW DATABASES")

    for bd in mi_cursor:
        print(bd)

    mi_cursor.close()
    mi_conexion.close()

except Error as e:
    print("Ha ocurrido un error:")
    print(e)
'''

#Usando funciones

def conectarse(ip, usuario, contrasenia):
    try:
        conexion = mysql.connector.connect(
            host = ip,
            user = usuario,
            passwd = contrasenia)
        print("Conexion realizada correctamente")

    except Error as e:
        conexion = None
        print("Ha ocurrido el error:")
        print(e)

    return conexion

def desconectarse(conexion):
    if conexion:
        conexion.close()
        print("Conexion finalizada correctamente.")

def hacer_consulta(conexion):
    cursor = conexion.cursor()
    cursor.execute("SHOW DATABASES")
    for bd in cursor:
        print(bd)
    cursor.close()

i = input("Introduzca la ip: ")
u = input("Introduzca el usuario: ")
c = input("Introduzca la contrasenia: ")

conexion = conectarse(i,u,c)
if conexion:
    hacer_consulta(conexion)
    desconectarse(conexion)
        


















