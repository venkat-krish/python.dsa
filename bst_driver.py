from nonlinear.trees import BinarySearchTree


if __name__ == '__main__':

    bst = BinarySearchTree()

    data = [23, 14, 31, 7, 17, 9]

    for i in data:
        bst.insert(i)
    print('\n Preorder traversal: ')
    bst.preOrder(bst.root)
    print('\n Post-order traversal: ')
    bst.postOrder(bst.root)
    print('\n In-order traversal: ')
    bst.inOrder(bst.root)

    print(f'The min value of BST is {bst.findMin(bst.root)}')
    print(f'The max value of BST is {bst.findMax(bst.root)}')