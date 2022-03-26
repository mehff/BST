ROOT = "root"


class Node:
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.word)


class BinaryTree:
    def __init__(self, word=None, node=None):
        if node:
            self.root = node
        elif word:
            node = Node(word)
            self.root = node
        else:
            self.root = None

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        if node.right:
            self.inorder_traversal(node.right)

    def height(self, node=None):

        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        else:
            return hleft + 1


class BinarySearchTree(BinaryTree):

    def insert(self, word):
        parent = None
        r = self.root
        while r:
            parent = r
            if word < r.word:
                r = r.left
            else:
                r = r.right
        if parent is None:
            self.root = Node(word)
        elif word < parent.word:
            parent.left = Node(word)
        else:
            parent.right = Node(word)

    def search(self, word):
        return self._search(word, self.root)

    def _search(self, word, node):
        if node is None:
            return node
        if node.word == word:
            return BinarySearchTree(node)
        if word < node.word:
            return self._search(word, node.left)
        return self._search(word, node.right)
