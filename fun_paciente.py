from beautifultable import BeautifulTable
import pymysql
from login import connect_to_database


def menu_paciente(rut_paciente):
    while True:
        print("1. Mostrar ficha médica")
        print("2. Mostrar ficha médica por RUT")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_ficha_medica_por_rut(rut_paciente)
        elif opcion == "3":
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

def obtener_rut_paciente(id_usuario):
    try:
        # Establecer conexión a la base de datos
        connection = connect_to_database()
        cursor = connection.cursor()

        # Consulta SQL para obtener el RUT del paciente
        sql = """
        SELECT fm.ID_FichaMedica, fm.Diagnostico, fm.Fecha_Atencion, fm.Anamnesis, fm.Nombre_Medico_Atendio
        FROM fichamedica fm
        JOIN paciente p ON fm.ID_Paciente = p.ID_Paciente
        JOIN (
        SELECT COALESCE(profesional.ID_Profesional, paciente.ID_Paciente) AS ID
        FROM login
        LEFT JOIN profesional ON login.ID_Profesional = profesional.ID_Profesional
        LEFT JOIN paciente ON login.ID_TipoUsuario = paciente.ID_TipoUsuario
        WHERE login.ID_Login = %s
        ) AS user_id ON p.ID_Paciente = user_id.ID
        """

        # Ejecutar la consulta SQL con el id_usuario proporcionado
        cursor.execute(sql, (id_usuario,))
        resultado = cursor.fetchone()

        if resultado:
            rut_paciente = resultado[0]
            return rut_paciente
        else:
            print(f"No se encontró un paciente para el ID de usuario {id_usuario}.")
            return None

    except pymysql.MySQLError as e:
        print(f"Error al obtener el RUT del paciente: {e}")
        return None

    finally:
        cursor.close()
        connection.close()

def mostrar_ficha_medica_por_rut(rut_paciente):
    try:
        connection = connect_to_database()
        with connection.cursor() as cursor:
            sql = """
                SELECT p.ID_Paciente, p.RUT, p.Nombre, p.Apellido, f.ID_FichaMedica, f.Diagnostico, f.Fecha_Atencion, f.Anamnesis, m.Nombre AS Medicamento
                FROM paciente p
                LEFT JOIN fichamedica f ON p.ID_Paciente = f.ID_Paciente
                LEFT JOIN medicamento m ON f.ID_Medicamento = m.ID_Medicamento
                WHERE p.RUT = %s
            """
            cursor.execute(sql, (rut_paciente,))
            ficha_medica = cursor.fetchone()

            if not ficha_medica:
                print(f"No se encontró ficha médica para el paciente con RUT {rut_paciente}.")
                return

            print("Ficha Médica:")
            table = BeautifulTable()
            table.columns.header = ["ID Paciente", "RUT", "Nombre", "Apellido", "ID Ficha", "Diagnóstico", "Fecha Atención", "Anamnesis", "Medicamento"]
            table.rows.append([
                ficha_medica[0],
                ficha_medica[1],
                ficha_medica[2],
                ficha_medica[3],
                ficha_medica[4],
                ficha_medica[5],
                ficha_medica[6],
                ficha_medica[7],
                ficha_medica[8]
            ])
            print(table)

    except pymysql.MySQLError as e:
        print("Error al mostrar la ficha médica:", e)

    finally:
        connection.close()