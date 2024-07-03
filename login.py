from getpass import getpass
import pymysql
from fun_admin import * 
from fun_medico import *

def connect_to_database():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="killcoronavirus"
    )
def menu_administrador():
    while True:
        print("\nMenú de administrador:")
        print("1. Mantenimiento Medicamentos")
        print("2. Mantenimiento Especialidades")
        print("3. Mantenimiento Medicos")
        print("4. Mantenimiento Examenes")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mantenimiento_medicamentos()
        elif opcion == "2":
            mantenimiento_especialidades()
        elif opcion == "3":
            mantenimiento_medicos()
        elif opcion == "4":
            mantenimiento_examenes()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Funciones de médico
def menu_medico():
    while True:
        print("\nMenú de medico:")
        print("1. Generar nueva anamnesis")
        print("2. Generar nuevo diagnostico")
        print("3. Recetar medicamentos")
        print("4. Recetar examenes")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            generar_anamnesis()
        elif opcion == "2":
            generar_diagnostico()
        elif opcion == "3":
            recetar_medicamentos()
        elif opcion == "4":
            recetar_examenes()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def login():
    print("Bienvenido al sistema de salud KillCoronaVirus.")
    print("")
    print("Por favor, ingrese sus credenciales:")
    print("")
    username = input("Nombre de usuario: ")
    password = getpass.getpass("Contraseña: ")

    connection = connect_to_database()
    cursor = connection.cursor()

    query = "SELECT ID_TipoUsuario FROM login WHERE Usuario = %s AND Password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if result:
        tipo_usuario = result[0]
        if tipo_usuario == 1:
            menu_administrador()
        elif tipo_usuario == 2:
            menu_medico()
        else:
            print("Tipo de usuario no válido.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    login()
