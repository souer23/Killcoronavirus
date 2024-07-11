import getpass
import pymysql
from beautifultable import BeautifulTable

#Conexion base de datos
def connect_to_database():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="killcoronavirus"
    )

#Menu donde el administrador puede escoger de varias funciones
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
            return
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

#Funcion CRUD completo para tabla Medicamentos
def mantenimiento_medicamentos():
    while True:
        print("\nMenú de Mantenimiento de Medicamentos:")
        print("")
        print("1. Crear medicamento")
        print("2. Mostrar medicamentos")
        print("3. Actualizar medicamento")
        print("4. Eliminar medicamento")
        print("5. Volver al menú principal")
        print("")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_medicamento()
        elif opcion == "2":
            mostrar_medicamentos()
        elif opcion == "3":
            actualizar_medicamento()
        elif opcion == "4":
            eliminar_medicamento()
        elif opcion == "5":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def crear_medicamento():
    try:
        connection = connect_to_database()
        with connection.cursor() as cursor:
            while True:
                nombre = input("Ingrese el nombre del medicamento: ").strip()
                if not nombre:
                    print("El nombre del medicamento no puede estar vacío.")
                    continue
                
                descripcion = input("Ingrese la descripción del medicamento: ").strip()
                if not descripcion:
                    print("La descripción no puede estar vacía.")
                    continue
                break
            sql = "INSERT INTO `medicamento` (`Nombre`, `Descripcion`) VALUES (%s, %s)"
            cursor.execute(sql, (nombre, descripcion))
        connection.commit()
        print("Medicamento creado con éxito.")
    except pymysql.MySQLError as e:
        print("Error al crear el medicamento:", e)
    finally:
        connection.close()

def mostrar_medicamentos():
    try:
        connection = connect_to_database()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `medicamento` WHERE `activo` = 1"
            cursor.execute(sql)
            medicamentos = cursor.fetchall()
            print("Listado de medicamentos:")
            table = BeautifulTable(maxwidth=120)
            table.set_style(BeautifulTable.STYLE_GRID)
            table.columns.header = ["ID", "Nombre", "Descripción"]
            for medicamento in medicamentos:
                table.rows.append([medicamento[0], medicamento[1], medicamento[2]])
            print(table)
    except pymysql.MySQLError as e:
        print("Error al obtener los medicamentos:", e)
    finally:
        connection.close()

def actualizar_medicamento():
    try:
        connection = connect_to_database()
        with connection.cursor() as cursor:
            id_medicamento = int(input("Ingrese el ID del medicamento a actualizar: "))
            while True:
                nombre = input("Ingrese el nuevo nombre del medicamento: ").strip()
                if not nombre:
                    print("El nombre del medicamento no puede estar vacío.")
                    continue
                descripcion = input("Ingrese la nueva descripción del medicamento: ").strip()
                if not descripcion:
                    print("La descripción no puede estar vacía.")
                    continue
                break
            sql = "UPDATE `medicamento` SET `Nombre` = %s, `Descripcion` = %s WHERE `ID_Medicamento` = %s"
            cursor.execute(sql, (nombre, descripcion, id_medicamento))
        connection.commit()
        print("Medicamento actualizado con éxito.")
    except pymysql.MySQLError as e:
        print("Error al actualizar el medicamento:", e)
    finally:
        connection.close()

def eliminar_medicamento():
    try:
        connection = connect_to_database()
        with connection.cursor() as cursor:
            id_medicamento = int(input("Ingrese el ID del medicamento a eliminar: "))
            sql = "UPDATE `medicamento` SET `activo` = 0 WHERE `ID_Medicamento` = %s"
            cursor.execute(sql, (id_medicamento,))
        connection.commit()
        print("Medicamento eliminado con éxito del sistema.")
    except pymysql.MySQLError as e:
        print("Error al eliminar el medicamento:", e)
    finally:
        connection.close()


