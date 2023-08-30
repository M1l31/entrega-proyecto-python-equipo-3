import tkinter as tk
import importlib

def importar_modulo(modulo):
    importlib.import_module(modulo)

class label_menu (tk.Tk):
    
    root = tk.Tk()
    root.title("MENU")

    label = tk.Label(root, text="-------------------MENU------------------")
    label.pack()

    button1 = tk.Button(root, text="Sanciones, Observaciones y Amonestaciones", command=lambda: importar_modulo("Sanciones"))
    button1.pack()

    separator1 = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN)
    separator1.pack(fill=tk.X, padx=10, pady=5)

    button2 = tk.Button(root, text="Asistencias", command=lambda: importar_modulo("Asistencia"))
    button2.pack()

    separator2 = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN)
    separator2.pack(fill=tk.X, padx=10, pady=5)

    button3 = tk.Button(root, text="Agregar alumno", command=lambda: importar_modulo("Alumnos"))
    button3.pack()

    root.mainloop()