from linkedlist import LinkedList


class DFifo:
    """Dynamicka fronta (FIFO) implementovana pomocou LinkedList.
    Na rozdiel od statickej Fifo nema pevnu kapacitu - rastie podla potreby.
    """

    def __init__(self):
        self._list = LinkedList()

    def put(self, item):
        """Vlozi prvok na koniec fronty."""
        self._list.add_last(item)

    def get(self):
        """Vyberie a vrati prvok zo zaciatku fronty."""
        if self._list.is_empty():
            raise IndexError("empty DFIFO")
        return self._list.remove_first()

    def getLength(self):
        """Vrati aktualny pocet prvkov vo fronte."""
        return self._list.size()

    def __str__(self):
        return str(self._list)

    def raw(self):
        return self._list.to_list()