#Funcion CRUD completo para tabla Especialidades
def mantenimiento_especialidades():
    while True:
        print("\nMenú de Mantenimiento de Especialidades:")
        print("")
        print("1. Crear especialidad")
        print("2. Mostrar especialidades")
        print("3. Actualizar especialidad")
        print("4. Eliminar especialidad")
        print("5. Volver al menú principal")
        print("")
        opcion = input("Seleccione una opción: ") 

        if opcion == "1":
            crear_especialidad()
        elif opcion == "2":
            mostrar_especialidades()
        elif opcion == "3":
            actualizar_especialidad()
        elif opcion == "4":
            eliminar_especialidad()
        elif opcion == "5":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def crear_especialidad():
    try:
        connection = connect_to_database()
        with connection.cursor() as cursor:
            while True:
                nombre_especialidad = input("Ingrese el nombre de la especialidad: ").strip()
                if not nombre_especialidad:
                    print("El nombre de la especialidad no puede estar vacío.")
                    continue
                break
            sql = "INSERT INTO `especialidad` (`Nombre_Especialidad`) VALUES (%s)"
            cursor.execute(sql, (nombre_especialidad,))
        connection.commit()
        print("Especialidad creada con éxito.")
    except pymysql.MySQLError as e:
        print("Error al crear la especialidad:", e)
    finally:
        connection.close()

def mostrar_especialidades():
    try:
        connection = connect_to_database()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `especialidad` WHERE `activo` = 1"
            cursor.execute(sql)
            especialidades = cursor.fetchall()
            print("Listado de especialidades:")
            table = BeautifulTable(maxwidth=120)
            table.set_style(BeautifulTable.STYLE_GRID)
            table.columns.header = ["ID", "Nombre Especialidad"]
            for especialidad in especialidades:
                table.rows.append([especialidad[0], especialidad[1]])
            print(table)
    except pymysql.MySQLError as e:
        print("Error al obtener las especialidades:", e)
    finally:
        connection.close()

def actualizar_especialidad():
    try:
        connection = connect_to_database()
        with connection.cursor() as cursor:
            id_especialidad = int(input("Ingrese el ID de la especialidad a actualizar: "))
            while True:
                nombre_especialidad = input("Ingrese el nuevo nombre de la especialidad: ").strip()
                if not nombre_especialidad:
                    print("El nombre de la especialidad no puede estar vacío.")
                    continue
                break
            sql = "UPDATE `especialidad` SET `Nombre_Especialidad` = %s WHERE `ID_Especialidad` = %s"
            cursor.execute(sql, (nombre_especialidad, id_especialidad))
        connection.commit()
        print("Especialidad actualizada con éxito.")
    except pymysql.MySQLError as e:
        print("Error al actualizar la especialidad:", e)
    finally:
        connection.close()

def eliminar_especialidad():
    try:
        connection = connect_to_database()
        with connection.cursor() as cursor:
            id_especialidad = int(input("Ingrese el ID de la especialidad a eliminar: "))
            sql = "UPDATE `especialidad` SET `activo` = 0 WHERE `ID_Especialidad` = %s"
            cursor.execute(sql, (id_especialidad,))
        connection.commit()
        print("Especialidad eliminada con éxito del sistema.")
    except pymysql.MySQLError as e:
        print("Error al eliminar la especialidad:", e)
    finally:
        connection.close()


