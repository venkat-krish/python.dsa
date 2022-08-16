from nonlinear.logrithmic import Heap

if __name__ == '__main__':
    heap_struct = Heap()

    data = [3, 9, 12, 7, 1]

    for i in data:
        heap_struct.add(i)

    heap_struct.display()
