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
    # Esta función solo se encarga de mostrar por consola las opciones del sistema
    # No recibe parámetros ni devuelve nada, solo imprime texto
    print("\n=======================================")
    print("  SISTEMA DE INSCRIPCIÓN A CURSOS - UTN")
    print("=======================================")
    print("1. Registrar Estudiante")
    print("2. Mostrar Estudiantes Registrados")
    print("3. Mostrar Cursos y Cupos")
    print("4. Inscribir Estudiante a un Curso")
    print("5. Mostrar Lista de Espera")
    print("6. Mostrar Estadísticas del Sistema")
    print("7. Salir")


def mostrar_cursos():
    # Esta función recorre la lista global 'cursos' y muestra el estado de cada uno

    # VALIDACIÓN: si la lista de cursos está vacía, avisamos y cortamos la función con 'return'
    if not cursos:
        print("\nNo hay cursos cargados.")
        return

    print("\n--- ESTADO DE LOS CURSOS ---")

    # BUCLE: usamos 'enumerate' para obtener el índice (i) junto con los datos de cada curso
    for i, curso in enumerate(cursos):
        nombre = curso[0]          # Posición 0 de la lista: nombre del curso
        cupo_max = curso[1]        # Posición 1 de la lista: cupo máximo permitido
        cant_inscriptos = len(curso[2])  # Posición 2: lista de DNIs inscriptos; contamos cuántos hay con len()

        # CÁLCULO: cupos disponibles = cupo máximo menos los que ya están inscriptos
        disponibles = cupo_max - cant_inscriptos

        # CONDICIONAL: si no quedan cupos disponibles (0 o menos), mostramos un aviso especial
        if disponibles <= 0:
            estado = "¡SIN CUPO!"
        else:
            estado = f"{disponibles} disponibles"

        # IMPRESIÓN: mostramos toda la información del curso en una sola línea, bien formateada
        # i + 1 es para que el usuario vea "Curso 1, 2, 3..." en vez de empezar desde 0
        print(f"[{i + 1}] {nombre} | Cupo Máx: {cupo_max} | Inscriptos: {cant_inscriptos} | {estado}")


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