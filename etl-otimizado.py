## INSTALAR BILBIOTECAS 
#pip install pyspark mysql-connector-python pandas

## INICIAR SESSÃO SPARK
# exemplos MySQL e Postgresql

from pyspark.sql import SparkSession
#spark = SparkSession.builder.appName("ETL Example").getOrCreate()
''' Certifique-se de que o JAR do driver MySQL está acessível no caminho especificado 
#e que as credenciais e a URL estão corretas para a sua configuração do banco de dados.'''

# MySQL
spark = SparkSession.builder \
    .appName("ETL Example") \
    .config("spark.jars", "/path/to/mysql-<version>.jar") \  # Caminho para o jar do driver MySQL
    .getOrCreate()

#Postgresql
'''
spark = SparkSession.builder \
    .appName("ETL Example") \
    .config("spark.jars", "/path/to/postgresql-<version>.jar") \  # Caminho para o jar do driver PostgreSQL
    .getOrCreate()
'''

## EXTRACT
# Leitura de arquivos CSV
df_csv = spark.read.csv("path/to/file.csv", header=True, inferSchema=True)

# Leitura de banco de dados SQL (mysql)
df_sql = spark.read.format("jdbc").options(
    url="jdbc:mysql://localhost:3306/dbname",  # Altere para a URL do MySQL
    driver="com.mysql.jdbc.Driver",            # Altere para o driver do MySQL
    dbtable="table_name",
    user="username",
    password="password"
).load()

# Leitura de banco de dados SQL (postgresql
'''
df_sql = spark.read.format("jdbc").options(
    url="jdbc:postgresql://localhost:5432/dbname",  # Altere para a URL do PostgreSQL
    driver="org.postgresql.Driver",                 # Altere para o driver do PostgreSQL
    dbtable="table_name",
    user="username",
    password="password"
).load()
'''

## TRANSFORM
# Filtros e seleções: Filtrar e selecionar colunas específicas.
# Filtrar dados
df_filtered = df_csv.filter(df_csv['age'] > 30)

# Selecionar colunas
df_selected = df_csv.select('name', 'age', 'salary')

# Agregação e agregações avançadas: Como contagem, soma e médias.
from pyspark.sql import functions as F

# Agregação por grupo
df_aggregated = df_csv.groupBy("department").agg(F.avg("salary").alias("average_salary"))

# Junções (Joins): O Spark é otimizado para junções distribuídas.
df_joined = df_csv.join(df_sql, df_csv["id"] == df_sql["id"], "inner")

# Manipulações de dados: Como adicionar novas colunas ou transformar dados.
# Criar uma nova coluna
df_transformed = df_csv.withColumn('salary_increase', df_csv['salary'] * 1.1)


## LOAD
# Carregar para S3 (formato Parquet)
df_filtered.write.parquet("s3://bucket-name/path/", mode="overwrite")

# Carregar para um banco MySQL
df_transformed.write.format("jdbc").options(
    url="jdbc:mysql://localhost:3306/dbname",  # Altere para a URL do MySQL
    driver="com.mysql.jdbc.Driver",            # Altere para o driver do MySQL
    dbtable="output_table",
    user="username",
    password="password"
).mode("overwrite").save()

# Carregar para um banco PostgreSQL
'''
df_transformed.write.format("jdbc").options(
    url="jdbc:postgresql://localhost:5432/dbname",  # Altere para a URL do PostgreSQL
    driver="org.postgresql.Driver",                   # Altere para o driver do PostgreSQL
    dbtable="output_table",
    user="username",
    password="password"
).mode("overwrite").save()
'''

## 4. OTIMIZAÇÃO PYSPARK
# Uso de Parquet: Persistir DataFrame na memória caso seja utilizado em múltiplas operações para evitar reprocessamentos desnecessários.
df_cached = df_transformed.cache()

# Particionamento: Dividir o DataFrame em partições para otimizar a leitura e escrita de dados.
df_transformed.write.partitionBy("year").parquet("s3://bucket-name/path/")

# Reparticionamento: Antes de operações como agregações e joins, o reparticionamento pode melhorar a performance.
df_repartitioned = df_transformed.repartition(10)

''' # Filtragem de dados antes de transformação: Evite carregar dados desnecessários. 
# Aplique filtros e projeções (seleção de colunas) o mais cedo possível no pipeline.
# Broadcast Join: Se você está fazendo um join entre uma grande tabela e uma pequena tabela, 
# você pode usar broadcast para a tabela pequena, o que pode melhorar a performance.
'''
from pyspark.sql.functions import broadcast

df_joined = df_large.join(broadcast(df_small), "id")

'''# Persistência em disco: Quando os dados são grandes e você não quer que a memória se esgote, 
use disk para persistir dados intermediários.'''
df_repartitioned.write.mode("overwrite").parquet("s3://bucket-name/path/")

# Registrando DataFrame como tabela temporária
df_csv.createOrReplaceTempView("df_table")

## 5. USO DE PYSPARK SQL
'''# A utilização de SQL em PySpark é poderosa e pode ser feita tanto através da API SQL do PySpark 
quanto através da execução de queries SQL diretamente no SparkSession.'''

# Registrando DataFrame como tabela temporária
df_csv.createOrReplaceTempView("df_table")

# Executando query SQL
df_sql_query = spark.sql("SELECT department, AVG(salary) FROM df_table GROUP BY department")
