import resources
import tree
from tree import BinarySearchTree


def seek_words():
    words = input(print('---Que palavra(s) deseja procurar? Separe-as pelo caractere ","'))
    wordsl = words.split(',')

    bsts = resources.allFilesToTree()
    bsts.inorder_traversal()

    itms = wordsl
    for itm in itms:
        s = bsts.search(itm)
        if s is None:
            print(itm, "não encontrado")
        else:
            print(s.root.word, 'encontrado')
    print('\n\n')
    user_interface()


def input_words():
    fin = None
    fileid = int(input(print('---Em qual arquivo deseja inserir?\n1)--file1.txt\n2)--file2.txt\n3)--file3.txt')))
    if fileid == 1:
        fin = open('file1.txt', 'r+')
        fin.read()
    if fileid == 2:
        fin = open('file2.txt', 'r+')
        fin.read()
    if fileid == 3:
        fin = open('file3.txt', 'r+')
        print('-Arquivo "file3.txt" aberto.')
        fin.read()

    wordin = input(print('Digite a(s) palavra(s) que você deseja inserir, separadas pelo caractere ","'))
    wordlst = wordin.split(',')
    bsti = BinarySearchTree()
    for w in wordlst:
        bsti.insert(w)
        fin.write(w + ',')
        fin.read()
        print('A palavra', w, 'foi inserida.')

    user_interface()


def count_words():
    words = input(print('---Quais palavra(s) deseja procurar? Separe-as pelo caracter ","\n---Caso deseje ver a '
                        'frequência de todas as palavras, digite "freqall"'))
    if words == 'freqall':
        wordsl = resources.allWords()
        bstc = resources.allFilesToTree()
        bstc.inorder_traversal()

        wordc = []

        itms = wordsl
        for itm in itms:
            s = bstc.search(itm)
            if s is None:
                print(itm, "não existe.")
            else:
                wordc.append(str(s.root.word))

        for wd in range(0, len(wordc)):
            print('Frequência:', wordc[wd], 'aparece', wordc.count(wordc[wd]), 'vez.')
    else:
        wordsl = words.split(',')
        bstc = resources.allFilesToTree()
        bstc.inorder_traversal()
        wordc = []
        itms = resources.allWords()
        for itm in itms:
            s = bstc.search(itm)
            if s is None:
                print(itm, "não existe.")
            else:
                wordc.append(str(s.root.word))

        for w in range(0, len(wordsl)):
            for wd in range(0, len(wordc)):
                if wordsl[w] == wordc[wd]:
                    print('Frequência:', wordc.count(wordc[wd]), wordsl[w])

    user_interface()


def height_words():
    bstftt = resources.allFilesToTree()
    bstftt.inorder_traversal()
    th = tree.BinaryTree.height(bstftt)
    print('A altura da árvore é', th, '.')
    user_interface()


def user_interface():
    print('\n~~~~ATP MÉTODOS DE PESQUISA E ORDENAÇÃO EM ESTRUTURAS DE DADOS~~~~\n\nQue operação deseja realizar?\n')
    fnc = int(input(print('----1) Buscar palavras\n----2) Inserir palavras\n----3) Frequência de palavras\n----4) '
                          'Altura da Árvore\n----5) Encerrar o programa')))

    if fnc == 1:
        seek_words()
    if fnc == 2:
        input_words()
    if fnc == 3:
        count_words()
    if fnc == 4:
        height_words()
    if fnc == 5:
        print("Adios")
        exit()


user_interface()
