import tkinter as tk


def registrar_comportamiento():
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    comportamiento = comportamiento_entry.get()

    
    if nombre and apellido and comportamiento:
        informe = f"Nombre: {nombre}\nApellido: {apellido}\nComportamiento: {comportamiento}\n\n"
        try:
            with open('informe.txt', 'a') as archivo:
                archivo.write(informe)
            resultado_label.config(text="Comportamiento registrado exitosamente.", fg="green")
            
            nombre_entry.delete(0, tk.END)
            apellido_entry.delete(0, tk.END)
            comportamiento_entry.delete(0, tk.END)
        except FileNotFoundError:
            resultado_label.config(text="El archivo 'informe.txt' no existe.", fg="red")
        except Exception as e:
            resultado_label.config(text=f"Error al registrar comportamiento: {str(e)}", fg="red")
    else:
        resultado_label.config(text="Por favor, complete todos los campos.", fg="red")


ventana = tk.Tk()
ventana.title("Registro de Comportamiento Estudiantil")


nombre_label = tk.Label(ventana, text="Nombre:")
nombre_entry = tk.Entry(ventana)

apellido_label = tk.Label(ventana, text="Apellido:")
apellido_entry = tk.Entry(ventana)

comportamiento_label = tk.Label(ventana, text="Comportamiento:")
comportamiento_entry = tk.Entry(ventana)


registrar_button = tk.Button(ventana, text="Registrar", command=registrar_comportamiento)


resultado_label = tk.Label(ventana, text="", fg="green")


nombre_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
nombre_entry.grid(row=0, column=1, padx=10, pady=5)
apellido_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
apellido_entry.grid(row=1, column=1, padx=10, pady=5)
comportamiento_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
comportamiento_entry.grid(row=2, column=1, padx=10, pady=5)
registrar_button.grid(row=3, columnspan=2, pady=10)
resultado_label.grid(row=4, columnspan=2, padx=10, pady=5)

ventana.mainloop()
