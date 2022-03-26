from tree import BinarySearchTree


def f1r():
    f1 = open('file1.txt', 'r+')
    f1rd = f1.read()
    return f1rd


def f2r():
    f2 = open('file2.txt', 'r+')
    f2rd = f2.read()
    return f2rd


def f3r():
    f3 = open('file3.txt', 'r+')
    f3rd = f3.read()
    return f3rd


def allWords():
    allw = (f1r() + f2r() + f3r())
    listw = allw.split(',')
    return listw


def allFilesToTree():
    values = allWords()
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree


def filesToTree(f):
    values = f
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree
