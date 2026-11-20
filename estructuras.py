# ============================================================
# PROYECTO: SISTEMA SIMPLE DE BIBLIOTECA
# ESTRUCTURA: ARBOL BINARIO DE BUSQUEDA (BST)
# ARCHIVO: estructuras.py
# ============================================================

# ============================================================
# CLASE LIBRO
# ============================================================

class Libro:
    """
    Representa un libro de la biblioteca.

    Atributos:
        codigo: identificador unico del libro.
        titulo: nombre del libro.
        autor: autor del libro.
        año: año de publicacion.
        cantidad_disponible: ejemplares disponibles.
    """

    def __init__(self, codigo, titulo, autor, año, cantidad_disponible):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.cantidad_disponible = cantidad_disponible

    def __str__(self):
        """
        Devuelve la informacion del libro en formato legible.
        """
        return (
            f"Codigo: {self.codigo} | "
            f"Titulo: {self.titulo} | "
            f"Autor: {self.autor} | "
            f"Año: {self.año} | "
            f"Disponibles: {self.cantidad_disponible}"
        )


# ============================================================
# CLASE NODO
# ============================================================

class Nodo:
    """
    Representa un nodo dentro del arbol BST.

    Cada nodo contiene:
        libro: objeto Libro almacenado.
        izquierdo: referencia al hijo izquierdo.
        derecho: referencia al hijo derecho.
    """

    def __init__(self, libro):
        self.libro = libro
        self.izquierdo = None
        self.derecho = None


# ============================================================
# CLASE ARBOL BINARIO DE BUSQUEDA
# ============================================================

