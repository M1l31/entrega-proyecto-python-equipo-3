import tkinter as tk
from tkinter import simpledialog, messagebox

class AsistenciaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Asistencias, Sanciones y Amonestaciones")
        
        self.menu_bar = tk.Menu(self.root)
        
        self.asistencia_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.asistencia_menu.add_command(label="Registrar Asistencia", command=self.registrar_asistencia)
        self.menu_bar.add_cascade(label="Asistencias", menu=self.asistencia_menu)
        
        self.sanciones_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.sanciones_menu.add_command(label="Registrar Sanción", command=self.registrar_sancion)
        self.menu_bar.add_cascade(label="Sanciones", menu=self.sanciones_menu)
        
        self.amonestaciones_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.amonestaciones_menu.add_command(label="Registrar Amonestación", command=self.registrar_amonestacion)
        self.menu_bar.add_cascade(label="Amonestaciones", menu=self.amonestaciones_menu)
        
        self.root.config(menu=self.menu_bar)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.registros = []

    def registrar_asistencia(self):
        nombre = simpledialog.askstring("Registrar Asistencia", "Ingrese el nombre:")
        if nombre:
            self.registros.append(f"Asistencia - Nombre: {nombre}")
    
    def registrar_sancion(self):
        nombre = simpledialog.askstring("Registrar Sanción", "Ingrese el nombre:")
        motivo = simpledialog.askstring("Registrar Sanción", "Ingrese el motivo de la sanción:")
        if nombre and motivo:
            self.registros.append(f"Sanción - Nombre: {nombre}, Motivo: {motivo}")
    
    def registrar_amonestacion(self):
        nombre = simpledialog.askstring("Registrar Amonestación", "Ingrese el nombre:")
        motivo = simpledialog.askstring("Registrar Amonestación", "Ingrese el motivo de la amonestación:")
        if nombre and motivo:
            self.registros.append(f"Amonestación - Nombre: {nombre}, Motivo: {motivo}")
    
    def on_closing(self):
        if messagebox.askokcancel("Salir", "¿Estás seguro que quieres salir? Los datos no guardados se perderán."):
            self.guardar_registros()
            self.root.destroy()
    
    def guardar_registros(self):
        with open("registros.txt", "w") as file:
            for registro in self.registros:
                file.write(registro + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = AsistenciaApp(root)
    root.mainloop()

    "comentario"
    "comentario"
    
    
