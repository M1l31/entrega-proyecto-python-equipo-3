import time
import sys

class Alumnos:
    def __init__(self, nombre: str, apellido: str, num_lista=int):
        self.nombre = nombre
        self.apellido = apellido
        self.amonestaciones = []
        self.observaciones = []
        self.sanciones = []

    def leer_historial(self):
        print("Historial de", self.nombre, self.apellido)
        print("Amonestaciones:", self.amonestaciones)
        print("Observaciones:", self.observaciones)
        print("Sanciones:", self.sanciones)
        print("")

    def guardar_historial(self):
        with open("historial.txt", "a") as archivo:
            archivo.write(f"Alumno: {self.nombre} {self.apellido}\n")
            archivo.write(f"Cantidad de Amonestaciones: {len(self.amonestaciones)}\n")
            archivo.write(f"Cantidad de Observaciones: {len(self.observaciones)}\n")
            archivo.write(f"Cantidad de Sanciones: {len(self.sanciones)}\n")
            archivo.write("Amonestaciones:\n")
            for amonestacion in self.amonestaciones:
                archivo.write(f"- {amonestacion}\n")
            archivo.write("Observaciones:\n")
            for observacion in self.observaciones:
                archivo.write(f"- {observacion}\n")
            archivo.write("Sanciones:\n")
            for sancion in self.sanciones:
                archivo.write(f"- Tiempo: {sancion[0]} horas, Razón: {sancion[1]}\n")
            archivo.write("\n")

    def cargar_historial(self):
        with open("historial.txt", "r") as archivo:
            lineas = archivo.readlines()
            for i, linea in enumerate(lineas):
                if linea.strip() == f"Alumno: {self.nombre} {self.apellido}":
                    cantidad_amonestaciones = int(lineas[i + 1].split(":")[1])
                    cantidad_observaciones = int(lineas[i + 2].split(":")[1])
                    cantidad_sanciones = int(lineas[i + 3].split(":")[1])

                    amonestaciones = []
                    observaciones = []
                    sanciones = []

                    for j in range(i + 5, i + 5 + cantidad_amonestaciones):
                        amonestacion = lineas[j].strip().split("-")[1].strip()
                        amonestaciones.append(amonestacion)

                    for j in range(i + 6 + cantidad_amonestaciones, i + 6 + cantidad_amonestaciones + cantidad_observaciones):
                        observacion = lineas[j].strip().split("-")[1].strip()
                        observaciones.append(observacion)

                    for j in range(i + 7 + cantidad_amonestaciones + cantidad_observaciones, i + 7 + cantidad_amonestaciones + cantidad_observaciones + cantidad_sanciones):
                        sancion = lineas[j].strip().split(", ")
                        tiempo = sancion[0].split(":")[1].strip()
                        razon = sancion[1].split(":")[1].strip()
                        sanciones.append((tiempo, razon))

                    self.amonestaciones = amonestaciones
                    self.observaciones = observaciones
                    self.sanciones = sanciones
                    break

def buscar_alumno(nombre, apellido):
    with open("alumnos.txt", "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(" ")
            if datos[0] == nombre and datos[1] == apellido:
                return True
    return False

while True:
    print("--------------------------------")
    print("✅- Agregar Amonestacion = 1")
    print("--------------------------------")
    print("✅- Agregar Observacion = 2")
    print("--------------------------------")
    print("✅- Agregar Sanciones = 3")
    print("--------------------------------")
    print("✅- Leer Historial = 4")
    print("--------------------------------")
    print("✅- Salir = 5")
    print("--------------------------------")
    opcion = input("‼📌- Ingrese la Opcion‼ = ")

    if opcion in ["1", "2", "3"]:
        nombre = input("📌- Ingrese el nombre del alumno: ")
        apellido = input("📌- Ingrese el apellido del alumno: ")
        if buscar_alumno(nombre, apellido):
            alumno = Alumnos(nombre, apellido)
        else:
            print("❌ El alumno no está registrado.")
            continue

    if opcion == "1":
        amonestaciones = input("📌- Ingrese la cantidad de amonestaciones: ")
        while True:
            confirmacion = input(f"🌐- Confirmar la cantidad de {amonestaciones} amonestación/es (SI-NO): ")
            if confirmacion == "SI":
                motivo = input("📌- Razón de la amonestación/es: ")
                alumno.amonestaciones.append(motivo)
                break

    if opcion == "2":
        observaciones = input("📌- Ingrese la cantidad de observaciones: ")
        while True:
            confirmacion = input(f"🌐- Confirmar la cantidad de {observaciones} observación/es (SI-NO): ")
            if confirmacion == "SI":
                motivo = input("📌- Razón de la observación/es: ")
                alumno.observaciones.append(motivo)
                break

    if opcion == "3":
        sanciones = input("📌- Ingrese la cantidad de sanciones: ")
        while True:
            confirmacion = input(f"🌐- Confirmar la cantidad de {sanciones} sanción/es (SI-NO): ")
            if confirmacion == "SI":
                tiempo = input("📌- Tiempo de la sanción en horas: ")
                while True:
                    confirmacion = input(f"🌐- Confirmar {tiempo} horas de sanción (SI-NO): ")
                    if confirmacion == "SI":
                        motivo = input("📌- Razón de la sanción: ")
                        alumno.sanciones.append((tiempo, motivo))
                        break

    if opcion == "4":
        alumno.cargar_historial()
        alumno.leer_historial()
        time.sleep(3)

    if opcion == "5":
        alumno.guardar_historial()
        sys.exit("✅- Cerrando Programa")
