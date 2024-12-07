class CircularLinkedList:
    class _Node:
        def __init__(self, value):
            self.value = value
            self.node_next = None
    
    def __init__(self) -> None:
        self.head = None
        self.queue = None
        self.size = 0
    
    def __str__(self) -> str:
        arr = []
        current_node = self.head
        pivot = True
        count = self.size
        while count != 0:
            if pivot != False or current_node != self.head:
                arr.append(current_node.value)
                current_node = current_node.node_next
                pivot = False
                count -= 1
            else:
                break
        return str(arr) + "Size: " + str(self.size)

    def prepend(self, value):
        node_new = self._Node(value)
        if self.head == None and self.queue == None:
            self.head = node_new
            self.queue = node_new
        else:
            node_new.node_next = self.head
            self.queue.node_next = node_new
            self.head = node_new
        self.size+=1
    
    def append(self, value):
        node_new = self._Node(value)
        if self.head == None and self.queue == None:
            self.head = node_new
            self.queue = node_new
        else:
            self.queue.node_next = node_new
            node_new.node_next  = self.head
            self.queue = node_new
        self.size += 1
    
    def shift(self):
        if self.size == 0:
            self.head = None
            self.queue = None
        else:
            node_deleted = self.head
            self.head = node_deleted.node_next
            self.queue.node_next = self.head
            node_deleted.node_next = None
            self.size -= 1
            return print(node_deleted.value)
    
    def pop(self):
        if self.size == 0:
            self.head = None
            self.queue = None
        else:
            current_node = self.head
            new_queue = current_node
            count = self.size
            while count != 0:
                if current_node.node_next != self.head:
                    new_queue = current_node
                    current_node = current_node.node_next
                else:
                    break
            self.queue = new_queue
            self.queue.node_next = self.head
            self.size -= 1
            return print(current_node.value)
    
    def get(self, index):
        if index == self.size - 1:
            print(self.queue.value)
            return self.queue
        elif index == 0:
            print(self.head.value)
            return self.head
        elif not (index >= self.size or index < 0):
            current_node = self.head
            count = 0
            while count != index:
                current_node = current_node.node_next
                count += 1
            print(current_node.value)
            return current_node
        else:
            return None
    
    def update(self, index, value):
        node_target = self.get(index)
        if node_target != None:
            node_target.value = value
        else:
            return None
    
    def insert(self, index, value):
        if index == self.size - 1:
            return self.append(value)
        elif not (index >= self.size or index < 0):
            node_new = self._Node(value)
            nodes_before = self.get(index)
            nodes_next = nodes_before.node_next
            nodes_before.node_next = node_new
            node_new.node_next = nodes_next
            self.size += 1
        else:
            return None
    
    def remove(self, index):
        if index == 0:
            return self.shift()
        elif index == self.size - 1:
            return self.pop()
        elif not (index >= self.size or index < 0):
            nodes_before = self.get(index - 1)
            node_remove = nodes_before.node_next
            nodes_before.node_next = node_remove.node_next
            node_remove.node_next = None
            self.size -= 1
            return node_remove
        else:
            return None
    
    def reverse(self):
        nodes_reverse = None
        current_node = self.head
        self.queue = current_node
        pivot = True
        count = self.size
        while count != 0:
            if pivot != False or current_node != self.head:
                node_next = current_node.node_next
                current_node.node_next = nodes_reverse
                nodes_reverse = current_node
                current_node = node_next
                pivot = False
                count -= 1
            else:
                break
        self.head = nodes_reverse
        self.queue.node_next = self.head