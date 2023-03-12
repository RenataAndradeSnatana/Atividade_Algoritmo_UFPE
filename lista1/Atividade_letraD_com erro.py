class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Historico:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def remove(self, value):
        node = self.find_node(value)
        if node is None:
            return
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

    def find_node(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                return node
            node = node.next
        return None

    def find(self, value):
        node = self.find_node(value)
        if node is None:
            return
        self.remove(value)
        self.add(value)

    def exib(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next


historico = Historico()
while True:
    command = input().split()
    if command[0] == 'ADD':
        historico.add(command[1])
    elif command[0] == 'REM':
        historico.remove(command[1])
    elif command[0] == 'FIND':
        historico.find(command[1])
    elif command[0] == 'EXIB':
        historico.exib()
    elif command[0] == 'END':
        break
