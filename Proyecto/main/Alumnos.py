def guardar_alumno(nombre, apellido):
    with open('alumnos.txt', 'a') as archivo:
        archivo.write(f'{nombre} {apellido}\n')
    print('Alumno guardado correctamente.')


while True:
    nombre = input('📌- Ingrese el nombre del alumno (o "salir" para terminar): ')
    if nombre.lower() == 'salir':
        break

    apellido = input('📌- Ingrese el apellido del alumno: ')
    guardar_alumno(nombre, apellido)

print('🌐- Proceso terminado. Los alumnos han sido guardados en "alumnos.txt".')
