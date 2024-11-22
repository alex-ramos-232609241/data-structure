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
    
    def update(self, index, value) -> None:
        target_node = self.get(index)
        if target_node != None:
            target_node.value = value
        else:
            return None

    def insert(self, index, value):
        if index == self.size - 1:
            return self.append(value)
        elif not (index >= self.size or index < 0):
            node_new = self._Node(value)
            before_node = self.get(index)
            node_next = before_node.node_next
            before_node.node_next = node_new
            node_new.node_next = node_next
            self.size += 1
        else:
            return None
    
    def remove(self, index):
        if index == 0:
            return self.shift()
        elif index == self.size - 1:
            return self.pop()
        elif not (index >= self.size or index < 0):
            before_node = self.get(index - 1)
            node_remove = before_node.node_next
            before_node.node_next = node_remove.node_next
            node_remove.node_next = None
            self.size -= 1
            return node_remove
        else:
            return None

    def reverse(self):
        node_reverse = None
        current_node = self.head
        self.queue = current_node
        while current_node != None:
            node_next = current_node.node_next
            current_node.node_next = node_reverse
            node_reverse = current_node
            current_node = node_next
        self.head = node_reverse
        return self.head


sll = Single_linked_list()

sll.prepend("A")
sll.prepend("B")
sll.prepend("C")
sll.prepend("D")

print(sll)
sll.reverse()
print(sll)

