import pandas as pd
from functools import reduce
df1 = pd.DataFrame([
    {"nome":"Ricardo", "idade":23},
    {"nome":"Camila", "idade":12},
    {"nome":"Alice", "idade":24},
    {"nome":"Marlei", "idade":32},
    {"nome":"Marilene", "idade":56},
    {"nome":"Judite", "idade":60},
])

df2 = pd.DataFrame([
    {"nome":"Pedro", "idade": 15},
    {"nome":"João", "idade":30},
    {"nome":"Maria", "idade":19},
    {"nome":"Marcelo", "idade":18},
    {"nome":"Alex", "idade":38},
    {"nome":"Otavio", "idade":44},
])

lista_df = [df1,df2]
        
func1 = lambda x,y: x.append(y)
dataframe_full = reduce(func1, lista_df)

print(dataframe_full.value_counts)
print(dataframe_full)