class ArbolBinarioBusqueda:
    """
    Implementa un Arbol Binario de Busqueda (BST).

    Organizacion:
        - Codigos menores: subarbol izquierdo.
        - Codigos mayores: subarbol derecho.
        - Codigos duplicados: no se permiten.
    """

    def __init__(self):
        # La raiz representa el primer nodo del arbol.
        # Al inicio, el arbol esta vacio.
        self.raiz = None

    # --------------------------------------------------------
    # INSERTAR
    # --------------------------------------------------------

    def insertar(self, libro):
        """
        Inserta un libro en el BST usando su codigo.

        Si el arbol esta vacio, el libro se convierte en raiz.
        Si no, se busca la posicion correcta.

        Retorna True si se inserta.
        Retorna False si el codigo ya existe.
        """

        # Caso 1: el arbol esta vacio.
        if self.raiz is None:
            self.raiz = Nodo(libro)
            return True

        # Caso 2: el arbol ya tiene elementos.
        return self._insertar_recursivo(self.raiz, libro)

    def _insertar_recursivo(self, nodo_actual, libro):
        """
        Compara los codigos y busca la posicion de insercion.

        Este metodo es recursivo porque puede llamarse a si mismo
        para avanzar por los subarboles.
        """

        # Si el codigo es menor, vamos hacia la izquierda.
        if libro.codigo < nodo_actual.libro.codigo:

            # Si el lugar izquierdo esta libre, insertamos.
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(libro)
                return True

            # Si esta ocupado, seguimos buscando a la izquierda.
            return self._insertar_recursivo(
                nodo_actual.izquierdo, libro
            )

        # Si el codigo es mayor, vamos hacia la derecha.
        elif libro.codigo > nodo_actual.libro.codigo:

            # Si el lugar derecho esta libre, insertamos.
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(libro)
                return True

            # Si esta ocupado, seguimos buscando a la derecha.
            return self._insertar_recursivo(
                nodo_actual.derecho, libro
            )

        # Si los codigos son iguales, no insertamos duplicados.
        else:
            return False

    # --------------------------------------------------------
    # BUSCAR
    # --------------------------------------------------------

    def buscar(self, codigo):
        """
        Busca un libro por su codigo.

        Retorna el objeto Libro si lo encuentra.
        Retorna None si no existe.
        """

        return self._buscar_recursivo(self.raiz, codigo)

    def _buscar_recursivo(self, nodo_actual, codigo):
        """
        Busca el codigo comparando con el nodo actual.

        Si es menor, busca a la izquierda.
        Si es mayor, busca a la derecha.
        Si coincide, devuelve el libro.
        """

        # Si llegamos a None, el codigo no existe.
        if nodo_actual is None:
            return None

        # Si el codigo coincide, devolvemos el libro.
        if codigo == nodo_actual.libro.codigo:
            return nodo_actual.libro

        # Si es menor, continuamos por la izquierda.
        elif codigo < nodo_actual.libro.codigo:
            return self._buscar_recursivo(
                nodo_actual.izquierdo, codigo
            )

        # Si es mayor, continuamos por la derecha.
        else:
            return self._buscar_recursivo(
                nodo_actual.derecho, codigo
            )

    # --------------------------------------------------------
    # ELIMINAR
    # --------------------------------------------------------

    def eliminar(self, codigo):
        """
        Elimina un libro del BST segun su codigo.

        Se consideran tres casos:
        1. Nodo sin hijos.
        2. Nodo con un hijo.
        3. Nodo con dos hijos.
        """

        # Verificamos si el libro existe antes de eliminar.
        if self.buscar(codigo) is None:
            return False

        # La raiz tambien puede ser eliminada.
        self.raiz = self._eliminar_recursivo(self.raiz, codigo)
        return True

    def _eliminar_recursivo(self, nodo_actual, codigo):
        """
        Busca el nodo que se debe eliminar y reorganiza el arbol.
        """

        # Si no hay nodo, retornamos None.
        if nodo_actual is None:
            return None

        # Buscamos por el subarbol izquierdo.
        if codigo < nodo_actual.libro.codigo:
            nodo_actual.izquierdo = self._eliminar_recursivo(
                nodo_actual.izquierdo, codigo
            )

        # Buscamos por el subarbol derecho.
        elif codigo > nodo_actual.libro.codigo:
            nodo_actual.derecho = self._eliminar_recursivo(
                nodo_actual.derecho, codigo
            )

        # Encontramos el nodo que contiene el codigo.
        else:

            # CASO 1: el nodo no tiene hijos.
            if (
                nodo_actual.izquierdo is None
                and nodo_actual.derecho is None
            ):
                return None

            # CASO 2: solamente tiene hijo derecho.
            elif nodo_actual.izquierdo is None:
                return nodo_actual.derecho

            # CASO 2: solamente tiene hijo izquierdo.
            elif nodo_actual.derecho is None:
                return nodo_actual.izquierdo

            # CASO 3: tiene dos hijos.
            else:
                # Encontramos el sucesor inorden:
                # el menor nodo del subarbol derecho.
                sucesor = self._buscar_minimo(nodo_actual.derecho)

                # Copiamos el libro del sucesor al nodo actual.
                nodo_actual.libro = sucesor.libro

                # Eliminamos el sucesor de su ubicacion anterior.
                nodo_actual.derecho = self._eliminar_recursivo(
                    nodo_actual.derecho,
                    sucesor.libro.codigo
                )

        # Devolvemos el nodo actualizado.
        return nodo_actual

    def _buscar_minimo(self, nodo):
        """
        Encuentra el nodo con el menor codigo de un subarbol.

        En un BST, el menor valor se encuentra avanzando
        continuamente hacia la izquierda.
        """

        actual = nodo

        while actual.izquierdo is not None:
            actual = actual.izquierdo

        return actual

    # --------------------------------------------------------
    # RECORRIDO INORDER
    # --------------------------------------------------------

    def inorder(self):
        """
        Retorna una lista de libros ordenados por codigo.

        El recorrido visita:
            1. Subarbol izquierdo.
            2. Nodo actual.
            3. Subarbol derecho.
        """

        libros = []

        self._inorder_recursivo(self.raiz, libros)

        return libros

    def _inorder_recursivo(self, nodo_actual, libros):
        """
        Recorre el arbol Inorder de forma recursiva.
        """

        # Caso base: no existe nodo.
        if nodo_actual is None:
            return

        # Paso 1: recorrer el lado izquierdo.
        self._inorder_recursivo(nodo_actual.izquierdo, libros)

        # Paso 2: guardar el libro del nodo actual.
        libros.append(nodo_actual.libro)

        # Paso 3: recorrer el lado derecho.
        self._inorder_recursivo(nodo_actual.derecho, libros)

    # --------------------------------------------------------
    # BUSCAR POR AUTOR
    # --------------------------------------------------------

    def buscar_por_autor(self, autor):
        """
        Retorna todos los libros que coinciden con un autor.

        Como el BST esta ordenado por codigo y no por autor,
        debemos recorrer todos los nodos.
        """

        encontrados = []

        self._buscar_autor_recursivo(self.raiz, autor, encontrados)

        return encontrados

    def _buscar_autor_recursivo(self, nodo_actual, autor, encontrados):
        """
        Revisa el autor de cada nodo del arbol.
        """

        # Si el nodo no existe, terminamos esta rama.
        if nodo_actual is None:
            return

        # Comparamos los autores ignorando mayusculas.
        if nodo_actual.libro.autor.lower() == autor.lower():
            encontrados.append(nodo_actual.libro)

        # Revisamos el subarbol izquierdo.
        self._buscar_autor_recursivo(
            nodo_actual.izquierdo, autor, encontrados
        )

        # Revisamos el subarbol derecho.
        self._buscar_autor_recursivo(
            nodo_actual.derecho, autor, encontrados
        )

    # --------------------------------------------------------
    # CONTAR LIBROS
    # --------------------------------------------------------

    def contar_libros(self):
        """
        Retorna el total de libros registrados (nodos).

        No suma los ejemplares disponibles.
        Cuenta cuantos registros Libro hay en el BST.
        """

        return self._contar_recursivo(self.raiz)

    def _contar_recursivo(self, nodo_actual):
        """
        Cuenta los nodos del subarbol recursivamente.
        """

        # Un nodo inexistente aporta cero.
        if nodo_actual is None:
            return 0

        # Sumamos:
        # 1 por el nodo actual,
        # la cantidad del lado izquierdo,
        # la cantidad del lado derecho.
        return (
            1
            + self._contar_recursivo(nodo_actual.izquierdo)
            + self._contar_recursivo(nodo_actual.derecho)
        )
