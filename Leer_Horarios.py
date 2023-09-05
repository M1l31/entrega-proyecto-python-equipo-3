import tkinter as tk
from tkinter import ttk


def mostrar_horarios():
    dia_seleccionado = dia_var.get()
    resultado_text.delete(1.0, tk.END)  

    try:
        with open('horarios.txt', 'r') as archivo:
            lineas = archivo.readlines()
            horarios_dia = []
            horario_actual = {}
            encontrado = False

            for linea in lineas:
                linea = linea.strip()
                if linea.startswith("Día:"):
                   
                    if horario_actual:
                        horarios_dia.append(horario_actual)
                        horario_actual = {}
                    horario_actual["Dia"] = linea.replace("Día: ", "")
                elif linea.startswith("Módulo:"):
                    horario_actual["Modulo"] = linea.replace("Módulo: ", "")
                elif linea.startswith("Profesor:"):
                    horario_actual["Profesor"] = linea.replace("Profesor: ", "")
                elif linea.startswith("Materia:"):
                    horario_actual["Materia"] = linea.replace("Materia: ", "")

            
            if horario_actual and horario_actual["Dia"] == dia_seleccionado:
                horarios_dia.append(horario_actual)

            if horarios_dia:
                for horario in horarios_dia:
                    resultado_text.insert(tk.END, f"Día: {horario['Dia']}\n")
                    resultado_text.insert(tk.END, f"Módulo: {horario['Modulo']}\n")
                    resultado_text.insert(tk.END, f"Profesor: {horario['Profesor']}\n")
                    resultado_text.insert(tk.END, f"Materia: {horario['Materia']}\n\n")
                    encontrado = True

            if not encontrado:
                resultado_text.insert(tk.END, f"No se encontraron horarios para el día '{dia_seleccionado}'.")
    except FileNotFoundError:
        resultado_text.insert(tk.END, "El archivo 'horarios.txt' no existe.\n")


ventana = tk.Tk()
ventana.title("Lectura de Horarios por Día")


dia_label = tk.Label(ventana, text="Seleccionar Día:")
dia_var = tk.StringVar()
dia_combobox = ttk.Combobox(ventana, textvariable=dia_var, values=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"])


mostrar_button = tk.Button(ventana, text="Mostrar Horarios", command=mostrar_horarios)


resultado_text = tk.Text(ventana, height=15, width=60)


dia_label.pack(pady=5)
dia_combobox.pack(pady=5)
mostrar_button.pack(pady=5)
resultado_text.pack(pady=10)


ventana.mainloop()