#Funcion CRUD completo para tabla Medicos
def mantenimiento_medicos():
    while True:
        print("\nMenú de Mantenimiento de Médicos:")
        print("1. Crear médico")
        print("2. Mostrar médicos")
        print("3. Actualizar médico")
        print("4. Eliminar médico")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_medico()
        elif opcion == "2":
            mostrar_medicos()
        elif opcion == "3":
            actualizar_medico()
        elif opcion == "4":
            eliminar_medico()
        elif opcion == "5":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def crear_medico():
    try:
        connection = connect_to_database()
        with connection.cursor() as cursor:
            while True:
                rut = input("Ingrese el RUT del profesional: ").strip()
                if not rut:
                    print("El RUT no puede estar vacío.")
                    continue
                
                nombre = input("Ingrese el nombre del profesional: ").strip()
                if not nombre:
                    print("El nombre no puede estar vacío.")
                    continue
                
                apellido = input("Ingrese el apellido del profesional: ").strip()
                if not apellido:
                    print("El apellido no puede estar vacío.")
                    continue
                
                telefono = input("Ingrese el teléfono del profesional: ").strip()
                if not telefono:
                    print("El teléfono no puede estar vacío.")
                    continue
                
                id_tipo_usuario = int(input("Ingrese el ID del tipo de usuario del profesional: "))
                break
            
            sql_profesional = """
                INSERT INTO `profesional` (`RUT`, `Nombre`, `Apellido`, `Telefono`, `ID_TipoUsuario`, `activo`)
                VALUES (%s, %s, %s, %s, %s, 1)
            """
            cursor.execute(sql_profesional, (rut, nombre, apellido, telefono, id_tipo_usuario))
            connection.commit()
            id_profesional = cursor.lastrowid

            agregar_especialidad = True
            while agregar_especialidad:
                id_especialidad = int(input("Ingrese el ID de la especialidad del profesional: "))
                sql_profesional_especialidad = """
                    INSERT INTO `profesional_especialidad` (`ID_Profesional`, `ID_Especialidad`)
                    VALUES (%s, %s)
                """
                cursor.execute(sql_profesional_especialidad, (id_profesional, id_especialidad))
                connection.commit()
                respuesta = input("¿Desea agregar otra especialidad? (s/n): ").lower()
                if respuesta != 's':
                    agregar_especialidad = False
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
            sql_login = """
                INSERT INTO `login` (`Usuario`, `Password`, `ID_TipoUsuario`)
                VALUES (%s, %s, %s)
            """
            cursor.execute(sql_login, (nombre_usuario, contrasena, id_tipo_usuario))
            connection.commit()
            print("Profesional y login creados con éxito.")
    except pymysql.MySQLError as e:
        print("Error al agregar el profesional:", e)
    finally:
        connection.close()

def mostrar_medicos():
    try:
        connection = connect_to_database()
        with connection.cursor() as cursor:
            sql = """
                SELECT p.ID_Profesional, p.RUT, p.Nombre, p.Apellido, p.Telefono, 
                       GROUP_CONCAT(e.Nombre_Especialidad SEPARATOR ', ') AS Especialidades
                FROM profesional p
                LEFT JOIN profesional_especialidad pe ON p.ID_Profesional = pe.ID_Profesional
                LEFT JOIN especialidad e ON pe.ID_Especialidad = e.ID_Especialidad
                WHERE p.activo = 1
                GROUP BY p.ID_Profesional
            """
            cursor.execute(sql)
            profesionales = cursor.fetchall()
            print("Listado de profesionales:")
            table = BeautifulTable(maxwidth=160)
            table.set_style(BeautifulTable.STYLE_GRID)
            table.columns.header = ["ID", "RUT", "Nombre", "Apellido", "Teléfono", "Especialidades"]
            for profesional in profesionales:
                table.rows.append(profesional)
            print(table)
    except pymysql.MySQLError as e:
        print("Error al obtener los profesionales:", e)
    finally:
        connection.close()

def actualizar_medico():
    try:
        connection = connect_to_database()
        with connection.cursor() as cursor:
            id_profesional = int(input("Ingrese el ID del médico a actualizar: "))
            while True:
                nombre = input("Ingrese el nuevo nombre del médico: ").strip()
                if not nombre:
                    print("El nombre no puede estar vacío.")
                    continue
                
                apellido = input("Ingrese el nuevo apellido del médico: ").strip()
                if not apellido:
                    print("El apellido no puede estar vacío.")
                    continue
                
                telefono = input("Ingrese el nuevo teléfono del médico: ").strip()
                if not telefono:
                    print("El teléfono no puede estar vacío.")
                    continue
                
                id_especialidad = int(input("Ingrese el nuevo ID de la especialidad del médico: "))
                id_tipo_usuario = int(input("Ingrese el nuevo ID del tipo de usuario del médico: "))
                break
            
            sql = """
                UPDATE `profesional` 
                SET `Nombre` = %s, `Apellido` = %s, `Telefono` = %s, 
                    `ID_Especialidad` = %s, `ID_TipoUsuario` = %s 
                WHERE `ID_Profesional` = %s
            """
            cursor.execute(sql, (nombre, apellido, telefono, id_especialidad, id_tipo_usuario, id_profesional))
            connection.commit()
            print("Médico actualizado con éxito.")
    except pymysql.MySQLError as e:
        print("Error al actualizar el médico:", e)
    finally:
        connection.close()
 
