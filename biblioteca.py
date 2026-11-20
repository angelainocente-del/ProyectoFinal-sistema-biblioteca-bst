'''
Sistema Simple de Biblioteca con Árbol Binario de Búsqueda (BST)
Curso: Estructura de Datos y Algoritmos
Grupo 3: Susana Garcia - Angela Inocente

El árbol se ordena por el código único de cada libro.
Todo está implementado desde cero (sin librerías externas).
'''


class Libro:
    '''
    Libro definition
    Guarda los datos de un libro. El campo 'codigo' es la clave del árbol.
    '''
    def __init__(self, codigo, titulo, autor, anio, cantidad):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.cantidad = cantidad

    def __str__(self):
        # Devuelve el libro como texto para mostrarlo en pantalla
        return (f"Código: {self.codigo} | Título: {self.titulo} | "
                f"Autor: {self.autor} | Año: {self.anio} | "
                f"Disponibles: {self.cantidad}")


class BSTNode:
    '''
    Node BST definition
    '''
    def __init__(self, data):
        self.left = None     # subárbol izquierdo: códigos menores
        self.right = None    # subárbol derecho: códigos mayores
        self.data = data     # objeto Libro


def insertNode(root, node):
    '''
    Insert a node in BST. Recursive mode.
    :param root: current node (BSTNode or None)
    :param node: BSTNode to insert
    :return: root of the updated subtree
    '''
    # Si llegamos a un lugar vacío, aquí se coloca el nodo nuevo
    if root is None:
        return node

    # Menor código -> izquierda; mayor código -> derecha
    if root.data.codigo > node.data.codigo:
        root.left = insertNode(root.left, node)
    elif root.data.codigo < node.data.codigo:
        root.right = insertNode(root.right, node)
    # Si los códigos son iguales no se insertan duplicados

    return root


def find(root, codigo):
    '''
    Method to find a book by codigo in BST. Recursive mode.
    :param root: current node
    :param codigo: codigo to search
    :return: BSTNode found or None
    '''
    currentNode = root
    # Caso base: llegamos al final y no estaba
    if currentNode == None:
        return None
    else:
        # Caso base: lo encontramos
        if codigo == currentNode.data.codigo:
            return currentNode
        # Descartamos la mitad del árbol en cada paso
        if codigo < currentNode.data.codigo:
            return find(currentNode.left, codigo)
        else:
            return find(currentNode.right, codigo)


def findMin(root):
    '''
    Find the minimum value node. Used internally by delete.
    :param root: current node
    :return: node with minimum value
    '''
    # El menor siempre está en el nodo más a la izquierda
    currentNode = root
    while currentNode.left is not None:
        currentNode = currentNode.left
    return currentNode


def delete(root, codigo):
    '''
    Delete a book by codigo in BST. Recursive mode.
    :param root: current node
    :param codigo: codigo to delete
    :return: root of the updated subtree
    '''
    # Caso base: el código no existe
    if root is None:
        return None

    # Primero se busca el nodo a eliminar
    if codigo < root.data.codigo:
        root.left = delete(root.left, codigo)
    elif codigo > root.data.codigo:
        root.right = delete(root.right, codigo)
    else:
        # Caso 1 (hoja) y Caso 2 (un hijo): sin hijo izquierdo o sin hijo derecho
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        # Caso 3: dos hijos -> sucesor in-order (mínimo del lado derecho)
        successor = findMin(root.right)
        root.data = successor.data
        root.right = delete(root.right, successor.data.codigo)

    return root


def inOrderTraversal(root):
    '''
    Print books In Order Traversal (ordenados por código)
    :param root: current node
    :return:
    '''
    if not root:
        return
    inOrderTraversal(root.left)      # 1. izquierda
    print(root.data)                 # 2. nodo
    inOrderTraversal(root.right)     # 3. derecha


def inOrderList(root, result=None):
    '''
    Same In Order Traversal, but returns a list of books
    :param root: current node
    :param result: list where books are stored
    :return: list of Libro ordered by codigo
    '''
    if result is None:
        result = []
    if not root:
        return result
    inOrderList(root.left, result)
    result.append(root.data)
    inOrderList(root.right, result)
    return result


def findByAuthor(root, autor):
    '''
    Find all books of an author.
    El árbol está ordenado por código, no por autor, por eso se revisa
    todo el árbol (recorrido in-order) y se filtran los libros del autor.
    :param root: current node
    :param autor: author name
    :return: list of Libro
    '''
    result = []
    for libro in inOrderList(root):
        if libro.autor.lower() == autor.lower():
            result.append(libro)
    return result


def countBooks(root):
    '''
    Count total books (nodes) in BST. Recursive mode.
    :param root: current node
    :return: number of nodes
    '''
    # Total = 1 (nodo actual) + nodos de la izquierda + nodos de la derecha
    if root is None:
        return 0
    return 1 + countBooks(root.left) + countBooks(root.right)


