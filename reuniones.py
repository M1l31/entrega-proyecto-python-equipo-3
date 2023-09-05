import tkinter as tk
from tkinter import messagebox


def crear_reunion():
    fecha = fecha_entry.get()
    tema = tema_entry.get()
    detalles = detalles_text.get("1.0", tk.END)

    with open("reuniones.txt", 'a') as archivo:
        archivo.write(f"Fecha: {fecha}\n")
        archivo.write(f"Tema: {tema}\n")
        archivo.write(f"Detalles:\n{detalles}\n\n")

    messagebox.showinfo("Reunión Creada", "Reunión creada con éxito.")


def listar_reuniones():
    try:
        with open("reuniones.txt", 'r') as archivo:
            contenido = archivo.read()
            if not contenido:
                contenido = "No hay reuniones programadas."
            resultados_text.delete("1.0", tk.END)
            resultados_text.insert("1.0", contenido)
    except FileNotFoundError:
        resultados_text.delete("1.0", tk.END)
        resultados_text.insert("1.0", "No hay reuniones programadas.")


ventana = tk.Tk()
ventana.title("Gestión de Reuniones Escolares o de Padres")


fecha_label = tk.Label(ventana, text="Fecha:")
fecha_entry = tk.Entry(ventana)

tema_label = tk.Label(ventana, text="Tema:")
tema_entry = tk.Entry(ventana)

detalles_label = tk.Label(ventana, text="Detalles:")
detalles_text = tk.Text(ventana, height=5, width=30)


crear_button = tk.Button(ventana, text="Crear Reunión", command=crear_reunion)


listar_button = tk.Button(ventana, text="Listar Reuniones", command=listar_reuniones)


resultados_text = tk.Text(ventana, height=10, width=40)


fecha_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
fecha_entry.grid(row=0, column=1, padx=10, pady=5)
tema_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
tema_entry.grid(row=1, column=1, padx=10, pady=5)
detalles_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
detalles_text.grid(row=2, column=1, padx=10, pady=5)
crear_button.grid(row=3, column=0, columnspan=2, pady=10)
listar_button.grid(row=4, column=0, columnspan=2, pady=5)
resultados_text.grid(row=5, column=0, columnspan=2, padx=10, pady=5)


ventana.mainloop()
