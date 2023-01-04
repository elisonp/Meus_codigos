lst= [x for x in range(0,11)]

print(lst)


# Raiz quadrada e um range de números , retornar uma lista

rqd = [x**2 for x in range(0,20)]

print(rqd)

# Retorna valores pares

par = [x for x in range(20) if x%2 ==0]

print(par)

# Operação aninhada

lst = [x**2 for x in [x**2 for x in range(10)]]
print(lst)