def eliminar_medico():
    try:
        connection = connect_to_database()
        with connection.cursor() as cursor:
            id_profesional = int(input("Ingrese el ID del médico a eliminar: "))
            sql = "UPDATE `profesional` SET `activo` = 0 WHERE `ID_Profesional` = %s"
            cursor.execute(sql, (id_profesional,))
            connection.commit()
            print("Médico eliminado con éxito del sistema.")
            
    except pymysql.MySQLError as e:
        print("Error al eliminar el médico:", e)
    finally:
        connection.close()


#Funcion CRUD completo para tabla Examenes
def mantenimiento_examenes():
    while True:
        print("\nMenú de Mantenimiento de Exámenes:")
        print("1. Crear examen")
        print("2. Mostrar exámenes")
        print("3. Actualizar examen")
        print("4. Eliminar examen")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_examen()
        elif opcion == "2":
            mostrar_examenes()
        elif opcion == "3":
            actualizar_examen()
        elif opcion == "4":
            eliminar_examen()
        elif opcion == "5":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def crear_examen():
    try:
        connection = connect_to_database()
        with connection.cursor() as cursor:
            while True:
                nombre = input("Ingrese el nombre del examen: ").strip()
                if not nombre:
                    print("El nombre del examen no puede estar vacío.")
                    continue
                descripcion = input("Ingrese la descripción del examen: ").strip()
                if not descripcion:
                    print("La descripción del examen no puede estar vacía.")
                    continue
                break
            sql = "INSERT INTO `examen` (`Nombre`, `Descripcion`) VALUES (%s, %s)"
            cursor.execute(sql, (nombre, descripcion))
        connection.commit()
        print("Examen creado con éxito.")
    except pymysql.MySQLError as e:
        print("Error al crear el examen:", e)
    finally:
        connection.close()

def mostrar_examenes():
    try:
        connection = connect_to_database()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `examen` WHERE `activo` = 1"
            cursor.execute(sql)
            examenes = cursor.fetchall()
            print("Listado de exámenes:")
            table = BeautifulTable(maxwidth=120)
            table.set_style(BeautifulTable.STYLE_GRID)
            table.columns.header = ["ID", "Nombre", "Descripción"]
            for examen in examenes:
                table.rows.append([examen[0], examen[1], examen[2]])
            print(table)
    except pymysql.MySQLError as e:
        print("Error al obtener los exámenes:", e)
    finally:
        connection.close()

def actualizar_examen():
    try:
        connection = connect_to_database()
        with connection.cursor() as cursor:
            id_examen = int(input("Ingrese el ID del examen a actualizar: "))
            while True:
                nombre = input("Ingrese el nuevo nombre del examen: ").strip()
                if not nombre:
                    print("El nombre del examen no puede estar vacío.")
                    continue
                descripcion = input("Ingrese la nueva descripción del examen: ").strip()
                if not descripcion:
                    print("La descripción del examen no puede estar vacía.")
                    continue
                break
            sql = "UPDATE `examen` SET `Nombre` = %s, `Descripcion` = %s WHERE `ID_Examen` = %s"
            cursor.execute(sql, (nombre, descripcion, id_examen))
        connection.commit()
        print("Examen actualizado con éxito.")
    except pymysql.MySQLError as e:
        print("Error al actualizar el examen:", e)
    finally:
        connection.close()

def eliminar_examen():
    try:
        connection = connect_to_database()
        with connection.cursor() as cursor:
            id_examen = int(input("Ingrese el ID del examen a eliminar: "))
            sql = "UPDATE `examen` SET `activo` = 0 WHERE `ID_Examen` = %s"
            cursor.execute(sql, (id_examen,))
            connection.commit()
            print("Examen eliminado con éxito del sistema.")
    except pymysql.MySQLError as e:
        print("Error al eliminar el examen:", e)
    finally:
        connection.close()