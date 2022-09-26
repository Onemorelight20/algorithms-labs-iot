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
    def __init__(self, root=Node.constructNULL()):
        self.NULL = NULL
        self.root = self.NULL
        if root is not NULL:
            self.root = root

    def delete_node(self, value):
        self.__delete_node(self.root, value)

    def print_tree(self):
        self.__print_helper(self.root, "", True)

    def __delete_node(self, node, key):
        node_to_delete = self.NULL
        while node is not self.NULL:
            if node.value is key:
                node_to_delete = node
            if node.value <= key:
                node = node.right
            else:
                node = node.left

        if node_to_delete is self.NULL:
            print("Value is not present in the tree")
            return

        if node_to_delete.left is self.NULL:
            node_to_fix_deletion = node_to_delete.right
            self.__swap(node_to_delete, node_to_delete.right)
        elif node_to_delete.right is self.NULL:
            node_to_fix_deletion = node_to_delete.left
            self.__swap(node_to_delete, node_to_delete.left)
        else:
            node_to_swap_with = self.__find_minimum(node_to_delete.right)
            node_to_fix_deletion = node_to_swap_with.right
            if node_to_swap_with.parent is node_to_delete:
                node_to_fix_deletion.parent = node_to_swap_with
            else:
                self.__swap(node_to_swap_with, node_to_swap_with.right)
                node_to_swap_with.right = node_to_delete.right
                node_to_swap_with.right.parent = node_to_swap_with

            self.__swap(node_to_delete, node_to_swap_with)
            node_to_swap_with.left = node_to_delete.left
            node_to_swap_with.left.parent = node_to_swap_with
            node_to_swap_with.color = node_to_delete.color
        if node_to_delete.color is BLACK:
            self.__fix_tree_after_deletion(node_to_fix_deletion)

    def __find_minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node

    def __fix_tree_after_deletion(self, node_to_fix):
        while node_to_fix != self.root and node_to_fix.color is BLACK:
            if node_to_fix is node_to_fix.parent.left:
                sibling = node_to_fix.parent.right
                # case 1: sibling is red -> it`s children are black
                if sibling.color is RED:
                    sibling.color, node_to_fix.parent.color = BLACK, RED
                    self.__left_rotate(node_to_fix.parent)
                    sibling = node_to_fix.parent.right
                # case 4: sibling is black, and it`s children are black too
                if sibling.left.color is BLACK and sibling.right.color is BLACK:
                    sibling.color = RED
                    node_to_fix = node_to_fix.parent
                else:
                    # case 3: node_to_fix is black, sibling is black, sibling`s right child is black
                    if sibling.right.color is BLACK:
                        sibling.left.color = BLACK
                        sibling.color = RED
                        self.__right_rotate(sibling)
                        sibling = node_to_fix.parent.right
                    # case 2: node_to_fix is black, sibling is black, sibling`s right child is red
                    sibling.color = node_to_fix.parent.color
                    node_to_fix.parent.color = BLACK
                    sibling.right.color = BLACK
                    self.__left_rotate(node_to_fix.parent)
                    node_to_fix = self.root
            # if the node_to_fix is parent`s right child
            else:
                sibling = node_to_fix.parent.left
                # case 1: sibling is red -> it`s children are black
                if sibling.color is RED:
                    sibling.color = BLACK
                    node_to_fix.parent.color = RED
                    self.__right_rotate(node_to_fix.parent)
                    sibling = node_to_fix.parent.left
                # case 4: sibling is black, and it`s children are black too
                if sibling.right.color is BLACK and sibling.right.color is BLACK:
                    sibling.color = RED
                    node_to_fix = node_to_fix.parent
                else:
                    # case 3: node_to_fix is black, sibling is black, sibling`s left child is black
                    if sibling.left.color is BLACK:
                        sibling.right.color = BLACK
                        sibling.color = RED
                        self.__left_rotate(sibling)
                        sibling = node_to_fix.parent.left
                    # case 2: node_to_fix is black, sibling is black, sibling`s left child is red
                    sibling.color = node_to_fix.parent.color
                    node_to_fix.parent.color = BLACK
                    sibling.left.color = BLACK
                    self.__right_rotate(node_to_fix.parent)
                    node_to_fix = self.root
        node_to_fix.color = BLACK

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

            string_color = "RED" if node.color is RED else "BLACK"
            print(str(node.value) + " IS " + string_color)
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    def __left_rotate(self, node_to_rotate):
        right_child_of_rotated_node = node_to_rotate.right
        node_to_rotate.right = right_child_of_rotated_node.left
        if right_child_of_rotated_node.left != self.NULL:
            right_child_of_rotated_node.left.parent = node_to_rotate

        right_child_of_rotated_node.parent = node_to_rotate.parent
        if node_to_rotate.parent is None:
            self.root = right_child_of_rotated_node
        elif node_to_rotate is node_to_rotate.parent.left:
            node_to_rotate.parent.left = right_child_of_rotated_node
        else:
            node_to_rotate.parent.right = right_child_of_rotated_node
        right_child_of_rotated_node.left = node_to_rotate
        node_to_rotate.parent = right_child_of_rotated_node

    def __right_rotate(self, node_to_rotate):
        left_child_of_rotated_node = node_to_rotate.left
        node_to_rotate.left = left_child_of_rotated_node.right
        if left_child_of_rotated_node.right != self.NULL:
            left_child_of_rotated_node.right.parent = node_to_rotate

        left_child_of_rotated_node.parent = node_to_rotate.parent
        if node_to_rotate.parent is None:
            self.root = left_child_of_rotated_node
        elif node_to_rotate is node_to_rotate.parent.right:
            node_to_rotate.parent.right = left_child_of_rotated_node
        else:
            node_to_rotate.parent.left = left_child_of_rotated_node
        left_child_of_rotated_node.right = node_to_rotate
        node_to_rotate.parent = left_child_of_rotated_node
