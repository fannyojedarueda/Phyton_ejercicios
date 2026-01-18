"""Demostración de operaciones con listas"""

def demo():
    items = ['manzana', 'banana', 'cereza']
    print('Inicial:', items)

    items.append('durazno')
    print('Después append:', items)

    items.insert(1, 'kiwi')
    print('Después insert:', items)

    items.remove('banana')
    print('Después remove banana:', items)

    sliced = items[1:3]
    print('Sliced (1:3):', sliced)


if __name__ == "__main__":
    demo()
