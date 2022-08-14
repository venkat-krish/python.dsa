# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from linear.linkedlist import SinglyLinkedList, DoublyLinkedList



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    data = [12, 23,34,45,56]

    linked_list = SinglyLinkedList()

    for i in data:
        linked_list.add(i)

    for elem in linked_list.traverse():
        print(elem)

    # print('Enter the value to search')
    # value = int(input())
    # # 2. Test case for search
    # print('The value %d is found %s' % (value, linked_list.search(value)))
    #
    # # 3. Remove the node from the front
    # print(linked_list.remove(value))
    #
    # for elem in linked_list.traverse():
    #     print(elem)
    print("\n Print the list in reverse order")
    # 4. Reverse traversal
    for elm in linked_list.reverse_traverse():
        print(elm)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

    doubly_linkedlist = DoublyLinkedList()

    for i in data:
        doubly_linkedlist.add(i)
    print(f'Size of the list {doubly_linkedlist.length}')

    print('\n Printing doubly linked list:')
    for elm in doubly_linkedlist.traverse():
        print(elm)

    print('\n Printing doubly linked list in reverse order:')
    for elm in doubly_linkedlist.reverse_traverse():
        print(elm)

    # print(doubly_linkedlist.remove(34))
    #
    # print('\n Printing doubly linked list:')
    # for elm in doubly_linkedlist.traverse():
    #     print(elm)

    print(f'Size of the list {doubly_linkedlist.length}')
    order = 3
    print('\n Remove the {} node from reverse'.format(order))
    doubly_linkedlist.remove_from_reverse(order)

    print('\n Printing doubly linked list:')
    for elm in doubly_linkedlist.traverse():
        print(elm)
