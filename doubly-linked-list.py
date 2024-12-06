class Double_linked_List:
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
        arr = []
        current_node = self.head
        while current_node != None:
            arr.append(current_node.value)
            current_node = current_node.node_next
        return str(arr) + "size: " + str(self.size)
    
    def prepend(self, value):
        node_new = self._Node(value)
        if self.head == None and self.queue == None:
            self.head = node_new
            self.queue = node_new
        else:
            self.head.node_before = node_new
            node_new.node_next = self.head
            self.head = node_new
        self.size+=1
    
    def append(self, value):
        node_new = self._Node(value)
        if self.head == None and self.queue == None:
            self.head = node_new
            self.queue = node_new
        else:
            self.queue.node_next = node_new
            node_new.node_before = self.queue
            self.queue = node_new
        self.size+=1
    
    def shift(self):
        if self.size == 0:
            self.head = None
            self.queue = None
        elif self.head != None:
            node_deleted = self.head
            self.head = node_deleted.node_next
            node_deleted.node_next = None
            self.size-=1
            return print(node_deleted.value)
    
    def pop(self):
        if self.size == 0:
            self.head = None
            self.queue = None
        else:
            node_deleted = self.queue
            self.queue = node_deleted.node_before
            self.queue.node_next = None
            node_deleted.node_before = None
            self.size-=1
            return print(node_deleted.value)
    
    def get(self, index):
        if index == self.size - 1:
            print(self.queue.value)
            return self.queue
        elif index == 0:
            print(self.head.value)
            return self.head
        elif not (index >= self.size or index < 0):
            index_balance = int(self.size / 2)
            if index <= index_balance:
                current_node = self.head
                count = 0
                while count != index:
                    current_node = current_node.node_next
                    count+=1
                print(current_node.value)
                return current_node
            else:
                current_node = self.queue
                count = self.size - 1
                while count != index:
                    current_node = current_node.node_before
                    count-=1
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
            node_new.node_before = nodes_before
            node_new.node_next = nodes_next
            nodes_next.node_before = node_new
            self.size += 1
        else:
            return None
    
    def remove(self, index):
        if index == 0:
            return self.shift()
        elif index == self.size:
            return self.pop()
        elif not (index >= self.size or index < 0):
            node_remove = self.get(index)
            node_before = node_remove.node_before
            node_next = node_remove.node_next
            node_before.node_next = node_next
            node_next.node_before = node_before
            node_remove.node_before = None
            node_remove.node_next = None
            self.size-=1
        else:
            return None
    
    def reverse(self):
        node_reverse = None
        current_node = self.head
        self.queue = current_node
        while current_node != None:
            node_reverse = current_node.node_before
            current_node.node_before = current_node.node_next
            current_node.node_next = node_reverse
            current_node = current_node.node_before
        self.head = node_reverse.node_before

dll = Double_linked_List()
dll.prepend('A')
dll.prepend('B')
dll.prepend('C')
dll.prepend('D')

dll.reverse()

print(dll)