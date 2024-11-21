class Single_linked_list:
    class _Node:
        def __init__(self, value) -> None:
            self.value = value
            self.node_next = None
    
    def __init__(self) -> None:
        self.head = None
        self.queue = None
        self.size = 0
    
    def __str__(self) -> str:
        arr = []
        current_node = self.head
        while current_node != None:
            arr.append(current_node.value)
            current_node = current_node.node_next
        return str(arr) + "size: " + str(self.size)

    def append(self, value) -> None:
        node_new = self._Node(value)
        if self.head == None and self.queue == None:
            self.head = node_new
            self.queue = node_new
        else:
            self.queue.node_next = node_new
            self.queue = node_new
        self.size += 1
    
    def prepend(self, value) -> None:
        node_new = self._Node(value)
        if self.head == None and self.queue == None:
            self.head = node_new
            self.queue = node_new
        else:
            node_new.node_next = self.head
            self.head = node_new
        self.size += 1
    
    def shift(self) -> str:
        #remove first value from single linked list
        if self.size == 0:
            self.head = None
            self.queue = None
        else:
            node_delete = self.head
            self.head = node_delete.node_next
            node_delete.node_next = None
            self.size -= 1
            return print(node_delete.value)

    def pop(self):
        #delete last value from single linked list
        if self.size == 0:
            self.head = None
            self.queue = None
        else:
            current_node = self.head
            new_queue = current_node
            while current_node.node_next != None:
                new_queue = current_node
                current_node = current_node.node_next
            self.queue = new_queue
            self.queue.node_next = None
            self.size -= 1
            return print(current_node.value)
    
    def get(self, index):
        # get a node
        if index == self.size - 1:
            print(self.queue.value)
            return self.queue
        elif index == 0:
            print(self.head.value)
            return self.head
        elif not (index >= self.size or index < 0):
            current_node = self.head
            counter = 0
            while counter != index:
                current_node = current_node.node_next
                counter += 1
            print(current_node.value)
            return current_node
        else:
            return None


sll = Single_linked_list()

sll.prepend("A")
sll.prepend("B")
sll.prepend("C")

sll.get(1)
sll.get(2)
sll.get(3)

