# Trabajo Final Integrador - Python
# Escenario 13: Sistema de inscripción a cursos

estudiantes = []
cursos = [
    ["Python Inicial", 3, []],
    ["Excel Básico", 2, []],
    ["Diseño Web", 2, []],
]
lista_espera = []


# Carlos Aramberry
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


# Tomás Garcilazo
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


# Carlos González
def inscribir_estudiante():
    # Validar que existan estudiantes registrados antes de continuar
    if not estudiantes:
        print("\nNo hay estudiantes registrados en el sistema.")
        return

    # 1: Mostrar estudiantes y elegir uno
    print("\n--- Estudiantes Registrados ---")
    for i, estudiante in enumerate(estudiantes):
        # Asumiendo que el estudiante se guardó como una lista [nombre, dni] o un string
        print(f"{i + 1}. {estudiante[0]} - DNI: {estudiante[1]}")
    
    try:
        opcion_est = int(input("Elija el número del estudiante a inscribir: ")) - 1
        if opcion_est < 0 or opcion_est >= len(estudiantes):
            print("Número de estudiante inválido.")
            return
        estudiante_elegido = estudiantes[opcion_est]
    except ValueError:
        print("Error: Debe ingresar un número válido.")
        return

    # 2: Mostrar cursos y elegir uno
    print("\n--- Cursos Disponibles ---")
    for i, curso in enumerate(cursos):
        nombre_curso = curso[0]
        cupo_maximo = curso[1]
        inscriptos_actuales = len(curso[2])
        print(f"{i + 1}. {nombre_curso} (Inscriptos: {inscriptos_actuales}/{cupo_maximo})")

    try:
        opcion_curso = int(input("Elija el número del curso: ")) - 1
        if opcion_curso < 0 or opcion_curso >= len(cursos):
            print("Número de curso inválido.")
            return
        curso_elegido = cursos[opcion_curso]
    except ValueError:
        print("Error: Debe ingresar un número válido.")
        return

    # 3: Lógica de inscripción y control de cupos
    nombre_curso = curso_elegido[0]
    cupo_maximo = curso_elegido[1]
    lista_inscriptos = curso_elegido[2]

    # Validar si el estudiante ya está inscripto para evitar duplicados
    if estudiante_elegido in lista_inscriptos:
        print(f"\nEl estudiante ya se encuentra inscripto en {nombre_curso}.")
        return

    # Si hay cupo, inscribir (agregar a la sublista de inscriptos del curso)
    if len(lista_inscriptos) < cupo_maximo:
        lista_inscriptos.append(estudiante_elegido)
        print(f"\n¡Éxito! Estudiante inscripto correctamente en '{nombre_curso}'.")
    else:
        # Si no hay cupo, agregar a lista de espera
        # Estructura: [estudiante, nombre_del_curso]
        lista_espera.append([estudiante_elegido, nombre_curso])
        print(f"\nEl curso '{nombre_curso}' no tiene cupos disponibles.")
        print("El estudiante fue agregado a la lista de espera.")


def mostrar_lista_espera():
    print("\n--- Lista de Espera ---")
    
    if not lista_espera:
        print("Actualmente no hay nadie en la lista de espera.")
        return

    # Mostrar estudiantes iterando sobre la lista de espera
    for i, registro in enumerate(lista_espera):
        estudiante = registro[0]
        curso_deseado = registro[1]
        print(f"{i + 1}. Curso: {curso_deseado} | Estudiante: {estudiante[0]} - DNI: {estudiante[1]}")


# Martin Alarcon
def mostrar_estadisticas():
    # 1. Total de estudiantes registrados en el sistema
    total_estudiantes = len(estudiantes)
    print("\n" + "="*45)
    print("      ESTADÍSTICAS GENERALES DEL SISTEMA")
    print("="*45)
    print(f"Total de estudiantes registrados: {total_estudiantes}")
    print("-"*45)

    # Validar si existen cursos cargados antes de operar
    if not cursos:
        print("No hay cursos registrados para calcular estadísticas.")
        print("="*45)
        return

    # Inicializar variables para encontrar el curso con mayor demanda
    # (Contadores y acumuladores requeridos por la cátedra)
    nombre_mayor_demanda = ""
    max_inscriptos = -1

    print("Inscripciones y cupos por curso:")

    # Recorrer la matriz de cursos
    for curso in cursos:
        nombre_curso = curso[0]
        cupo_maximo = curso[1]
        cantidad_inscriptos = len(curso[2]) # Longitud de la lista de alumnos inscritos

        # Calcular los cupos restantes
        cupos_restantes = cupo_maximo - cantidad_inscriptos

        print(f" * Curso: {nombre_curso}")
        print(f"   - Inscriptos: {cantidad_inscriptos}")
        print(f"   - Cupos restantes: {cupos_restantes}")
        print("-"*45)

        # Lógica para determinar el curso con mayor demanda
        if cantidad_inscriptos > max_inscriptos:
            max_inscriptos = cantidad_inscriptos
            nombre_mayor_demanda = nombre_curso

    # Mostrar el curso con mayor demanda basándose en los resultados
    if max_inscriptos > 0:
        print(f"Curso con mayor demanda: {nombre_mayor_demanda} ({max_inscriptos} inscriptos)")
    else:
        print("Curso con mayor demanda: Aún no hay estudiantes inscritos en ningún curso.")

    print("="*45)


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
        print("\n=======================================")
        print("Gracias por utilizar el sistema.")
        print("Hasta luego.")
        print("=======================================")

    else:
        print("Opción inválida.")