# ---------------------------- MENÚ INTERACTIVO ----------------------------

def readInt(message):
    '''
    Ask for an integer until the user types a valid one.
    :param message: text to show
    :return: integer typed by the user
    '''
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Ingrese un número entero válido.")


def menu():
    '''
    Interactive menu. Keeps the root of the BST and calls the functions.
    '''
    root = None

    while True:
        print("\n===== SISTEMA DE BIBLIOTECA =====")
        print("1. Agregar libro")
        print("2. Buscar libro por código")
        print("3. Eliminar libro por código")
        print("4. Mostrar todos los libros (inorder)")
        print("5. Buscar libros por autor")
        print("6. Contar total de libros")
        print("7. Salir")
        option = input("Elija una opción: ")

        if option == "1":
            codigo = readInt("Código: ")
            # El código debe ser único
            if find(root, codigo) is not None:
                print("Error: ya existe un libro con ese código.")
            else:
                titulo = input("Título: ")
                autor = input("Autor: ")
                anio = readInt("Año: ")
                cantidad = readInt("Cantidad disponible: ")
                libro = Libro(codigo, titulo, autor, anio, cantidad)
                root = insertNode(root, BSTNode(libro))
                print("Libro agregado correctamente.")

        elif option == "2":
            node = find(root, readInt("Código a buscar: "))
            if node is None:
                print("Libro no encontrado.")
            else:
                print(node.data)

        elif option == "3":
            codigo = readInt("Código a eliminar: ")
            if find(root, codigo) is None:
                print("Libro no encontrado.")
            else:
                root = delete(root, codigo)
                print("Libro eliminado.")

        elif option == "4":
            if root is None:
                print("No hay libros registrados.")
            else:
                inOrderTraversal(root)

        elif option == "5":
            books = findByAuthor(root, input("Autor: "))
            if not books:
                print("No se encontraron libros de ese autor.")
            for libro in books:
                print(libro)

        elif option == "6":
            print(f"Total de libros: {countBooks(root)}")

        elif option == "7":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida.")


# ---------------------------- BLOQUE DE PRUEBAS ----------------------------

def runTests():
    '''
    Pruebas automáticas con assert. Si algo falla, el programa avisa.
    '''
    print("=== EJECUTANDO PRUEBAS ===")
    root = None

    # Prueba 1: agregar libros (el 50 queda como raíz)
    datos = [(50, "Libro A", "Autor 1"), (30, "Libro B", "Autor 2"),
             (70, "Libro C", "Autor 1"), (20, "Libro D", "Autor 3"),
             (40, "Libro E", "Autor 2"), (60, "Libro F", "Autor 4"),
             (80, "Libro G", "Autor 1")]
    for codigo, titulo, autor in datos:
        root = insertNode(root, BSTNode(Libro(codigo, titulo, autor, 2000, 5)))
    print("OK: agregar libros")

    # Prueba 2: contar
    assert countBooks(root) == 7
    print("OK: contar total = 7")

    # Prueba 3: inorder devuelve los códigos ordenados
    assert [l.codigo for l in inOrderList(root)] == [20, 30, 40, 50, 60, 70, 80]
    print("OK: recorrido inorder ordenado")

    # Prueba 4: buscar por código
    assert find(root, 40).data.titulo == "Libro E"
    assert find(root, 99) is None
    print("OK: buscar por código")

    # Prueba 5: buscar por autor (sin distinguir mayúsculas)
    assert len(findByAuthor(root, "autor 1")) == 3
    assert findByAuthor(root, "Nadie") == []
    print("OK: buscar por autor")

    # Prueba 6: eliminar nodo hoja (20)
    root = delete(root, 20)
    assert find(root, 20) is None
    assert countBooks(root) == 6
    print("OK: eliminar hoja")

    # Prueba 7: eliminar nodo con un hijo (30 solo tiene al 40)
    root = delete(root, 30)
    assert [l.codigo for l in inOrderList(root)] == [40, 50, 60, 70, 80]
    print("OK: eliminar nodo con un hijo")

    # Prueba 8: eliminar nodo con dos hijos (la raíz 50)
    root = delete(root, 50)
    assert [l.codigo for l in inOrderList(root)] == [40, 60, 70, 80]
    assert countBooks(root) == 4
    print("OK: eliminar nodo con dos hijos")

    # Prueba 9: eliminar un código que no existe no cambia el árbol
    root = delete(root, 999)
    assert countBooks(root) == 4
    print("OK: eliminar código inexistente")

    print("=== TODAS LAS PRUEBAS PASARON ===")


if __name__ == "__main__":
    runTests()   # primero corre las pruebas
    menu()       # luego inicia el menú interactivo