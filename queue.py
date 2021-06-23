class Queue:
    def __init__(self):
        self.temp = []

    # Добавляет элемент в конец очереди
    def add_element(self, element):
        self.temp.append(element)

    # Очищает очередь
    def clear(self):
        self.temp[:] = []

    # Возвращает размер очереди
    def size(self):
        return len(self.temp)

    # Удаляет первый элемент и возвращает его
    def del_element(self):
        return self.temp.pop(0)
