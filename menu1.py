import tkinter as tk


def registrar_estudiantes():
    print("Opción 1.1 - Registro de Estudiantes")
    import Registro_de_Estudiantes
def actualizar_informacion_estudiantil():
    print("Opción 1.2 - Actualización de Información Estudiantil")
    import Informes_Estudiantes
def buscar_y_filtrar_estudiantes():
    print("Opción 1.3 - Búsqueda y Filtros de Estudiantes")
    import Busqueda_Estudiantes_corregir
def registrar_asistencia():
    print("Opción 1.4 - Registro de Asistencia")
    import Registro_de_Asistencias
def generar_informes_de_asistencia():
    print("Opción 1.5 - Generación de Informes de Asistencia")
    import Leer_Asistencia
def menu2():
    print("Opción 1.6 - Menu 2")
    import menu2
def Leer_Informes():
    print("Opción 1.7 - Leer informes")
    import Leer_Informes

ventana = tk.Tk()
ventana.title("Menú de Gestión de Estudiantes")


boton_registrar_estudiantes = tk.Button(ventana, text="Registrar Estudiantes", command=registrar_estudiantes)
boton_actualizar_informacion = tk.Button(ventana, text="Informe Estudiantil", command=actualizar_informacion_estudiantil)
boton_buscar_filtrar = tk.Button(ventana, text="Búsqueda y Filtros de Estudiantes", command=buscar_y_filtrar_estudiantes)
boton_registrar_asistencia = tk.Button(ventana, text="Registrar Asistencia", command=registrar_asistencia)
boton_generar_informes = tk.Button(ventana, text="Leer Asistencia", command=generar_informes_de_asistencia)
boton_menu2 = tk.Button(ventana, text="Menu2 (Horarios,disiplina y etc)", command=menu2)
boton_Leer_Informe = tk.Button(ventana, text="Leer Informes (preceptores)", command=Leer_Informes)
boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)


boton_registrar_estudiantes.pack(pady=10)
boton_actualizar_informacion.pack(pady=10)
boton_buscar_filtrar.pack(pady=10)
boton_registrar_asistencia.pack(pady=10)
boton_generar_informes.pack(pady=10)
boton_menu2.pack(pady=10)
boton_Leer_Informe.pack(pady=10)
boton_salir.pack(pady=10)
ventana.mainloop()
