class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.color = 1  # 1 for red, 0 for black


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(0)
        self.NIL.color = 0
        self.NIL.left = None
        self.NIL.right = None
        self.root = self.NIL

    def insert(self, val):
        node = Node(val)
        node.parent = None
        node.left = self.NIL
        node.right = self.NIL
        node.color = 1  # new node is always red

        y = None
        x = self.root

        while x != self.NIL:
            y = x
            if node.val < x.val:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.val < y.val:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = 0
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)

    def fix_insert(self, node):
        while node.parent.color == 1:
            if node.parent == node.parent.parent.right:
                u = node.parent.parent.left  # uncle
                if u.color == 1:
                    u.color = 0  # change the colors
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent  # perform right rotation
                        self.right_rotate(node)
                    node.parent.color = 0  # recolor and rotate
                    node.parent.parent.color = 1
                    self.left_rotate(node.parent.parent)
            else:
                u = node.parent.parent.right  # uncle

                if u.color == 1:
                    u.color = 0  # change the colors
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent  # perform left rotation
                        self.left_rotate(node)
                    node.parent.color = 0  # recolor and rotate
                    node.parent.parent.color = 1
                    self.right_rotate(node.parent.parent)

            if node == self.root:
                break
        self.root.color = 0

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def print_tree(self, node, level=0):
        if node != self.NIL:
            self.print_tree(node.right, level + 1)

            print(' ' * 4 * level + '->', node.val, ' ' + ('R' if node.color == 1 else 'B'))
            self.print_tree(node.left, level + 1)

tree = RedBlackTree()
tree.insert(55)
tree.insert(40)
tree.insert(65)
tree.insert(60)
tree.insert(75)
tree.insert(57)
tree.print_tree(tree.root)