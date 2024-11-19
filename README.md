# 🛠️ Construção de ETL Otimizado com PySpark

## Apache Spark

O Apache Spark é uma plataforma de processamento de dados em grande escala e oferece ferramentas poderosas para processar grandes volumes de dados de forma distribuída e eficiente.
O **PySpark é uma interface em Python para o Apache Spark** e permite que você utilize toda a funcionalidade do Spark, como **processamento de dados em batch e streaming, machine learning (MLlib), SQL e muito mais**.

## Vantagens do PySpark

- **Escalabilidade:** Pode processar grandes volumes de dados, distribuindo tarefas entre múltiplas máquinas.
- **Velocidade:** Em comparação com outras tecnologias de processamento, o Spark pode ser muito mais rápido devido à sua arquitetura em memória.
- **Flexibilidade:** Oferece APIs para processamento de dados em batch, SQL e machine learning.
- **Suporte a SQL:** Utiliza o Spark SQL para consultas SQL, o que facilita a integração com outras ferramentas.

---

## Construindo ETL em PySpark

Quando falamos de ETL (Extract, Transform, Load) com PySpark, o objetivo é construir pipelines eficientes que extraem dados de fontes, fazem transformações e os carregam para o destino.
O processo pode ser feito utilizando **Spark DataFrames** (estrutura de dados imutável e distribuída que suporta operações em grandes volumes de dados) e **Spark SQL** para transformar os dados de forma otimizada.

## Diretrizes para otimizar o processo de ETL usando PySpark:

### 1. Extração (Extract)

Na fase de extração, os dados podem vir de diferentes fontes, como arquivos CSV, bancos de dados SQL, NoSQL, etc. No PySpark, a extração é realizada através da leitura de arquivos ou conexões com fontes externas.

### 2. Transformação (Transform)

As transformações no PySpark são feitas com a API de DataFrame ou com SQL. O Spark permite operações como filtro, agregação, junção e ordenação de dados de forma distribuída e eficiente.

- **Filtros e seleções:** Filtrar e selecionar colunas específicas.
- **Agregação e agregações avançadas:** Como contagem, soma e médias.
- **Junções (Joins):** O Spark é otimizado para junções distribuídas.
- **Manipulações de dados:** Como adicionar novas colunas ou transformar dados.

### 3. Carregamento (Load)

A carga dos dados no destino pode ser feita de várias formas, incluindo salvar no HDFS, S3, em bancos de dados, etc.

### 4. Otimizações em PySpark

- **Uso de Parquet:** O formato Parquet é altamente otimizado para grandes volumes de dados e tem compressão eficiente. Quando possível, preferir trabalhar com esse formato ao invés de CSV.
- **Persistência:** Se você realizar múltiplas operações em um DataFrame, você pode persistir ele na memória para evitar reprocessamentos desnecessários.
- **Particionamento:** Dividir o DataFrame em partições para otimizar a leitura e escrita de dados.
- **Reparticionamento:** Antes de operações como agregações e joins, o reparticionamento pode melhorar a performance.
- **Filtragem de dados antes de transformação:** Evite carregar dados desnecessários. Aplique filtros e projeções (seleção de colunas) o mais cedo possível no pipeline.
- **Broadcast Join:** Se você está fazendo um join entre uma grande tabela e uma pequena tabela, você pode usar broadcast para a tabela pequena, o que pode melhorar a performance.
- **Persistência em disco:** Quando os dados são grandes e você não quer que a memória se esgote, use disk para persistir dados intermediários.

### 5. Uso de PySpark SQL

A utilização de SQL em PySpark é poderosa e pode ser feita tanto através da API SQL do PySpark quanto através da execução de queries SQL diretamente no SparkSession.

---

## Para construir ETL's otimizados em PySpark:

- **Aproveite o formato de dados Parquet.**
- **Utilize caching e persistência para dados intermediários.**
- **Particione seus dados para otimizar leitura e escrita.**
- **Execute transformações como joins e agregações com operações distribuídas e broadcast quando necessário.**

## Especificação Técnica

- **IDE:** VSCode (Visual Studio Code)
- **Linguagem:** Python
  - **Bibliotecas (principais):** pip install pyspark mysql-connector-python pandas

---

## 🚀 Configuração e Execução

### 1. Criar o Ambiente Virtual

- **1.1. Abra o terminal ou o PowerShell no Windows.**

- **1.2. Navegue até o diretório base do projeto:**
  cd D:\GitHub\etl-pyspark

- **1.3. Crie o ambiente virtual:**
  python -m venv venv

- **1.4. Ative o ambiente virtual:**
  venv\Scripts\activate

### 2. Instalar as Dependências

- **2.1. Instale as dependências do arquivo requirements.txt existente**
  pip install -r requirements.txt

- **2.2. OU CASO exclua o arquivo requirements.txt existente:**
  - **2.2.1. Primeiro: Instale as dependências necessárias com pip:**
    pip install pandas beautifulsoup4 lxml selenium webdriver-manager
  - **2.2.2. Segundo: Gere arquivo requirements.txt**
    pip freeze > requirements.txt

### 3. Executar o Script

- **3.1. Navegue até o diretório onde está o script:**
  cd D:\GitHub\etl-pyspark

- **3.2. Execute o script com o Python:**
  python etl-otimizado.py

### 4. Manutenção do Ambiente

- **4.1. Para Desativar o Ambiente:**
  **Quando terminar de usar o ambiente virtual, você pode desativá-lo com o comando:**
  deactivate

- **4.2. Para Reativar o Ambiente:**
  **Sempre que quiser executar novamente, reative o ambiente com:**
  venv\Scripts\activate
