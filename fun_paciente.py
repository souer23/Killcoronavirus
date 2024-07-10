from beautifultable import BeautifulTable
import pymysql
from login import connect_to_database


def menu_paciente(rut_paciente):
    connection = connect_to_database()
    while True:
        print("\nMenú del Paciente:")
        print("1. Buscar ficha médica por RUT del paciente")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_fichas_medicas_por_paciente(connection, rut_paciente)
        elif opcion == "2":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
    connection.close()

def mostrar_fichas_medicas_por_paciente(connection, rut_paciente): 
    try:
        with connection.cursor() as cursor:
            sql = """
                SELECT p.Nombre AS Nombre_Paciente, f.Fecha_Atencion, f.Diagnostico, pr.Nombre AS Nombre_Profesional
                FROM fichamedica f
                JOIN paciente p ON f.ID_Paciente = p.ID_Paciente
                JOIN profesional pr ON f.ID_Profesional = pr.ID_Profesional
                WHERE p.ID_Paciente = %s
            """
            cursor.execute(sql, (rut_paciente,))
            fichas = cursor.fetchall()

            if fichas:
                table = BeautifulTable()
                table.set_style(BeautifulTable.STYLE_GRID)
                table.column_headers = ["Nombre del Paciente", "Fecha de Atención", "Diagnóstico", "Nombre del Profesional"]

                for ficha in fichas:
                    table.append_row([
                        ficha[0],  # Nombre_Paciente
                        ficha[1],  # Fecha_Atencion
                        ficha[2],  # Diagnostico
                        ficha[3]   # Nombre_Profesional
                    ])

                print("Fichas médicas del paciente con ID", rut_paciente)
                print(table)
            else:
                print(f"No se encontraron fichas médicas para el ID '{rut_paciente}'.")
    except pymysql.MySQLError as e:
        print("Error al mostrar las fichas médicas del paciente:", e)