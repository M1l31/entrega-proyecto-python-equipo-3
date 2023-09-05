import tkinter as tk


def buscar_informacion():
    nombre_buscar = nombre_buscar_entry.get()
    apellido_buscar = apellido_buscar_entry.get()

    resultados_listbox.delete(0, tk.END)  

    try:
        with open('estudiantes.txt', 'r') as archivo:
            lineas = archivo.read().split('\n\n')  
            encontrado = False

            for estudiante in lineas:
                estudiante_info = estudiante.strip().split('\n')
                nombre = estudiante_info[0].split(': ')[1]
                apellido = estudiante_info[1].split(': ')[1]

                if nombre.lower() == nombre_buscar.lower() and apellido.lower() == apellido_buscar.lower():
                    resultados_listbox.insert(tk.END, f"Nombre: {nombre}")
                    resultados_listbox.insert(tk.END, f"Apellido: {apellido}")
                    resultados_listbox.insert(tk.END, estudiante_info[2])  
                    resultados_listbox.insert(tk.END, estudiante_info[3])  
                    resultados_listbox.insert(tk.END, estudiante_info[4])  
                    resultados_listbox.insert(tk.END, estudiante_info[5])  
                    resultados_listbox.insert(tk.END, estudiante_info[6])  
                    resultados_listbox.insert(tk.END, estudiante_info[7])  
                    encontrado = True

            if not encontrado:
                resultados_listbox.insert(tk.END, "No se encontró información para el nombre y apellido proporcionados.")

    except FileNotFoundError:
        resultados_listbox.insert(tk.END, "El archivo 'estudiantes.txt' no existe.")
    except Exception as e:
        resultados_listbox.insert(tk.END, f"Error al buscar información: {str(e)}")


def descargar_archivo():
    contenido = resultados_listbox.get(0, tk.END)
    
    try:
        with open('informacion_busqueda.txt', 'w') as archivo:
            for linea in contenido:
                archivo.write(linea + '\n')
        resultados_listbox.insert(tk.END, "Archivo 'informacion_busqueda.txt' descargado con éxito.")
    except Exception as e:
        resultados_listbox.insert(tk.END, f"Error al descargar el archivo: {str(e)}")


ventana = tk.Tk()
ventana.title("Buscar Información de Estudiantes")


nombre_buscar_label = tk.Label(ventana, text="Nombre:")
nombre_buscar_entry = tk.Entry(ventana)

apellido_buscar_label = tk.Label(ventana, text="Apellido:")
apellido_buscar_entry = tk.Entry(ventana)


buscar_button = tk.Button(ventana, text="Buscar", command=buscar_informacion)


resultados_listbox = tk.Listbox(ventana, width=50, height=10)


descargar_button = tk.Button(ventana, text="Descargar Archivo", command=descargar_archivo)


nombre_buscar_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
nombre_buscar_entry.grid(row=0, column=1, padx=10, pady=5)
apellido_buscar_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
apellido_buscar_entry.grid(row=1, column=1, padx=10, pady=5)
buscar_button.grid(row=2, columnspan=2, pady=10)
resultados_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
descargar_button.grid(row=4, columnspan=2, pady=10)


ventana.mainloop()
