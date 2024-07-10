import pymysql
import re
from beautifultable import BeautifulTable
from login import connect_to_database
from datetime import datetime
import getpass

def connect_to_database():
    # Esta función debe ser implementada según tu método de conexión a la base de datos MySQL.
    # Aquí un ejemplo genérico:
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="killcoronavirus",
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

def mostrar_tabla_datos(tabla, connection):
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM {tabla}"
            cursor.execute(sql)
            if cursor.rowcount > 0:
                # Crear una tabla bonita para mostrar los datos
                table = BeautifulTable()
                table.set_style(BeautifulTable.STYLE_GRID)

                # Obtener nombres de columnas y añadirlos como encabezados
                column_names = [i[0] for i in cursor.description]
                table.column_headers = column_names
                
                # Obtener todas las filas recuperadas
                rows = cursor.fetchall()
                
                # Agregar filas a la tabla
                for row in rows:
                    formatted_row = [str(item) for item in row.values()]  # Convertir los valores en strings
                    table.append_row(formatted_row)
                
                # Mostrar la tabla
                print(f"Tabla {tabla}:")
                print(table)
            else:
                print(f"No hay datos en la tabla {tabla}.")
    except pymysql.MySQLError as e:
        print(f"Error al mostrar la tabla {tabla}: {e}")

def buscar_paciente(connection):
    try:
        rut_paciente = input("Ingrese el RUT del paciente (sin puntos ni guión): ").strip()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM paciente WHERE RUT = %s"
            cursor.execute(sql, (rut_paciente,))
            paciente = cursor.fetchone()
            if paciente:
                print("Paciente encontrado:")
                print(f"ID: {paciente['ID_Paciente']}")
                print(f"Nombre: {paciente['Nombre']} {paciente['Apellido']}")
                print(f"Fecha de Nacimiento: {paciente['Fecha_Nac']}")
                print(f"Teléfono: {paciente['Telefono']}")
                print(f"Tipo de Usuario: {paciente['ID_TipoUsuario']}")
                return rut_paciente
            else:
                print("No se encontró un paciente con ese RUT.")
                agregar_paciente(connection, rut_paciente)
                return rut_paciente
    except pymysql.MySQLError as e:
        print("Error al buscar paciente:", e)

