import tkinter as tk
from captcha.image import ImageCaptcha
import random
import os
from PIL import ImageTk, Image


CAPTCHA_IMAGE_FOLDER = 'captcha_images'


captcha = ImageCaptcha()


current_captcha = ""
current_captcha_image = None


def generar_captcha():
    global current_captcha, current_captcha_image

    captcha_text = ''.join(random.choice('0123456789ABCDEF') for _ in range(6))
    captcha_image = captcha.generate_image(captcha_text)

    
    captcha_image.save(os.path.join(CAPTCHA_IMAGE_FOLDER, 'captcha.png'))

    current_captcha = captcha_text
    current_captcha_image = ImageTk.PhotoImage(Image.open(os.path.join(CAPTCHA_IMAGE_FOLDER, 'captcha.png')))
    
    captcha_label.config(image=current_captcha_image)
    captcha_label.image = current_captcha_image


def verificar_captcha(input_text, captcha_text):
    return input_text == captcha_text


def iniciar_sesion():
    usuario = usuario_entry.get()
    contrasena = contrasena_entry.get()
    captcha_input = captcha_entry.get()

    if verificar_credenciales(usuario, contrasena):
        if verificar_captcha(captcha_input, current_captcha):
            resultado_label.config(text='😃 Inicio de sesión exitoso. 😃')
            import menu1
        else:
            resultado_label.config(text='❌ Captcha incorrecto. Inténtalo de nuevo. ❌')
    else:
        resultado_label.config(text='❌ Credenciales incorrectas. Inténtalo de nuevo. ❌')


def verificar_credenciales(usuario, contrasena):
    try:
        with open('usuarios.txt', 'r') as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                usuario_guardado, contrasena_guardada = linea.strip().split(':')
                if usuario == usuario_guardado and contrasena == contrasena_guardada:
                    return True
    except FileNotFoundError:
        print("El archivo 'usuarios.txt' no existe.")
    return False


def registrar_usuario():
    usuario = usuario_entry.get()
    contrasena = contrasena_entry.get()
    
    if usuario and contrasena:
        if not verificar_credenciales(usuario, contrasena):
            with open('usuarios.txt', 'a') as archivo:
                archivo.write(f"{usuario}:{contrasena}\n")
            resultado_label.config(text='✅ Registro exitoso. Ahora puedes iniciar sesión. ✅')
        else:
            resultado_label.config(text='❌ El usuario ya existe. Inténtalo con otro nombre de usuario. ❌')
    else:
        resultado_label.config(text='❌ Por favor, ingresa un nombre de usuario y una contraseña. ❌')


if not os.path.exists(CAPTCHA_IMAGE_FOLDER):
    os.makedirs(CAPTCHA_IMAGE_FOLDER)


ventana = tk.Tk()
ventana.title("Inicio de Sesión")


usuario_label = tk.Label(ventana, text="Usuario:")
usuario_entry = tk.Entry(ventana)
contrasena_label = tk.Label(ventana, text="Contraseña:")
contrasena_entry = tk.Entry(ventana, show="*")
captcha_label = tk.Label(ventana, text="CAPTCHA:")
captcha_label_image = tk.Label(ventana)
captcha_entry = tk.Entry(ventana)
resultado_label = tk.Label(ventana, text="")


iniciar_sesion_button = tk.Button(ventana, text="Iniciar Sesión 😃", command=iniciar_sesion)
registrar_button = tk.Button(ventana, text="Registrarse ✅", command=registrar_usuario)


usuario_label.pack()
usuario_entry.pack()
contrasena_label.pack()
contrasena_entry.pack()
captcha_label.pack()
captcha_label_image.pack()
captcha_entry.pack()
iniciar_sesion_button.pack()
registrar_button.pack()
resultado_label.pack()


generar_captcha()


ventana.mainloop()
