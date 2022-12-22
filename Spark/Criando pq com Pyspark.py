from pyspark.sql import SparkSession, Row


# Criaremos uma sessão com o Spark.
spark = SparkSession.builder.appName("demo-app").getOrCreate()


# Criaremos um DataFrame com dados a serem salvos.
'''pessoas_df = spark.createDataFrame([
    Row(nome="Pedro", idade=15),
    Row(nome="João", idade=30),
    Row(nome="Maria", idade=19),
    Row(nome="Marcelo", idade=18),
    Row(nome="Alex", idade=38),
    Row(nome="Otavio", idade=44),
    Row(nome="Ricardo", idade=23),
    Row(nome="Camila", idade=12),
    Row(nome="Alice", idade=24),
    Row(nome="Marlei", idade=32),
    Row(nome="Marilene", idade=56),
    Row(nome="Judite", idade=60),
])

print(pessoas_df.show)

pessoas_df.write.parquet("pessoas.parquet")'''
# Salvaremos o DataFrame como um arquivo Parquet.
# pessoas_df.write.parquet("C:\Project\Meus_codigos\Spark\\files\pessoas.parquet")
data =[("James ","","Smith","36636","M",3000),
              ("Michael ","Rose","","40288","M",4000),
              ("Robert ","","Williams","42114","M",4000),
              ("Maria ","Anne","Jones","39192","F",4000),
              ("Jen","Mary","Brown","","F",-1)]

columns=["firstname","middlename","lastname","dob","gender","salary"]

df = spark.createDataFrame(data,columns)

df.write.csv("C:\Project\Meus_codigos\people.csv")

'''Carregaremos o arquivo Parquet que acabamos de criar para 
efetuar algumas consultas, todas informações são preservadas.'''
# parquet_df = spark.read.parquet("C:\Project\Meus_codigos\Spark\\files\pessoas.parquet")