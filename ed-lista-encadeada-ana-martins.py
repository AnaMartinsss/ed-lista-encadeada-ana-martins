#exercicio aula 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def remove(self, value):
        current = self.head
        previous = None

        while current:
            if current.data == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True

            previous = current
            current = current.next

        return False

    def search(self, value):
        current = self.head

        while current:
            if current.data == value:
                return True
            current = current.next

        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def size(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count


lista = LinkedList()

lista.insert_beginning(3)
lista.insert_beginning(1)
lista.insert_end(5)
lista.insert_end(7)

lista.print_list()

print("Tamanho:", lista.size())
print("Buscar 5:", lista.search(5))

lista.remove(3)
lista.print_list()

