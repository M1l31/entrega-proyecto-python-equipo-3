import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def crear_curso():
    curso = curso_var.get()
    especialidad = especialidad_var.get()
    cantidad_alumnos = alumnos_entry.get()
    
    if curso and especialidad and cantidad_alumnos:
        
        registro_curso = f"Curso: {curso}\nEspecialidad: {especialidad}\nAlumnos: {cantidad_alumnos}\n\n"
        
        try:
            with open('cursos.txt', 'a') as archivo:
                archivo.write(registro_curso)
            messagebox.showinfo("Éxito", "Curso creado correctamente y guardado en 'cursos.txt'.")
            curso_var.set("")  
            especialidad_var.set("")  
            alumnos_entry.delete(0, tk.END)  
        except Exception as e:
            messagebox.showerror("Error al guardar", f"Ocurrió un error al guardar el curso: {str(e)}")
    else:
        messagebox.showwarning("Campos Vacíos", "Por favor, completa todos los campos.")


ventana = tk.Tk()
ventana.title("Creación de Cursos")


curso_label = tk.Label(ventana, text="Curso:")
cursos = ["1A", "1B", "1C", "2A", "2B", "2C", "3A", "3B", "3C", "4A", "4B", "4C", "5A", "5B", "5C", "6A", "6B", "6C", "7A", "7B", "7C"]
curso_var = tk.StringVar()
curso_menu = ttk.Combobox(ventana, textvariable=curso_var, values=cursos)
curso_menu.set("")  


especialidad_label = tk.Label(ventana, text="Especialidad:")
especialidades = ["Especialidad Nula", "Electrónica", "Electromecánica", "Programación"]
especialidad_var = tk.StringVar()
especialidad_menu = ttk.Combobox(ventana, textvariable=especialidad_var, values=especialidades)
especialidad_menu.set("")  


alumnos_label = tk.Label(ventana, text="Cantidad de Alumnos:")
alumnos_entry = tk.Entry(ventana)


crear_curso_button = tk.Button(ventana, text="Crear Curso", command=crear_curso)


curso_label.pack()
curso_menu.pack(pady=5)
especialidad_label.pack()
especialidad_menu.pack(pady=5)
alumnos_label.pack()
alumnos_entry.pack(pady=5)
crear_curso_button.pack(pady=10)


ventana.mainloop()
