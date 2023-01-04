""""
A função MAP recebe uma função e uma sequência de elementos,
retornando uma lista com o resultado obtido dos elementos 
que foram passados como parâmetro para função.
"""

def fahrenheit(T):
    return ((float(9)/5)*T + 32)

def celsius(T):
    return ((float(5)/9)*(T - 32))

temperaturas = 0, 22.5, 40, 100

# print(list(map(fahrenheit, temperaturas)))

for temp in map(fahrenheit, temperaturas):
    print(temp)

print(
    list(
        map(
            lambda x: (5.0/9)*(x-32), temperaturas
        )
    )
)