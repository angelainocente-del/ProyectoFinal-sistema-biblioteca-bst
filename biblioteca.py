# ============================================================
# PROYECTO: SISTEMA SIMPLE DE BIBLIOTECA
# ARCHIVO: biblioteca.py
# ============================================================
#
# Este archivo contiene el menu principal del programa.
#
# Se conecta con:
# - estructuras.py: clases y BST.
# - operaciones.py: funciones de gestion de libros.
# ============================================================

from estructuras import ArbolBinarioBusqueda
from operaciones import (
    registrar_libro,
    consultar_libro,
    eliminar_libro,
    mostrar_libros,
    consultar_autor,
    contar_libros,
    cargar_libros_ejemplo
)


# ============================================================
# PRUEBAS AUTOMATICAS
# ============================================================

def pruebas_automaticas():
    """
    Ejecuta pruebas de las operaciones principales del BST.

    Se utiliza un arbol independiente para no modificar
    los libros que el usuario haya registrado en el menu.
    """

    print("\n====================================")
    print("       PRUEBAS AUTOMATICAS")
    print("====================================")

    # Creamos un arbol exclusivo para las pruebas.
    arbol_prueba = ArbolBinarioBusqueda()

    # Insertamos libros de prueba.
    cargar_libros_ejemplo(arbol_prueba)

    # --------------------------------------------------------
    # PRUEBA 1: CONTAR
    # --------------------------------------------------------

    print("\nPrueba 1: Contar libros")

    assert arbol_prueba.contar_libros() == 7
    print("CORRECTO: se registraron 7 libros.")

    # --------------------------------------------------------
    # PRUEBA 2: BUSCAR LIBRO EXISTENTE
    # --------------------------------------------------------

    print("\nPrueba 2: Buscar codigo 40")

    libro = arbol_prueba.buscar(40)

    assert libro is not None
    assert libro.codigo == 40

    print("CORRECTO: libro con codigo 40 encontrado.")

    # --------------------------------------------------------
    # PRUEBA 3: BUSCAR LIBRO INEXISTENTE
    # --------------------------------------------------------

    print("\nPrueba 3: Buscar codigo 999")

    libro = arbol_prueba.buscar(999)

    assert libro is None

    print("CORRECTO: codigo inexistente.")

    # --------------------------------------------------------
    # PRUEBA 4: RECORRIDO INORDER
    # --------------------------------------------------------

    print("\nPrueba 4: Recorrido Inorder")

    libros_ordenados = arbol_prueba.inorder()

    codigos = [libro.codigo for libro in libros_ordenados]

    assert codigos == [20, 30, 40, 50, 60, 70, 80]

    print("CORRECTO: libros ordenados:")
    print(codigos)

    # --------------------------------------------------------
    # PRUEBA 5: BUSCAR POR AUTOR
    # --------------------------------------------------------

    print("\nPrueba 5: Buscar autor Gabriel Garcia Marquez")

    libros_autor = arbol_prueba.buscar_por_autor(
        "Gabriel Garcia Marquez"
    )

    assert len(libros_autor) == 2

    print("CORRECTO: se encontraron 2 libros del autor.")

    # --------------------------------------------------------
    # PRUEBA 6: ELIMINAR
    # --------------------------------------------------------

    print("\nPrueba 6: Eliminar codigo 30")

    resultado = arbol_prueba.eliminar(30)

    assert resultado is True
    assert arbol_prueba.buscar(30) is None
    assert arbol_prueba.contar_libros() == 6

    print("CORRECTO: codigo 30 eliminado.")
    print("El arbol conserva 6 libros.")

    # --------------------------------------------------------
    # PRUEBA 7: CODIGO DUPLICADO
    # --------------------------------------------------------

    print("\nPrueba 7: Insertar codigo duplicado 50")

    libro_raiz = arbol_prueba.buscar(50)

    resultado = arbol_prueba.insertar(libro_raiz)

    assert resultado is False
    assert arbol_prueba.contar_libros() == 6

    print("CORRECTO: no se permiten codigos duplicados.")

    # --------------------------------------------------------
    # RESULTADO FINAL
    # --------------------------------------------------------

    print("\n====================================")
    print("TODAS LAS PRUEBAS FUERON SUPERADAS")
    print("====================================")


# ============================================================
# MENU PRINCIPAL
# ============================================================

def menu():
    """
    Controla las opciones del sistema de biblioteca.
    """

    # Creamos el arbol que almacenara los libros del usuario.
    biblioteca = ArbolBinarioBusqueda()

    while True:

        print("\n" + "=" * 45)
        print("       SISTEMA SIMPLE DE BIBLIOTECA")
        print("       ARBOL BINARIO DE BUSQUEDA")
        print("=" * 45)

        print("1. Agregar libro")
        print("2. Buscar libro por codigo")
        print("3. Eliminar libro por codigo")
        print("4. Mostrar libros ordenados por codigo")
        print("5. Buscar libros por autor")
        print("6. Contar libros registrados")
        print("7. Cargar libros de ejemplo")
        print("8. Ejecutar pruebas automaticas")
        print("9. Salir")

        opcion = input("\nSeleccione una opcion: ").strip()

        # Opcion 1: registrar libro.
        if opcion == "1":
            registrar_libro(biblioteca)

        # Opcion 2: buscar por codigo.
        elif opcion == "2":
            consultar_libro(biblioteca)

        # Opcion 3: eliminar libro.
        elif opcion == "3":
            eliminar_libro(biblioteca)

        # Opcion 4: mostrar libros ordenados.
        elif opcion == "4":
            mostrar_libros(biblioteca)

        # Opcion 5: buscar por autor.
        elif opcion == "5":
            consultar_autor(biblioteca)

        # Opcion 6: contar registros.
        elif opcion == "6":
            contar_libros(biblioteca)

        # Opcion 7: insertar datos de demostracion.
        elif opcion == "7":
            cargar_libros_ejemplo(biblioteca)

        # Opcion 8: ejecutar las pruebas.
        elif opcion == "8":
            pruebas_automaticas()

        # Opcion 9: finalizar programa.
        elif opcion == "9":
            print("\nGracias por utilizar el sistema.")
            print("Programa finalizado.")
            break

        # Si se ingresa otra opcion.
        else:
            print("Opcion invalida. Intente nuevamente.")


# ============================================================
# INICIO DEL PROGRAMA
# ============================================================

# Esta condicion evita que el menu se ejecute si este archivo
# se importa desde otro archivo Python.

if __name__ == "__main__":
    menu()
