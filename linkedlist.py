class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    # 1) Je zoznam prazdny?
    def is_empty(self):
        return self.head is None

    # 2) Velkost zoznamu
    def size(self):
        return self._size

    # 3) Vlozenie na zaciatok
    def add_first(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self._size += 1

    # 4) Vlozenie na koniec
    def add_last(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    # 5) Odobratie prveho prvku a jeho navrat
    def remove_first(self):
        if self.head is None:
            raise IndexError("empty LinkedList")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return value

    # 6) Odobratie posledneho prvku a jeho navrat
    def remove_last(self):
        if self.head is None:
            raise IndexError("empty LinkedList")
        if self.head is self.tail:
            value = self.head.value
            self.head = self.tail = None
            self._size -= 1
            return value
        current = self.head
        while current.next is not self.tail:
            current = current.next
        value = self.tail.value
        current.next = None
        self.tail = current
        self._size -= 1
        return value

    # 7) Nahlad na prvy prvok (bez zmazania)
    def peek_first(self):
        if self.head is None:
            raise IndexError("empty LinkedList")
        return self.head.value

    # 8) Nahlad na posledny prvok (bez zmazania)
    def peek_last(self):
        if self.tail is None:
            raise IndexError("empty LinkedList")
        return self.tail.value

    # 9) Vymazanie vsetkych prvkov
    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0

    # 10) Vyhladanie prvku - vrati index alebo -1
    def index_of(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    # 11) Vlozenie na zadany index (0 <= index <= size)
    def insert_at(self, index, value):
        if index < 0 or index > self._size:
            raise IndexError("index out of range")
        if index == 0:
            self.add_first(value)
            return
        if index == self._size:
            self.add_last(value)
            return
        prev = None
        current = self.head
        for _ in range(index):
            prev = current
            current = current.next
        new_node = Node(value, current)
        prev.next = new_node
        self._size += 1

    # 12) Zmazanie prvku na indexe - vrati jeho hodnotu
    def remove_at(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        if index == 0:
            return self.remove_first()
        prev = None
        current = self.head
        for _ in range(index):
            prev = current
            current = current.next
        prev.next = current.next
        if current is self.tail:
            self.tail = prev
        self._size -= 1
        return current.value

    # 13) Prevod na Python zoznam
    def to_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

    # 14) Obratenie zoznamu
    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def __str__(self):
        return str(self.to_list())

    def __len__(self):
        return self._size
