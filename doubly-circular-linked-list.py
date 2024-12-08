class CircleLinkedList:
    class _Node:
        def __init__(self, value):
            self.value = value
            self.node_before = None
            self.node_next = None
    
    def __init__(self):
        self.head = None
        self.queue = None
        self.size = 0

    def __str__(self):
        array = []
        node_actual = self.head
        pivot = True
        count = self.size
        while count != 0:
            if pivot != False or node_actual != self.head:
                array.append(node_actual.value)
                node_actual = node_actual.node_next
                pivot = False
                count -=1 
            else:
                break
        return str(array) + " size: " + str(self.size)
    
    def prepend(self, value):
        nuevo_Node = self._Node(value)
        if self.head == None and self.queue == None:
            self.head = nuevo_nodo
            self.queue = nuevo_nodo
        else:
            self.head.node_before = nuevo_nodo
            nuevo_nodo.node_next = self.head
            self.queue.node_next = nuevo_nodo
            nuevo_nodo.node_before = self.queue
            self.head = nuevo_nodo
        self.size += 1
    def append(self, value):
        # Agrega un elemento al final de la linkedlist
        nuevo_nodo = self._Node(value)
        if self.head == None and self.queue == None:
            self.head = nuevo_nodo
            self.queue = nuevo_nodo
        else:
            self.queue.node_next = nuevo_nodo
            nuevo_nodo.node_before = self.queue
            nuevo_nodo.node_next = self.head 
            self.head.node_before = nuevo_nodo
            self.queue = nuevo_nodo
        self.size += 1
    def shift(self):
        # Saca el primer elemento de la linkedlist
        if self.size == 0:
            self.head = None
            self.queue = None
        else:
            node_eliminado = self.head
            self.head = node_eliminado.node_next
            self.head.node_before = self.queue
            self.queue.node_next = self.head
            node_eliminado.node_before = None
            node_eliminado.node_next = None
            self.size -= 1
            return print(node_eliminado.value)
    def pop(self):
        # Saca el ultimo elemento de la linkedlist
        if self.size == 0:
            self.head = None
            self.queue = None
        else:
            node_eliminado = self.queue
            self.queue = node_eliminado.node_before
            self.queue.node_next = self.head
            self.head.node_before = self.queue
            node_eliminado.node_before = None
            node_eliminado.node_next = None
            self.size -= 1
            return print(node_eliminado.value)
    def get(self, indice):
        # Obtiene un nodo dado un indice
        if indice == self.size - 1:
            print(self.queue.value)
            return self.queue
        elif indice == 0:
            print(self.head.value)
            return self.head
        elif not (indice >= self.size or indice < 0):
            indice_balanceado = int(self.size / 2)
            if indice <= indice_balanceado:
                node_actual = self.head
                count = 0
                while count != indice:
                    node_actual = node_actual.node_next
                    count += 1
                print(node_actual.value)
                return node_actual
            else:
                node_actual = self.queue
                count = self.size - 1
                while count != indice:
                    node_actual = node_actual.node_before
                    count -= 1
                print(node_actual.value)
                return node_actual
        else:
            return None
    def update(self, indice, value):
        # Cambia el value de un nodo dado el indice
        node_objetivo = self.get(indice)
        if node_objetivo != None:
            node_objetivo.value = value
        else:
            return None
    def insert(self, indice, value):
        # Agrega un elemento en donde sea en la linkedlist dado el indice
        if indice == self.size - 1:
            return self.append(value)
        elif not (indice >= self.size or indice < 0):
            nuevo_nodo = self._Node(value)
            nodos_anteriores = self.get(indice)
            nodos_siguientes = nodos_anteriores.node_next
            nodos_anteriores.node_next = nuevo_nodo
            nuevo_nodo.node_before = nodos_anteriores
            nuevo_nodo.node_next = nodos_siguientes
            nodos_siguientes.node_before = nuevo_nodo
            self.size += 1
        else:
            return None
    def remove(self, indice):
        # Saca un elemento de donde sea de la linkedlist dado un indice
        if indice == 0:
            return self.shift()
        elif indice == self.size - 1:
            return self.pop()
        elif not (indice >= self.size or indice < 0):
            node_removido = self.get(indice)
            nodos_anteriores = node_removido.node_before
            nodos_siguientes = node_removido.node_next
            nodos_anteriores.node_next = nodos_siguientes
            nodos_siguientes.node_before  = nodos_anteriores
            node_removido.node_before = None
            node_removido.node_next = None
            self.size -= 1
            return node_removido
        else:
            return None
    def reverse(self):
        # Revierte los nodos de la linkedlist
        nodos_revertidos = None
        self.head.node_before = None
        self.queue.node_next = None
        node_actual = self.head
        self.queue = node_actual
        while node_actual != None:
            nodos_revertidos = node_actual.node_before
            node_actual.node_before = node_actual.node_next
            node_actual.node_next = nodos_revertidos
            node_actual = node_actual.node_before
        self.head = nodos_revertidos.node_before
        self.head.node_before = self.queue
        self.queue.node_next = self.head

cll = CircleLinkedList()