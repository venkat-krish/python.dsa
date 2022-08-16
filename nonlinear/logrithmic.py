

class Heap:
    def __init__(self):
        self.heap = []
        self.count = 0

    def add(self, value):
        '''
        value is the data to be added in the node
        Count is the number of items in the heap
        :param value:
        :return:
        '''
        try:
            self.heap.append(value)
            self.count += 1
            self.min_heapify()
        except IndexError as ie:
            print(f'Index error {value}, {self.count} : {ie}')

    def __swap(self, left, right):
        self.heap[left], self.heap[right] = self.heap[right], self.heap[left]

    def display(self):
        for i in self.heap:
            print(i)

    def min_heapify(self):
        '''
        Count is to keep the track of number of items in the heap
        :return:d
        '''
        i = self.count - 1
        while i > 0 and self.heap[i] < self.heap[int((i-1)/2)]:
            self.__swap(i, int((i-1)/2))
            i = int((i - 1)/2)