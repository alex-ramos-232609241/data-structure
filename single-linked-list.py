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

sll = Single_linked_list()

sll.prepend("A")
sll.prepend("B")
sll.prepend("C")

print(sll)
    
