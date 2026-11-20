
# ============================================================
# PROYECTO: SISTEMA SIMPLE DE BIBLIOTECA
# ARCHIVO: operaciones.py
# ============================================================
#
# Este archivo contiene las funciones que permiten al usuario
# interactuar con el Arbol Binario de Busqueda (BST).
#
# Las clases Libro y ArbolBinarioBusqueda se importan desde
# estructuras.py.
# ============================================================

from estructuras import Libro

# ============================================================
# FUNCION AUXILIAR: LEER NUMEROS ENTEROS
# ============================================================

def leer_entero(mensaje):
    """
    Solicita un numero entero al usuario.

    Si el usuario ingresa texto u otro valor incorrecto,
    se vuelve a solicitar el dato.
    """

    while True:
        try:
            valor = int(input(mensaje))
            return valor

        except ValueError:
            print("Error: debe ingresar un numero entero.")


# ============================================================
# 1. REGISTRAR LIBRO
# ============================================================

def registrar_libro(arbol):
    """
    Solicita los datos de un libro y lo agrega al BST.

    Antes de insertarlo, verifica que el codigo no exista.
    """

    print("\n========== REGISTRAR LIBRO ==========")

    codigo = leer_entero("Ingrese el codigo del libro: ")

    # Verificamos que no exista otro libro con el mismo codigo.
    if arbol.buscar(codigo) is not None:
        print("Error: ya existe un libro con ese codigo.")
        return

    # Solicitamos los datos restantes del libro.
    titulo = input("Ingrese el titulo: ").strip()
    autor = input("Ingrese el autor: ").strip()
    año = leer_entero("Ingrese el año de publicacion: ")
    cantidad = leer_entero("Ingrese la cantidad disponible: ")

    # Validamos que titulo y autor tengan contenido.
    if not titulo or not autor:
        print("Error: el titulo y el autor son obligatorios.")
        return

    # Validamos el año.
    if año <= 0:
        print("Error: el año debe ser mayor que cero.")
        return

    # Validamos la cantidad de ejemplares.
    if cantidad < 0:
        print("Error: la cantidad no puede ser negativa.")
        return

    # Creamos el objeto Libro con los datos ingresados.
    nuevo_libro = Libro(codigo, titulo, autor, año, cantidad)

    # Insertamos el libro en el arbol.
    if arbol.insertar(nuevo_libro):
        print("Libro registrado correctamente.")
    else:
        print("No se pudo registrar el libro.")


# ============================================================
# 2. BUSCAR LIBRO POR CODIGO
# ============================================================

def consultar_libro(arbol):
    """
    Busca un libro por codigo y muestra su informacion.
    """

    print("\n========== BUSCAR LIBRO ==========")

    codigo = leer_entero("Ingrese el codigo del libro: ")

    # Utilizamos el metodo buscar del BST.
    libro = arbol.buscar(codigo)

    # Evaluamos si el libro fue encontrado.
    if libro is None:
        print("No se encontro un libro con ese codigo.")
    else:
        print("\nLibro encontrado:")
        print(libro)


# ============================================================
# 3. ELIMINAR LIBRO POR CODIGO
# ============================================================

def eliminar_libro(arbol):
    """
    Solicita el codigo de un libro y lo elimina del BST.
    """

    print("\n========== ELIMINAR LIBRO ==========")

    codigo = leer_entero("Ingrese el codigo del libro: ")

    # Utilizamos el metodo eliminar del BST.
    if arbol.eliminar(codigo):
        print("Libro eliminado correctamente.")
    else:
        print("No se encontro el libro que desea eliminar.")


# ============================================================
# 4. MOSTRAR LIBROS ORDENADOS POR CODIGO
# ============================================================

def mostrar_libros(arbol):
    """
    Muestra todos los libros ordenados por codigo
    mediante el recorrido Inorder.
    """

    print("\n========== LISTA DE LIBROS ==========")

    # Obtenemos la lista ordenada desde el BST.
    libros = arbol.inorder()

    # Verificamos si la biblioteca esta vacia.
    if len(libros) == 0:
        print("No hay libros registrados.")
        return

    # Recorremos la lista y mostramos cada libro.
    for libro in libros:
        print(libro)


# ============================================================
# 5. BUSCAR LIBROS POR AUTOR
# ============================================================

def consultar_autor(arbol):
    """
    Busca y muestra todos los libros de un autor.
    """

    print("\n========== BUSCAR POR AUTOR ==========")

    autor = input("Ingrese el nombre del autor: ").strip()

    # Validamos que el usuario ingrese un autor.
    if autor == "":
        print("Debe ingresar el nombre de un autor.")
        return

    # Ejecutamos la busqueda por autor.
    libros = arbol.buscar_por_autor(autor)

    # Si la lista esta vacia, no hubo coincidencias.
    if len(libros) == 0:
        print(f"No se encontraron libros de {autor}.")
        return

    # Mostramos los libros encontrados.
    print(f"\nLibros encontrados de {autor}:")

    for libro in libros:
        print(libro)


# ============================================================
# 6. CONTAR LIBROS REGISTRADOS
# ============================================================

def contar_libros(arbol):
    """
    Muestra el total de libros registrados en el BST.

    Cuenta registros de libros, no la suma de ejemplares.
    """

    print("\n========== CONTAR LIBROS ==========")

    total = arbol.contar_libros()

    print(f"Total de libros registrados: {total}")


# ============================================================
# 7. CARGAR LIBROS DE EJEMPLO
# ============================================================

def cargar_libros_ejemplo(arbol):
    """
    Inserta libros de ejemplo para facilitar las pruebas
    y demostraciones del sistema.

    Los codigos se eligieron para formar un BST con
    nodos a la izquierda y a la derecha de la raiz.
    """

    libros_ejemplo = [
        Libro(50, "El principito", "Antoine de Saint-Exupery", 1943, 5),
        Libro(30, "Don Quijote", "Miguel de Cervantes", 1605, 3),
        Libro(70, "Cien anos de soledad", "Gabriel Garcia Marquez", 1967, 4),
        Libro(20, "La ciudad y los perros", "Mario Vargas Llosa", 1963, 2),
        Libro(40, "Hamlet", "William Shakespeare", 1603, 6),
        Libro(60, "El amor en los tiempos del colera", "Gabriel Garcia Marquez", 1985, 2),
        Libro(80, "Maria", "Jorge Isaacs", 1867, 3)
    ]

    agregados = 0

    # Insertamos cada libro utilizando el BST.
    for libro in libros_ejemplo:
        if arbol.insertar(libro):
            agregados += 1

    print(f"Se cargaron {agregados} libros de ejemplo.")
