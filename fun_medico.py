import pymysql
import re
from beautifultable import BeautifulTable
from login import connect_to_database
import datetime
import getpass


def menu_medico():
    while True:
        print("\nMenú del médico:")
        print("1. Mostrar pacientes")
        print("2. Buscar paciente")
        print("3. Generar nueva anamnesis")
        print("4. Generar nuevo diagnóstico")
        print("5. Recetar exámenes")
        print("6. Recetar medicamentos")
        print("7. Mostrar ficha médica")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                mostrar_pacientes()
            elif opcion == "2":
                pacientes = buscar_pacientes()
                if pacientes:
                    id_paciente = pacientes[0][0]  # Suponiendo que el primer resultado es el deseado
                    mostrar_ficha_medica_por_rut(id_paciente)
            elif opcion == "3":
                id_paciente = int(input("Ingrese el ID del paciente: "))
                id_ficha = int(input("Ingrese el ID de la ficha médica: "))
                generar_anamnesis(id_paciente, id_ficha)  # Asegúrate de pasar ambos IDs
            elif opcion == "4":
                id_ficha = int(input("Ingrese el ID de la ficha médica: "))
                generar_diagnostico(id_ficha)
            elif opcion == "5":
                id_ficha = int(input("Ingrese el ID de la ficha médica: "))
                recetar_examenes(id_ficha)
            elif opcion == "6":
                id_ficha = int(input("Ingrese el ID de la ficha médica: "))
                recetar_medicamentos(id_ficha)
            elif opcion == "7":
                id_ficha = int(input("Ingrese el rut del paciente: "))
                mostrar_ficha_medica_por_rut(id_ficha)
            elif opcion == "8":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
        except ValueError:
            print("Error: Ingrese un número válido para el ID.")

def mostrar_pacientes():
    connection = connect_to_database()
    cursor = connection.cursor()

    query = """
    SELECT ID_Paciente, RUT, Nombre, Apellido, Fecha_Nac, Telefono
    FROM paciente
    """
    
    cursor.execute(query)
    pacientes = cursor.fetchall()

    if pacientes:
        table = BeautifulTable()
        table.column_headers = ["ID", "RUT", "Nombre", "Apellido", "Fecha Nac", "Teléfono"]

        for paciente in pacientes:
            table.append_row(paciente)

        print("Listado de pacientes:")
        print(table)
    else:
        print("No hay pacientes registrados.")

    cursor.close()
    connection.close()

