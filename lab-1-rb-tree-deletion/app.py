from red_black_tree_deletion import RedBlackTree, Node, BLACK, NULL
from avl_tree_insertion import AVLTree


def show_rb_tree_deletion():
    node20 = Node(20, color=BLACK)
    node5 = Node(5, parent=node20)
    node30 = Node(30, color=BLACK, parent=node20)
    node10 = Node(10, color=BLACK, parent=node5)
    node4 = Node(4, color=BLACK, parent=node5)
    node3 = Node(3, parent=node4)
    node20.left = node5
    node20.right = node30
    node5.left = node4
    node5.right = node10
    node4.left = node3
    node3.left, node3.right = NULL, NULL
    node10.left, node10.right = NULL, NULL
    node30.left, node30.right = NULL, NULL
    node4.right = NULL


    tree = RedBlackTree(node20)

    tree.print_tree()
    tree.delete_node(20)
    tree.print_tree()


def show_avl_tree_insertion1():
    tree = AVLTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.preorder_print()


def show_avl_tree_insertion2():
    tree = AVLTree()
    tree.insert(5)
    tree.insert(10)
    tree.insert(8)

    tree.preorder_print()


if __name__ == "__main__":
    show_avl_tree_insertion1()
    show_avl_tree_insertion2()
    show_rb_tree_deletion()
