# Trabajo Final Integrador - Python
# Escenario 13: Sistema de inscripción a cursos

estudiantes = []
cursos = [
    ["Python Inicial", 3, []],
    ["Excel Básico", 2, []],
    ["Diseño Web", 2, []],
]
lista_espera = []


# =========================
# PERSONA 1
# =========================

def menu():
    # Mostrar las opciones del sistema
    pass


def mostrar_cursos():
    # Mostrar cursos, cupos totales, inscriptos y cupos disponibles
    pass


# =========================
# PERSONA 2
# =========================

def registrar_estudiante():
    # Título de la sección
    print("\n===== REGISTRAR ESTUDIANTE =====")

    # Solicita los datos del estudiante
    nombre = input("Ingrese el nombre: ")
    dni = input("Ingrese el DNI: ")

    # Verifica que los datos no estén vacíos
    if nombre == "" or dni == "":
        print("Error. No puede dejar campos vacíos.")
        return

    # Recorre la lista para verificar que el DNI no exista
    for estudiante in estudiantes:
        if estudiante[1] == dni:
            print("Ese DNI ya está registrado.")
            return

    # Agrega el estudiante a la lista
    estudiantes.append([nombre, dni])

    # Mensaje de confirmación
    print("Estudiante registrado correctamente.")


def mostrar_estudiantes():
    # Título de la sección
    print("\n===== ESTUDIANTES REGISTRADOS =====")

    # Verifica si existen estudiantes registrados
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        # Recorre la lista y muestra todos los estudiantes
        for i in range(len(estudiantes)):
            print(
                i + 1,
                "-",
                estudiantes[i][0],
                "- DNI:",
                estudiantes[i][1]
            )


# =========================
# PERSONA 3
# =========================

def inscribir_estudiante():
    # Mostrar estudiantes
    # Elegir estudiante
    # Mostrar cursos
    # Elegir curso
    # Si hay cupo, inscribir
    # Si no hay cupo, agregar a lista de espera
    pass


def mostrar_lista_espera():
    # Mostrar estudiantes en lista de espera
    pass


# =========================
# PERSONA 4
# =========================

def mostrar_estadisticas():
    # Mostrar total de estudiantes
    # Mostrar inscriptos por curso
    # Mostrar cupos restantes
    # Mostrar curso con mayor demanda
    pass


# =========================
# PROGRAMA PRINCIPAL
# =========================

opcion = 0

while opcion != 7:
    menu()

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Error: debe ingresar un número.")
        continue

    if opcion == 1:
        registrar_estudiante()

    elif opcion == 2:
        mostrar_estudiantes()

    elif opcion == 3:
        mostrar_cursos()

    elif opcion == 4:
        inscribir_estudiante()

    elif opcion == 5:
        mostrar_lista_espera()

    elif opcion == 6:
        mostrar_estadisticas()

    elif opcion == 7:
        print("Fin del programa.")

    else:
        print("Opción inválida.")