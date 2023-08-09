import tkinter as tk
import menu

class Usuario():
    numUsuarios = 0

    def __init__(self, nombre, contra):
        self.nombre = nombre
        self.contra = contra
        self.conectado = False
        self.intentos = 3
        Usuario.numUsuarios += 1

    def conectar(self):
        self.conectado = True

    def desconectar(self):
        self.conectado = False

    def __str__(self):
        conect = "Conectado" if self.conectado else "Desconectado"
        return f"Mi nombre de usuario es {self.nombre} y estoy {conect}"

class VentanaAsistencia(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Registro de Asistencia")
        self.geometry("400x300")
        self.label_asistencia = tk.Label(self, text="Registro de Asistencia", font=("Helvetica", 16, "bold"))
        self.label_asistencia.pack(pady=10)

        # Aquí puedes agregar componentes para llevar el registro de asistencia de los alumnos

# Lista para almacenar los usuarios registrados
usuarios_registrados = []

# Función para registrar un nuevo usuario
def registrar_usuario():
    nombre = entry_usuario.get()
    contrasena = entry_contrasena.get()
    nuevo_usuario = Usuario(nombre, contrasena)
    usuarios_registrados.append(nuevo_usuario)
    label_estado.config(text=f"Usuario {nombre} registrado con éxito.", fg="green")

# Función para validar las credenciales ingresadas en la interfaz
def validar_credenciales():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    # Buscar el usuario en la lista de usuarios registrados
    for usuario_obj in usuarios_registrados:
        if usuario_obj.nombre == usuario and usuario_obj.contra == contrasena:
            label_estado.config(text="Inicio de sesión exitoso", fg="green")
            usuario_obj.conectar()
            # Abre la ventana de asistencia al iniciar sesión exitosamente
            ventana_asistencia = VentanaAsistencia(ventana)
            ventana_asistencia.mainloop()
            return

    label_estado.config(text="Credenciales incorrectas", fg="red")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Inicio de Sesión y Registro")

# Etiqueta de título
label_titulo = tk.Label(ventana, text="ITS Villada-Preceptoria", font=("Helvetica", 16, "bold"))
label_titulo.pack(pady=10)

# Etiqueta y campo de entrada para el usuario
label_usuario = tk.Label(ventana, text="Usuario:", font=("Helvetica", 12))
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(ventana, font=("Helvetica", 12))
entry_usuario.pack(pady=5)

# Etiqueta y campo de entrada para la contraseña
label_contrasena = tk.Label(ventana, text="Contraseña:", font=("Helvetica", 12))
label_contrasena.pack(pady=5)
entry_contrasena = tk.Entry(ventana, show="*", font=("Helvetica", 12))  # La contraseña se muestra como asteriscos
entry_contrasena.pack(pady=5)

# Botón de inicio de sesión
boton_iniciar_sesion = tk.Button(ventana, text="Iniciar Sesión", font=("Helvetica", 14), command=validar_credenciales)
boton_iniciar_sesion.pack(pady=10)

# Botón de registro
boton_registrar_usuario = tk.Button(ventana, text="Registrar Usuario", font=("Helvetica", 14), command=registrar_usuario)
boton_registrar_usuario.pack(pady=5)

# Etiqueta para mostrar el estado del inicio de sesión o registro
label_estado = tk.Label(ventana, text="", font=("Helvetica", 12))
label_estado.pack()

# Ejecutar la ventana
ventana.mainloop()