def agregar_paciente(connection, rut_paciente):
    try:
        print("\nAgregando nuevo paciente al sistema:")
        nombre = input("Ingrese el nombre del paciente: ")
        apellido = input("Ingrese el apellido del paciente: ")
        fecha_nac = input("Ingrese la fecha de nacimiento del paciente (YYYY-MM-DD): ")
        telefono = input("Ingrese el teléfono del paciente: ")
        id_tipo_usuario = input("Ingrese el ID del tipo de usuario para el paciente: ")

        # Insertar nuevo paciente en la tabla paciente
        with connection.cursor() as cursor:
            sql_insert = """
                INSERT INTO paciente (RUT, Nombre, Apellido, Fecha_Nac, Telefono, ID_TipoUsuario)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql_insert, (rut_paciente, nombre, apellido, fecha_nac, telefono, id_tipo_usuario))
            connection.commit()

            print("Paciente agregado con éxito.")

        # Crear credencial de acceso para el paciente
        while True:
            nombre_usuario = input("Ingrese el nombre de usuario para el login: ").strip()
            if not nombre_usuario:
                print("El nombre de usuario no puede estar vacío.")
                continue
            contrasena = input("Ingrese la contraseña para el login: ").strip()
            if not contrasena:
                print("La contraseña no puede estar vacía.")
                continue
            break

        # Insertar credencial en la tabla login
        sql_login = """
            INSERT INTO `login` (`Usuario`, `Password`, `ID_TipoUsuario`)
            VALUES (%s, %s, %s)
        """
        with connection.cursor() as cursor:
            cursor.execute(sql_login, (nombre_usuario, contrasena, id_tipo_usuario))
            connection.commit()

            print("Credencial de acceso creada para el paciente.")

    except pymysql.MySQLError as e:
        print("Error al agregar paciente:", e)

def crear_ficha_medica(connection, rut_paciente):
    try:
        # Conexión a la base de datos

        # Obtener fecha actual
        fecha_atencion = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Ingreso de datos por el usuario
        diagnostico = input("Ingrese el diagnóstico: ")
        anamnesis = input("Ingrese la anamnesis: ")

        mostrar_tabla_datos("paciente", connection)

        # Validar y obtener ID_Paciente válido
        id_paciente = None
        while id_paciente is None:
            try:
                id_paciente = int(input("Ingrese el ID del paciente: "))
                with connection.cursor() as cursor:
                    sql = "SELECT * FROM paciente WHERE ID_Paciente = %s"
                    cursor.execute(sql, (id_paciente,))
                    if cursor.rowcount == 0:
                        print("No existe un paciente con ese ID. Intente nuevamente.")
                        id_paciente = None
            except ValueError:
                print("Ingrese un número válido para el ID del paciente.")

        mostrar_tabla_datos("profesional", connection)

        # Validar y obtener ID_Profesional válido
        id_profesional = None
        while id_profesional is None:
            try:
                id_profesional = int(input("Ingrese el ID del profesional: "))
                with connection.cursor() as cursor:
                    sql = "SELECT * FROM profesional WHERE ID_Profesional = %s"
                    cursor.execute(sql, (id_profesional,))
                    if cursor.rowcount == 0:
                        print("No existe un profesional con ese ID. Intente nuevamente.")
                        id_profesional = None
            except ValueError:
                print("Ingrese un número válido para el ID del profesional.")

        mostrar_tabla_datos("medicamento", connection)

        # Validar y obtener ID_Medicamento válido
        id_medicamento = None
        while id_medicamento is None:
            try:
                id_medicamento = int(input("Ingrese el ID del medicamento: "))
                with connection.cursor() as cursor:
                    sql = "SELECT * FROM medicamento WHERE ID_Medicamento = %s"
                    cursor.execute(sql, (id_medicamento,))
                    if cursor.rowcount == 0:
                        print("No existe un medicamento con ese ID. Intente nuevamente.")
                        id_medicamento = None
            except ValueError:
                print("Ingrese un número válido para el ID del medicamento.")

        
        mostrar_tabla_datos("examen", connection)
        
        # Validar y obtener ID_Examen válido
        id_examen = None
        while id_examen is None:
            try:
                id_examen = int(input("Ingrese el ID del examen: "))
                with connection.cursor() as cursor:
                    sql = "SELECT * FROM examen WHERE ID_Examen = %s"
                    cursor.execute(sql, (id_examen,))
                    if cursor.rowcount == 0:
                        print("No existe un examen con ese ID. Intente nuevamente.")
                        id_examen = None
            except ValueError:
                print("Ingrese un número válido para el ID del examen.")

        # Inserción de datos en la tabla fichamedica
        with connection.cursor() as cursor:
            sql_insert = """
                INSERT INTO fichamedica (Diagnostico, Fecha_Atencion, Anamnesis, ID_Paciente, ID_Profesional, ID_Medicamento, ID_Examen)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql_insert, (diagnostico, fecha_atencion, anamnesis, id_paciente, id_profesional, id_medicamento, id_examen))
            connection.commit()

            print("Ficha médica creada con éxito.")

    except pymysql.MySQLError as e:
        print("Error al crear la ficha médica:", e)

def menu_medico():
    connection = None
    try:
        connection = connect_to_database()
        while True:
            print("\nMenú del médico:")
            print("1. Crear nueva ficha médica")
            print("2. Buscar paciente")
            print("3. Buscar ficha médica por RUT del profesional")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                crear_ficha_medica(connection, None)  # Pasar None para el rut_paciente
            elif opcion == "2":
                buscar_paciente(connection)
            elif opcion == "3":
                mostrar_pacientes_atendidos_por_profesional(connection)
            elif opcion == "4":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
    except pymysql.MySQLError as e:
        print("Error de conexión a la base de datos:", e)
    finally:
        if connection and connection.open:
            connection.close()

def mostrar_pacientes_atendidos_por_profesional(connection):
    try:
        rut_profesional = input("Ingrese el RUT del profesional (sin puntos ni guión): ").strip()
        with connection.cursor() as cursor:
            # Buscar ID del profesional por su RUT
            sql = "SELECT ID_Profesional FROM profesional WHERE RUT = %s"
            cursor.execute(sql, (rut_profesional,))
            profesional = cursor.fetchone()
            if profesional:
                id_profesional = profesional['ID_Profesional']

                # Buscar pacientes atendidos por el profesional
                sql = """
                    SELECT p.Nombre, f.Fecha_Atencion, f.Diagnostico
                    FROM fichamedica f
                    JOIN paciente p ON f.ID_Paciente = p.ID_Paciente
                    WHERE f.ID_Profesional = %s
                """
                cursor.execute(sql, (id_profesional,))
                rows = cursor.fetchall()
                if rows:
                    table = BeautifulTable()
                    table.set_style(BeautifulTable.STYLE_GRID)
                    table.columns.header = ["Nombre del Paciente", "Fecha de Atención", "Diagnóstico"]
                    for row in rows:
                        table.rows.append([row['Nombre'], row['Fecha_Atencion'], row['Diagnostico']])
                    print(table)
                else:
                    print("No se encontraron pacientes atendidos por este profesional.")
            else:
                print("No se encontró un profesional con ese RUT.")
    except pymysql.MySQLError as e:
        print("Error al buscar pacientes atendidos por profesional:", e)