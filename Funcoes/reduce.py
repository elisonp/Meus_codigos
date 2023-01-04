""""
A função Reduce recebe uma função e uma sequência de elementos,
retornando uma lista com o resultado obtido dos elementos 
que foram passados como parâmetro para função.

Só que ao contrário da MAP ela soma cada posição até o último
elemento.
Exemplo: 
[0] = 47 [1] = 11 -> 58
58 + [2] = 42 -> 100
100 + [3] = 13 -> 113
"""
from functools import reduce


lst = [47,10,154,21]

# Adição

def soma(a,b):
    x = a + b
    return x

print(reduce(soma, lst))

# Subtração

def sub(a,b):
    x = a - b
    return x

print(reduce(sub, lst))


# função lambda com condicinal e utilizando o reduce
max_find = lambda a,b: a if (a>b) else b

print(reduce(max_find, lst))