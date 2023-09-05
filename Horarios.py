import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def guardar_horario():
    dia = dia_var.get()
    profesor = profesor_entry.get().strip()
    materia = materia_var.get().strip()
    modulo = modulo_var.get()

    if dia and profesor and materia and modulo:
        
        horario_actual = {
            "Dia": dia,
            "Modulo": int(modulo),
            "Profesor": profesor,
            "Materia": materia
        }
        
        
        horarios.append(horario_actual)
        
        
        horarios.sort(key=lambda x: (dias.index(x["Dia"]), x["Modulo"]))
        
        
        try:
            with open('horarios.txt', 'a') as archivo:  
                archivo.write(f"Día: {horario_actual['Dia']}\n")
                archivo.write(f"Módulo: {horario_actual['Modulo']}\n")
                archivo.write(f"Profesor: {horario_actual['Profesor']}\n")
                archivo.write(f"Materia: {horario_actual['Materia']}\n\n")
            messagebox.showinfo("Éxito", "Horario registrado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al guardar el horario: {str(e)}")
    else:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")


dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]


horarios = []


ventana = tk.Tk()
ventana.title("Gestión de Horarios")


dia_label = tk.Label(ventana, text="Día:")
dia_var = tk.StringVar()
dia_combobox = ttk.Combobox(ventana, textvariable=dia_var, values=dias)

profesor_label = tk.Label(ventana, text="Profesor:")
profesor_entry = tk.Entry(ventana)

materia_label = tk.Label(ventana, text="Materia:")
materia_var = tk.StringVar()
materia_combobox = ttk.Combobox(ventana, textvariable=materia_var, values=["Matematicas", "Lengua", "F.Cristiana", "Fisica", "Quimica", "Dibujo.Tecnico", "Taller", "Especialidad", "Historia", "Geografia", "F.Artistica", "Musica", "Biologia", "Estudio", "Logica.Matematica", "Informatica.Aplicada"])

modulo_label = tk.Label(ventana, text="Módulo:")
modulo_var = tk.StringVar()
modulo_combobox = ttk.Combobox(ventana, textvariable=modulo_var, values=[str(i) for i in range(1, 12)])


guardar_button = tk.Button(ventana, text="Guardar Horario", command=guardar_horario)


dia_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
dia_combobox.grid(row=0, column=1, padx=10, pady=5, columnspan=2, sticky="w")
profesor_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
profesor_entry.grid(row=1, column=1, padx=10, pady=5, columnspan=2, sticky="w")
materia_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
materia_combobox.grid(row=2, column=1, padx=10, pady=5, columnspan=2, sticky="w")
modulo_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
modulo_combobox.grid(row=3, column=1, padx=10, pady=5, columnspan=2, sticky="w")
guardar_button.grid(row=4, column=0, padx=10, pady=10, columnspan=3)


ventana.mainloop()
