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

    def __left_rotate(self, node_to_rotate):
        right_child_of_rotated_node = node_to_rotate.right
        node_to_change_parent = right_child_of_rotated_node.left

        right_child_of_rotated_node.left = node_to_rotate
        node_to_rotate.right = node_to_change_parent

        node_to_rotate.height = 1 + max(self.__get_height(node_to_rotate.left),
                                        self.__get_height(node_to_rotate.right))
        right_child_of_rotated_node.height = 1 + max(self.__get_height(right_child_of_rotated_node.left),
                                                     self.__get_height(right_child_of_rotated_node.right))
        return right_child_of_rotated_node

    def __right_rotate(self, node_to_rotate):
        left_child_of_rotated_node = node_to_rotate.left
        node_to_change_parent = left_child_of_rotated_node.right

        left_child_of_rotated_node.right = node_to_rotate
        node_to_rotate.left = node_to_change_parent

        node_to_rotate.height = max(self.__get_height(node_to_rotate.left),
                                    self.__get_height(node_to_rotate.right))
        left_child_of_rotated_node.height = max(self.__get_height(left_child_of_rotated_node.left),
                                                self.__get_height(left_child_of_rotated_node.right))
        return left_child_of_rotated_node

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

        print(f"{node.value} BalanceFactor is {self.__get_balance_factor(node)} |||||", end="")
        self.__preorder_print_helper(node.left)
        self.__preorder_print_helper(node.right)
