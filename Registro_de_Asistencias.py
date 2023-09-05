import tkinter as tk
from datetime import datetime


def registrar_asistencia():
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    curso = curso_var.get()
    fecha = fecha_entry.get()
    falta = falta_var.get()
    justificada = justificada_var.get()

   
    if nombre and apellido and fecha:
        
        registro = f"Nombre: {nombre}\nApellido: {apellido}\nCurso: {curso}\nInasistencia: {falta} : {fecha} : {justificada}\n\n"
        try:
            with open('asistencia.txt', 'a') as archivo:
                archivo.write(registro)
            resultado_label.config(text="Registro exitoso.", fg="green")
            
            nombre_entry.delete(0, tk.END)
            apellido_entry.delete(0, tk.END)
            curso_var.set("")  
            fecha_entry.delete(0, tk.END)
            falta_var.set("1")  
            justificada_var.set("Justificada")  
        except FileNotFoundError:
            resultado_label.config(text="El archivo 'asistencia.txt' no existe.", fg="red")
        except Exception as e:
            resultado_label.config(text=f"Error al registrar: {str(e)}", fg="red")
    else:
        resultado_label.config(text="Por favor, complete nombre, apellido y fecha.", fg="red")


ventana = tk.Tk()
ventana.title("Registro de Asistencia Estudiantil")


nombre_label = tk.Label(ventana, text="Nombre:")
nombre_entry = tk.Entry(ventana)

apellido_label = tk.Label(ventana, text="Apellido:")
apellido_entry = tk.Entry(ventana)


cursos = ["1A", "1B", "1C", "2A", "2B", "2C", "3A", "3B", "3C", "4A", "4B", "4C", "5A", "5B", "5C", "6A", "6B", "6C", "7A", "7B", "7C"]
curso_var = tk.StringVar()
curso_label = tk.Label(ventana, text="Curso:")
curso_menu = tk.OptionMenu(ventana, curso_var, *cursos)


fecha_label = tk.Label(ventana, text="Fecha:")
fecha_entry = tk.Entry(ventana)


falta_var = tk.StringVar()
falta_var.set("1")  
falta_label = tk.Label(ventana, text="Tipo de Falta:")
falta_menu = tk.OptionMenu(ventana, falta_var, "1", "1/2", "1/4")


justificada_var = tk.StringVar()
justificada_var.set("Justificada")  
justificada_label = tk.Label(ventana, text="Justificada/Injustificada:")
justificada_menu = tk.OptionMenu(ventana, justificada_var, "Justificada", "Injustificada")


registrar_button = tk.Button(ventana, text="Registrar", command=registrar_asistencia)


resultado_label = tk.Label(ventana, text="", fg="green")


nombre_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
nombre_entry.grid(row=0, column=1, padx=10, pady=5)
apellido_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
apellido_entry.grid(row=1, column=1, padx=10, pady=5)
curso_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
curso_menu.grid(row=2, column=1, padx=10, pady=5)
fecha_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
fecha_entry.grid(row=3, column=1, padx=10, pady=5)
falta_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
falta_menu.grid(row=4, column=1, padx=10, pady=5)
justificada_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
justificada_menu.grid(row=5, column=1, padx=10, pady=5)
registrar_button.grid(row=6, columnspan=2, pady=10)
resultado_label.grid(row=7, columnspan=2, padx=10, pady=5)


ventana.mainloop()
