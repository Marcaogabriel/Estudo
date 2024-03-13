#lanche [3] = o Mudou
#lanche.append = adicionar ao final
#lanche.insert(no local 0, pão)
# maneiras de excluir: 1 del lanche [3]  /  2 lanche.pop(3)  /  3 lanche.remove('Pizza')
lista = [0, 1, 2, 3, 4]
lista.append(7)
lista[4] = 6
lista.insert(4, 5)
lista.pop(1)
lista.pop(0)
lista.append(4)
lista.sort(reverse=True)
print(lista)
print(f'A lista tem {len(lista)} elementos')
