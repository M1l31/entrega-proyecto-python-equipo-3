import tkinter as tk

# Función para registrar un estudiante
def registrar_estudiante():
    # Obtener los valores de los campos de entrada
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    edad = edad_entry.get()
    telefono = telefono_entry.get()
    nombre_padres = padres_entry.get()
    correo = correo_entry.get()
    obra_social = obra_social_entry.get()
    barrio = barrio_entry.get()

    # Validar que se ingresen todos los campos
    if nombre and apellido and edad and telefono and nombre_padres and correo and obra_social and barrio:
        # Formatear los datos con etiquetas
        datos_estudiante = f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nTelefono: {telefono}\nNombre de los Padres: {nombre_padres}\nCorreo: {correo}\nObra Social: {obra_social}\nBarrio: {barrio}\n\n"
        try:
            # Abrir el archivo en modo de adición (a) y escribir los datos
            with open('estudiantes.txt', 'a') as archivo:
                archivo.write(datos_estudiante)
            resultado_label.config(text="Estudiante registrado exitosamente.")
            # Limpiar los campos de entrada después del registro
            nombre_entry.delete(0, tk.END)
            apellido_entry.delete(0, tk.END)
            edad_entry.delete(0, tk.END)
            telefono_entry.delete(0, tk.END)
            padres_entry.delete(0, tk.END)
            correo_entry.delete(0, tk.END)
            obra_social_entry.delete(0, tk.END)
            barrio_entry.delete(0, tk.END)
        except Exception as e:
            resultado_label.config(text=f"Error al registrar estudiante: {str(e)}")
    else:
        resultado_label.config(text="Por favor, complete todos los campos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Registro de Estudiantes")

# Crear etiquetas y campos de entrada
nombre_label = tk.Label(ventana, text="Nombre:")
nombre_entry = tk.Entry(ventana)

apellido_label = tk.Label(ventana, text="Apellido:")
apellido_entry = tk.Entry(ventana)

edad_label = tk.Label(ventana, text="Edad:")
edad_entry = tk.Entry(ventana)

telefono_label = tk.Label(ventana, text="Telefono:")
telefono_entry = tk.Entry(ventana)

padres_label = tk.Label(ventana, text="Nombre de los Padres:")
padres_entry = tk.Entry(ventana)

correo_label = tk.Label(ventana, text="Correo:")
correo_entry = tk.Entry(ventana)

obra_social_label = tk.Label(ventana, text="Obra Social:")
obra_social_entry = tk.Entry(ventana)

barrio_label = tk.Label(ventana, text="Barrio:")
barrio_entry = tk.Entry(ventana)

# Crear botón de registro
registrar_button = tk.Button(ventana, text="Registrar", command=registrar_estudiante)

# Crear etiqueta para mostrar resultados
resultado_label = tk.Label(ventana, text="")

# Colocar elementos en la ventana
nombre_label.grid(row=0, column=0)
nombre_entry.grid(row=0, column=1)
apellido_label.grid(row=1, column=0)
apellido_entry.grid(row=1, column=1)
edad_label.grid(row=2, column=0)
edad_entry.grid(row=2, column=1)
telefono_label.grid(row=3, column=0)
telefono_entry.grid(row=3, column=1)
padres_label.grid(row=4, column=0)
padres_entry.grid(row=4, column=1)
correo_label.grid(row=5, column=0)
correo_entry.grid(row=5, column=1)
obra_social_label.grid(row=6, column=0)
obra_social_entry.grid(row=6, column=1)
barrio_label.grid(row=7, column=0)
barrio_entry.grid(row=7, column=1)
registrar_button.grid(row=8, columnspan=2)
resultado_label.grid(row=9, columnspan=2)


ventana.mainloop()
