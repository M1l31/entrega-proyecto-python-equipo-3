import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def verificar_estudiante(nombre, apellido):
    try:
        with open('estudiantes.txt', 'r') as archivo:
            contenido = archivo.read()
            registros = contenido.split('\n\n')  
            for registro in registros:
                if nombre in registro and apellido in registro:
                    return True
            return False
    except FileNotFoundError:
        return False


def registrar_disciplina():
    nombre = nombre_entry.get().strip()
    apellido = apellido_entry.get().strip()
    cantidad = cantidad_var.get()
    disciplina = disciplina_var.get()
    razon = razon_entry.get().strip()
    fecha = fecha_entry.get().strip()

    if nombre and apellido and cantidad and disciplina and razon and fecha:
        
        if verificar_estudiante(nombre, apellido):
            registro = f"Nombre: {nombre}\nApellido: {apellido}\nCantidad: {cantidad}\nDisciplina: {disciplina}\nRazón: {razon}\nFecha: {fecha}\n\n"

            
            try:
                with open('disciplina.txt', 'a') as archivo:  
                    archivo.write(registro)
                messagebox.showinfo("Éxito", "Registro de disciplina guardado correctamente.")
                nombre_entry.delete(0, tk.END)  
                apellido_entry.delete(0, tk.END)  
                cantidad_var.set("")  
                disciplina_combobox.set("")  
                razon_entry.delete(0, tk.END)  
                fecha_entry.delete(0, tk.END)  
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error al guardar el registro: {str(e)}")
        else:
            messagebox.showerror("Error", "El estudiante no se encuentra en la lista de estudiantes.")
    else:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")


ventana = tk.Tk()
ventana.title("Registro de Disciplina")


nombre_label = tk.Label(ventana, text="Nombre:")
nombre_entry = tk.Entry(ventana)

apellido_label = tk.Label(ventana, text="Apellido:")
apellido_entry = tk.Entry(ventana)

cantidad_label = tk.Label(ventana, text="Cantidad:")
cantidad_var = tk.StringVar()
cantidad_entry = tk.Entry(ventana, textvariable=cantidad_var)

disciplina_label = tk.Label(ventana, text="Disciplina:")
disciplina_var = tk.StringVar()
disciplina_combobox = ttk.Combobox(ventana, textvariable=disciplina_var, values=["Observación", "Sanción", "Amonestación"])

razon_label = tk.Label(ventana, text="Razón:")
razon_entry = tk.Entry(ventana)

fecha_label = tk.Label(ventana, text="Fecha:")
fecha_entry = tk.Entry(ventana)


registrar_button = tk.Button(ventana, text="Registrar Disciplina", command=registrar_disciplina)


nombre_label.pack(padx=10, pady=5)
nombre_entry.pack(padx=10, pady=5)
apellido_label.pack(padx=10, pady=5)
apellido_entry.pack(padx=10, pady=5)
cantidad_label.pack(padx=10, pady=5)
cantidad_entry.pack(padx=10, pady=5)
disciplina_label.pack(padx=10, pady=5)
disciplina_combobox.pack(padx=10, pady=5)
razon_label.pack(padx=10, pady=5)
razon_entry.pack(padx=10, pady=5)
fecha_label.pack(padx=10, pady=5)
fecha_entry.pack(padx=10, pady=5)
registrar_button.pack(pady=10)


ventana.mainloop()