def crear_paciente():
    try:
        connection = connect_to_database()
        with connection.cursor() as cursor:
            rut = input("Ingrese el RUT del paciente: ")
            nombre = input("Ingrese el nombre del paciente: ")
            apellido = input("Ingrese el apellido del paciente: ")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento del paciente (YYYY-MM-DD): ")
            telefono = input("Ingrese el teléfono del paciente: ")

            sql_paciente = """
                INSERT INTO `paciente` (`RUT`, `Nombre`, `Apellido`, `Fecha_Nac`, `Telefono`, `ID_TipoUsuario`)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql_paciente, (rut, nombre, apellido, fecha_nacimiento, telefono, 3))
            connection.commit()

            id_paciente = cursor.lastrowid

            nombre_usuario = input("Ingrese el nombre de usuario para el login: ")
            contrasena = input("Ingrese la contraseña para el login: ")

            sql_login = """
                INSERT INTO `login` (`Usuario`, `Password`, `ID_TipoUsuario`)
                VALUES (%s, %s, %s)
            """
            cursor.execute(sql_login, (nombre_usuario, contrasena, 3))  # Aquí corregimos los parámetros
            connection.commit()

            print("Paciente y login creados con éxito.")
            return id_paciente, rut, nombre, apellido  # Devuelve los valores esperados

    except pymysql.MySQLError as e:
        print("Error al crear paciente:", e)
        return None  # Devuelve None en caso de error

    finally:
        connection.close()

def buscar_pacientes(id_medico=None):
    try:
        connection = connect_to_database()
        with connection.cursor() as cursor:
            if id_medico:
                sql = """
                    SELECT p.ID_Paciente, p.RUT, p.Nombre, p.Apellido, fm.ID_FichaMedica
                    FROM paciente p
                    JOIN fichamedica fm ON p.ID_Paciente = fm.ID_Paciente
                    WHERE fm.ID_Profesional = %s
                """
                cursor.execute(sql, (id_medico,))
            else:
                rut = input("Ingrese el RUT del paciente: ")
                sql = """
                    SELECT p.ID_Paciente, p.RUT, p.Nombre, p.Apellido, fm.ID_FichaMedica
                    FROM paciente p
                    JOIN fichamedica fm ON p.ID_Paciente = fm.ID_Paciente
                    WHERE p.RUT = %s
                """
                cursor.execute(sql, (rut,))

            pacientes = cursor.fetchall()

            if not pacientes:
                print("No se encontraron pacientes.")
                if input("¿Desea agregar un nuevo paciente? (s/n): ").lower() == 's':
                    id_paciente, rut, nombre, apellido = crear_paciente()
                    return [(id_paciente, rut, nombre, apellido, None, None)]
                else:
                    return []

            print("Pacientes encontrados:")
            table = BeautifulTable()
            table.columns.header = ["ID Paciente", "RUT", "Nombre", "Apellido", "ID Ficha"]
            for paciente in pacientes:
                table.rows.append(paciente)
            print(table)
            return pacientes

    except pymysql.MySQLError as e:
        print("Error al buscar pacientes:", e)

    finally:
        connection.close()

def generar_anamnesis(id_paciente):
    try:
        connection = connect_to_database()
        with connection.cursor() as cursor:
            anamnesis = input("Ingrese la anamnesis del paciente: ")

            sql = """
                INSERT INTO fichamedica (ID_Paciente, ID_Profesional, Anamnesis)
                VALUES (%s, %s, %s)
            """
            # Aquí asumo que necesitas ID_Profesional también, puedes adaptar según tus necesidades
            id_profesional = input("Ingrese el ID del profesional: ")
            cursor.execute(sql, (id_paciente, id_profesional, anamnesis))
            connection.commit()

            print("Anamnesis generada con éxito.")

    except pymysql.MySQLError as e:
        print("Error al generar la anamnesis:", e)

    finally:
        connection.close()


def generar_diagnostico(id_ficha):
    try:
        connection = connect_to_database()
        with connection.cursor() as cursor:
            diagnostico = input("Ingrese el diagnóstico del paciente: ")

            sql = """
                UPDATE fichamedica
                SET Diagnostico = %s
                WHERE ID_FichaMedica = %s
            """
            cursor.execute(sql, (diagnostico, id_ficha))
            connection.commit()

            print("Diagnóstico generado con éxito.")

    except pymysql.MySQLError as e:
        print("Error al generar el diagnóstico:", e)

    finally:
        connection.close()

def recetar_examenes(id_ficha):
    try:
        connection = connect_to_database()

        # Mostrar los exámenes disponibles
        with connection.cursor() as cursor:
            sql_select = "SELECT * FROM examen"
            cursor.execute(sql_select)
            examenes = cursor.fetchall()

            if examenes:
                table = BeautifulTable()
                table.column_headers = ["ID Examen", "Nombre"]
                for examen in examenes:
                    table.append_row([examen[0], examen[1]])

                print("Exámenes disponibles:")
                print(table)
            else:
                print("No hay exámenes disponibles.")

        # Pedir al usuario que ingrese el examen a recetar
        examen_id = input("Ingrese el ID del examen a recetar: ")

        # Actualizar la ficha médica con el examen recetado
        with connection.cursor() as cursor:
            sql_update = """
                UPDATE fichamedica
                SET ID_Examen = %s
                WHERE ID_FichaMedica = %s
            """
            cursor.execute(sql_update, (examen_id, id_ficha))
            connection.commit()

            print("Examen recetado con éxito.")

    except pymysql.MySQLError as e:
        print("Error al recetar el examen:", e)

    finally:
        connection.close()

def recetar_medicamentos(id_ficha):
    try:
        connection = connect_to_database()

        # Mostrar los medicamentos disponibles
        with connection.cursor() as cursor:
            sql_select = "SELECT * FROM medicamentos"
            cursor.execute(sql_select)
            medicamentos = cursor.fetchall()

            if medicamentos:
                table = BeautifulTable()
                table.column_headers = ["ID Medicamento", "Nombre"]
                for medicamento in medicamentos:
                    table.append_row([medicamento[0], medicamento[1]])

                print("Medicamentos disponibles:")
                print(table)
            else:
                print("No hay medicamentos disponibles.")

        # Pedir al usuario que ingrese el medicamento a recetar
        medicamento_id = input("Ingrese el ID del medicamento a recetar: ")

        # Actualizar la ficha médica con el medicamento recetado
        with connection.cursor() as cursor:
            sql_update = """
                UPDATE fichamedica
                SET ID_Medicamento = %s
                WHERE ID_FichaMedica = %s
            """
            cursor.execute(sql_update, (medicamento_id, id_ficha))
            connection.commit()

            print("Medicamento recetado con éxito.")

    except pymysql.MySQLError as e:
        print("Error al recetar el medicamento:", e)

    finally:
        connection.close()

def mostrar_ficha_medica_por_rut(rut):
    try:
        connection = connect_to_database()
        with connection.cursor() as cursor:
            # Buscar ID del paciente por rut
            sql_id_paciente = """
                SELECT ID_Paciente
                FROM paciente
                WHERE RUT = %s
            """
            cursor.execute(sql_id_paciente, (rut,))
            paciente = cursor.fetchone()

            if not paciente:
                print("No se encontró ningún paciente con ese rut.")
                return

            id_paciente = paciente[0]  # Acceder al primer elemento de la tupla

            # Consultar fichas médicas del paciente
            sql_fichas = """
                SELECT ID_FichaMedica, Diagnostico, Fecha_Atencion, Anamnesis, ID_Medicamento, ID_Examen
                FROM fichamedica
                WHERE ID_Paciente = %s
            """
            cursor.execute(sql_fichas, (id_paciente,))
            fichas_medicas = cursor.fetchall()

            if not fichas_medicas:
                print("No se encontraron fichas médicas para este paciente.")
            else:
                # Crear una tabla con BeautifulTable
                table = BeautifulTable()
                table.column_headers = ["ID Ficha Médica", "Diagnóstico", "Fecha de Atención", "Anamnesis", "ID Medicamento", "ID Examen"]

                for ficha in fichas_medicas:
                    table.append_row(ficha)

                print("Fichas Médicas encontradas:")
                print(table)

    except pymysql.MySQLError as e:
        print("Error al mostrar la ficha médica:", e)

    finally:
        connection.close()
