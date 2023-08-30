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
