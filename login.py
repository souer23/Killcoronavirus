from getpass import getpass
import pymysql
from fun_admin import * 
from fun_medico import *
from fun_paciente import *

def connect_to_database():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="killcoronavirus"
    )

def login():
    print("Bienvenido al sistema de salud KillCoronaVirus.")
    print("")
    print("Por favor, ingrese sus credenciales:")
    print("")
    username = input("Nombre de usuario: ")
    password = getpass.getpass("Contraseña: ")

    connection = connect_to_database()
    cursor = connection.cursor()

    query = "SELECT ID_TipoUsuario, ID_Profesional FROM login WHERE Usuario = %s AND Password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if result:
        tipo_usuario = result[0]
        if tipo_usuario == 1:
            menu_administrador()
        elif tipo_usuario == 2:
            menu_medico()
        elif tipo_usuario == 3:
            id_profesional = result[1]
            # Obtener ID_Paciente desde la tabla paciente
            query_paciente = "SELECT ID_Paciente FROM paciente WHERE Usuario = %s"
            cursor.execute(query_paciente, (username,))
            paciente_result = cursor.fetchone()
            if paciente_result:
                rut_paciente = paciente_result[0]
                menu_paciente(rut_paciente)
            else:
                print("No se encontró un paciente asociado a este usuario.")
        else:
            print("Tipo de usuario no válido.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    login()
