from beautifultable import BeautifulTable, BTColumnCollection, BTRowCollection
import pymysql
from login import connect_to_database  # Asumiendo que este módulo existe
from datetime import datetime

def menu_paciente(rut_paciente, username_paciente):
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
                SELECT p.Nombre AS Nombre_Paciente, p.Apellido AS Apellido_Paciente,
                       f.Fecha_Atencion, f.Diagnostico, e.Nombre AS Nombre_Examen,
                       m.Nombre AS Nombre_Medicamento, pr.Nombre AS Nombre_Profesional, 
                       pr.Apellido AS Apellido_Profesional
                FROM fichamedica f
                JOIN paciente p ON f.ID_Paciente = p.ID_Paciente
                LEFT JOIN examen e ON f.ID_Examen = e.ID_Examen
                LEFT JOIN medicamento m ON f.ID_Medicamento = m.ID_Medicamento
                JOIN profesional pr ON f.ID_Profesional = pr.ID_Profesional
                WHERE p.ID_Paciente = %s
            """
            cursor.execute(sql, (rut_paciente,))
            fichas = cursor.fetchall()

            if fichas:
                table = BeautifulTable()
                table.set_style(BeautifulTable.STYLE_GRID)
                table.columns.header = ["Nombre del Paciente", "Apellido del Paciente", 
                                        "Fecha de Atención", "Diagnóstico", "Examen", 
                                        "Medicamento", "Nombre del Profesional", 
                                        "Apellido del Profesional"]

                for ficha in fichas:
                    # Verifica que la fecha de atención no sea None antes de formatearla
                    fecha_atencion = ficha[2].strftime('%d-%m-%Y') if ficha[2] else "-"
                    
                    table.rows.append([
                        ficha[0],   # Nombre_Paciente
                        ficha[1],   # Apellido_Paciente
                        fecha_atencion,
                        ficha[3],   # Diagnóstico
                        ficha[4] if ficha[4] else "-",   # Nombre_Examen (verifica si es None)
                        ficha[5] if ficha[5] else "-",   # Nombre_Medicamento (verifica si es None)
                        ficha[6],   # Nombre_Profesional
                        ficha[7]    # Apellido_Profesional
                    ])

                print(f"Fichas médicas del paciente con ID {rut_paciente}:")
                print(table)
            else:
                print(f"No se encontraron fichas médicas para el ID '{rut_paciente}'.")

    except pymysql.MySQLError as e:
        print("Error al mostrar las fichas médicas del paciente:", e)
