class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self.__insert_processing(self.root, key)

    # visit left right
    def preorder_print(self):
        self.__preorder_print_helper(self.root)
        print()

    def __insert_processing(self, node, key):

        if not node:
            return Node(key)
        elif key < node.value:
            node.left = self.__insert_processing(node.left, key)
        else:
            node.right = self.__insert_processing(node.right, key)

        node.height = 1 + max(self.__get_height(node.left), self.__get_height(node.right))

        return self.__rebalanced_if_needed(node, key)

    def __rebalanced_if_needed(self, node, key):
        balance_factor = self.__get_balance_factor(node)

        if balance_factor > 1 and key < node.left.value:
            return self.__right_rotate(node)
        elif balance_factor < -1 and key > node.right.value:
            return self.__left_rotate(node)
        elif balance_factor > 1 and key > node.left.value:
            node.left = self.__left_rotate(node.left)
            return self.__right_rotate(node)
        elif balance_factor < -1 and key < node.right.value:
            node.right = self.__right_rotate(node.right)
            return self.__left_rotate(node)

        return node

    def __left_rotate(self, a):
        b = a.right
        T2 = b.left

        b.left = a
        a.right = T2

        a.height = 1 + max(self.__get_height(a.left), self.__get_height(a.right))
        b.height = 1 + max(self.__get_height(b.left), self.__get_height(b.right))
        return b

    def __right_rotate(self, b):
        a = b.left
        T2 = a.right

        a.right = b
        b.left = T2

        b.height = 1 + max(self.__get_height(b.left), self.__get_height(b.right))
        a.height = 1 + max(self.__get_height(a.left), self.__get_height(a.right))
        return a

    def __get_balance_factor(self, node):
        if not node:
            return 0

        return self.__get_height(node.left) - self.__get_height(node.right)

    def __get_height(self, node):
        if not node:
            return 0

        return node.height

    def __preorder_print_helper(self, node):
        if not node:
            return

        print("{0} ".format(node.value), end="")
        self.__preorder_print_helper(node.left)
        self.__preorder_print_helper(node.right)
