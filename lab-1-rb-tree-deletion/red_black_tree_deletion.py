BLACK = 0
RED = 1


class Node:
    def __init__(self, value, parent=None, left=None, right=None, color=RED):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.color = color

    @staticmethod
    def constructNULL():
        obj = Node(0)
        obj.color = BLACK
        obj.left = None
        obj.right = None
        return obj


NULL = Node.constructNULL()


class RedBlackTree:
    def __init__(self):
        self.NULL = NULL
        self.root = self.NULL

    def __init__(self, root):
        self.NULL = NULL
        self.root = root

    def delete_node(self, value):
        self.__delete_node(self.root, value)

    def print_tree(self):
        self.__print_helper(self.root, "", True)

    def __delete_node(self, node, key):
        node_to_delete = self.NULL
        while node != self.NULL:
            if node.value == key:
                node_to_delete = node
            if node.value <= key:
                node = node.right
            else:
                node = node.left

        if node_to_delete == self.NULL:
            print("Value is not present in the tree")
            return

        y = node_to_delete
        y_original_color = y.color
        if node_to_delete.left == self.NULL:
            x = node_to_delete.right
            self.__swap(node_to_delete, node_to_delete.right)
        elif node_to_delete.right == self.NULL:
            x = node_to_delete.left
            self.__swap(node_to_delete, node_to_delete.left)
        else:
            y = self.__find_minimum(node_to_delete.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node_to_delete:
                x.parent = y
            else:
                self.__swap(y, y.right)
                y.right = node_to_delete.right
                y.right.parent = y

            self.__swap(node_to_delete, y)
            y.left = node_to_delete.left
            y.left.parent = y
            y.color = node_to_delete.color
        if y_original_color == BLACK:
            self.__fix_tree_after_deletion(x)

    def __find_minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node

    def __fix_tree_after_deletion(self, x):
        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                sibling = x.parent.right
                if sibling.color == RED:
                    sibling.color = BLACK
                    x.parent.color = RED
                    self.__left_rotate(x.parent)
                    sibling = x.parent.right
                if sibling.left.color == BLACK and sibling.right.color == BLACK:
                    sibling.color = RED
                    x = x.parent
                else:
                    if sibling.right.color == BLACK:
                        sibling.left.color = BLACK
                        sibling.color = RED
                        self.__right_rotate(sibling)
                        sibling = x.parent.right

                    sibling.color = x.parent.color
                    x.parent.color = BLACK
                    sibling.right.color = RED
                    self.__left_rotate(x.parent)
                    x = self.root
            else:
                sibling = x.parent.left
                if sibling.color == RED:
                    sibling.color = BLACK
                    x.parent.color = RED
                    self.__right_rotate(x.parent)
                    sibling = x.parent.left

                if sibling.right.color == BLACK and sibling.right.color == BLACK:
                    sibling.color = RED
                    x = x.parent
                else:
                    if sibling.left.color == BLACK:
                        sibling.right.color = BLACK
                        sibling.color = RED
                        self.__left_rotate(sibling)
                        sibling = x.parent.left

                    sibling.color = x.parent.color
                    x.parent.color = BLACK
                    sibling.left.color = BLACK
                    self.__right_rotate(x.parent)
                    x = self.root
        x.color = BLACK

    def __swap(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def __print_helper(self, node, indent, last):
        if node != self.NULL:
            print(indent, end=' ')
            if last:
                print("R----", end=' ')
                indent += "     "
            else:
                print("L----", end=' ')
                indent += " |   "

            string_color = "RED" if node.color == RED else "BLACK"
            print(str(node.value) + "(" + string_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    def __left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def __right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
