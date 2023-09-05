import tkinter as tk
from tkinter import messagebox


def crear_curso():
    messagebox.showinfo("Crear Curso", "Opción 2.1: Creación de Cursos")
    import crear_curso
def asignar_estudiantes():
    messagebox.showinfo("Horarios de clase", "Opción 2.2: Asignación de Profes por Cursos")
    import Horarios
def horarios_clases():
    messagebox.showinfo("Leer de Horarios", "Opción 2.3: Leer Horarios de Clases")
    import Leer_Horarios
def gestion_aulas():
    messagebox.showinfo("Observaciones,Amonestaciones y Sanciones", "Opción 2.4: Gestión de Observaciones,Amonestaciones y Sanciones")
    import Sancion_Amonestacion_Observacion
def comunicacion_profesores():
    messagebox.showinfo("Leer Observaciones,Amonestaciones y Sanciones", "Opción 2.5: Leer Observaciones,Amonestaciones y Sanciones")
    import Leer_Sancion_Amonestacion_Observbacion
def gestion_materiales_didacticos():
    messagebox.showinfo("Gestión de Reuniones Escolares", "Opción 2.6: Gestión de Reuniones Escolares")
    import reuniones

ventana = tk.Tk()
ventana.title("Módulo 2: Gestión de Cursos")


crear_curso_button = tk.Button(ventana, text="2.1 Creación de Cursos", command=crear_curso)
asignar_estudiantes_button = tk.Button(ventana, text="2.2 Asignación de Profes por Cursos", command=asignar_estudiantes)
horarios_clases_button = tk.Button(ventana, text="2.3 Leer Horarios de Clases", command=horarios_clases)
gestion_aulas_button = tk.Button(ventana, text="2.4 Gestión de Observaciones,Amonestaciones y Sanciones", command=gestion_aulas)
comunicacion_profesores_button = tk.Button(ventana, text="2.5 Leer Observaciones,Amonestaciones y Sanciones", command=comunicacion_profesores)
gestion_materiales_didacticos_button = tk.Button(ventana, text="2.6 Gestión de Reuniones Escolares", command=gestion_materiales_didacticos)


crear_curso_button.pack(pady=10)
asignar_estudiantes_button.pack(pady=10)
horarios_clases_button.pack(pady=10)
gestion_aulas_button.pack(pady=10)
comunicacion_profesores_button.pack(pady=10)
gestion_materiales_didacticos_button.pack(pady=10)


ventana.mainloop()
