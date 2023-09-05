import tkinter as tk
from tkinter import messagebox

def buscar_informacion():
    nombre_buscar = nombre_buscar_entry.get()
    apellido_buscar = apellido_buscar_entry.get()
    archivo = "disciplina.txt"

    resultados_listbox.delete(0, tk.END)

    try:
        with open(archivo, 'r', encoding='latin-1') as archivo_displina:
            lineas = archivo_displina.readlines()
            registro_actual = {}
            registros_coincidentes = []

            for linea in lineas:
                linea = linea.strip()
                if not linea:
                    
                    if 'Nombre' in registro_actual and 'Apellido' in registro_actual:
                        if (
                            registro_actual['Nombre'] == nombre_buscar
                            and registro_actual['Apellido'] == apellido_buscar
                        ):
                            registros_coincidentes.append(registro_actual)
                    registro_actual = {}
                else:
                    
                    clave, valor = linea.split(": ", 1)
                    registro_actual[clave] = valor

            if registros_coincidentes:
                for registro in registros_coincidentes:
                    for clave, valor in registro.items():
                        resultados_listbox.insert(tk.END, f"{clave}: {valor}")
                    resultados_listbox.insert(tk.END, "")  
            else:
                resultados_listbox.insert(tk.END, "No se encontró información para el nombre y apellido proporcionados.")

    except FileNotFoundError:
        resultados_listbox.insert(tk.END, "El archivo 'displina.txt' no existe.")
    except Exception as e:
        resultados_listbox.insert(tk.END, f"Error al buscar información: {str(e)}")


ventana = tk.Tk()
ventana.title("Buscar Información en disiplina.txt")


nombre_buscar_label = tk.Label(ventana, text="Nombre:")
nombre_buscar_entry = tk.Entry(ventana)

apellido_buscar_label = tk.Label(ventana, text="Apellido:")
apellido_buscar_entry = tk.Entry(ventana)


buscar_button = tk.Button(ventana, text="Buscar", command=buscar_informacion)


resultados_listbox = tk.Listbox(ventana, width=50, height=10)


nombre_buscar_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
nombre_buscar_entry.grid(row=0, column=1, padx=10, pady=5)
apellido_buscar_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
apellido_buscar_entry.grid(row=1, column=1, padx=10, pady=5)
buscar_button.grid(row=2, columnspan=2, pady=10)
resultados_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5)


ventana.mainloop()
