import pandas as pd
# import pyspark

pessoas_df = pd.DataFrame([
    {"nome":"Pedro", "idade": 15},
    {"nome":"João", "idade":30},
    {"nome":"Maria", "idade":19},
    {"nome":"Marcelo", "idade":18},
    {"nome":"Alex", "idade":38},
    {"nome":"Otavio", "idade":44},
    {"nome":"Ricardo", "idade":23},
    {"nome":"Camila", "idade":12},
    {"nome":"Alice", "idade":24},
    {"nome":"Marlei", "idade":32},
    {"nome":"Marilene", "idade":56},
    {"nome":"Judite", "idade":60},
])

print(pessoas_df)

pessoas_df.to_parquet("C:\Project\Meus_codigos\Spark\\files\pessoas.pq")

parquet_df = pd.read_parquet("C:\Project\Meus_codigos\Spark\\files\pessoa'  s.pq")

print(parquet_df)