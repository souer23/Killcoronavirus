import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql

def menu_pantalla():
    global pantalla
    pantalla = Tk()
    pantalla.geometry("400x460")
    pantalla.title("Sistema Medico KillCoronaVirus")
    pantalla.iconbitmap("logo.ico")

    image = PhotoImage(file = "logo.gif")
    image = image.subsample(4,4)
    label = Label(image = image)
    label.pack()

    Label(text = "Acceso al Sistema", bg = "Teal", fg = "White", width = "300", height = "3", font=("Verdana", 12)).pack()
    Label(text="").pack()

    Button(text = "Iniciar Sesion", height = "3", width = "30", command = iniciar_sesion_doctor).pack()
    Label(text = "").pack()
    Button(text = "Perfil Administrador", height = "3", width = "30", command = iniciar_sesion_admin).pack()

    pantalla.mainloop()

def iniciar_sesion_doctor():
    global pantalla1
    pantalla1 = Toplevel(pantalla)
    pantalla1.geometry("400x250")
    pantalla1.title("Inicio de Sesion")
    pantalla1.iconbitmap("logo.ico")

    Label(pantalla1,text = "Por favor ingrese usuario y contraseña de Medico.",  bg = "Teal", fg = "White", width = "300", height = "3", font=("Verdana", 10)).pack()
    Label(pantalla1, text="").pack()

    global nombre_Medico_verify
    global contraseña_Medico_verify

    nombre_Medico_verify = StringVar()
    contraseña_Medico_verify = StringVar()
    
    global nombre_Medico_entry
    global contraseña_Medico_entry 

    Label(pantalla1, text = "Usuario").pack()
    nombre_Medico_entry = Entry (pantalla1, textvariable = nombre_Medico_verify)
    nombre_Medico_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text = "Contraseña").pack()
    contraseña_Medico_entry = Entry (pantalla1, textvariable = contraseña_Medico_verify)
    contraseña_Medico_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1, text = "Iniciar Sesion").pack()


def iniciar_sesion_admin():
    global pantalla1
    pantalla1 = Toplevel(pantalla)
    pantalla1.geometry("400x250")
    pantalla1.title("Inicio de Sesion")
    pantalla1.iconbitmap("logo.ico")

    Label(pantalla1,text = "Por favor ingrese usuario y contraseña de Administrador.",  bg = "Teal", fg = "White", width = "300", height = "3", font=("Verdana", 10)).pack()
    Label(pantalla1, text="").pack()

    global nombre_Admin_verify
    global contraseña_Admin_verify

    nombre_Admin_verify = StringVar()
    contraseña_Admin_verify = StringVar()
    
    global nombre_admin_entry
    global contraseña_admin_entry 

    Label(pantalla1, text = "Usuario").pack()
    nombre_admin_entry = Entry (pantalla1, textvariable = nombre_Admin_verify)
    nombre_admin_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text = "Contraseña").pack()
    contraseña_admin_entry = Entry (pantalla1, textvariable = contraseña_Admin_verify)
    contraseña_admin_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1, text = "Iniciar Sesion").pack()
menu_pantalla()