import mysql.connector
from mysql.connector import Error

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
