'''
--- Dimensão dos dados ---
(1000, 17)


--- Informações da estrutura do DataFrame ---
 #   Column                   Non-Null Count  Dtype  
---  ------                   --------------  -----  
 0   Invoice ID               1000 non-null   str    
 1   Branch                   1000 non-null   str    
 2   City                     1000 non-null   str    
 3   Customer type            1000 non-null   str    
 4   Gender                   1000 non-null   str    
 5   Product line             1000 non-null   str    
 6   Unit price               1000 non-null   float64
 7   Quantity                 1000 non-null   int64  
 8   Tax 5%                   1000 non-null   float64
 9   Sales                    1000 non-null   float64
 10  Date                     1000 non-null   str    
 11  Time                     1000 non-null   str    
 12  Payment                  1000 non-null   str    
 13  cogs                     1000 non-null   float64
 14  gross margin percentage  1000 non-null   float64
 15  gross income             1000 non-null   float64
 16  Rating                   1000 non-null   float64


'''

import pandas as pd

# ETAPA - Leitura e inspeção inicial do CSV no pandas:

# Leitura do arquivo que será analisado
caminho_csv = r"data/raw/vendas_raw_01.csv" 
df_vendas = pd.read_csv(caminho_csv, sep=",", encoding="utf-8")


# Dimensão dos dados (linhas, colunas)
print("\n--- Dimensão dos dados ---")
print(df_vendas.shape)

# Visualizando as primeiras 10 linhas do arquivo CSV
print("\n--- Primeiras 10 linhas do arquivo ---")
print(df_vendas.head(10))

# Visualizando os nomes das colunas
print("\n--- Nomes das Colunas ---")
print(df_vendas.columns.tolist()) 

# Verificando os tipos de dados existentes
print("\n--- Informações da estrutura do DataFrame ---")
print(df_vendas.info())

# Verificando valores ausentes
print("\n--- Quantidade de valores ausentes por coluna ---")
print(df_vendas.isnull().sum())

# Verificando linhas duplicadas
print(f"\n---Quantidade de linhas duplicadas: {df_vendas.duplicated().sum()} ---")

# Estatísticas gerais
print("\n--- Resumo Estatístico ---")
print(df_vendas.describe())

