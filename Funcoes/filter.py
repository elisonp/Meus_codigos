"""
A função filter recebe 2 argumentos, uma função e uma sequência.
Filtra todos os elementos de uma lista, para os quais a função retorne as variaveis que forem True.
"""

'''def Verificar_par(num):
    if num %2==0:
        return True
    else
        return False
'''
lst = [1, 2, 3, 4]

verificar_par = lambda x: True if (x %2==0) else  False

print(list(filter(verificar_par, lst)))


verificar_par2 = lambda x: (x %2==0)

print(list(filter(verificar_par2, lst)))


print(list(filter(lambda num: num > 8, lst)))