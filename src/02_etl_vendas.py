'''
--- Dimensão dos dados ---
(1000, 19)


--- Informações da estrutura do DataFrame ---
Data columns (total 19 columns):
 #   Column             Non-Null Count  Dtype    
---  ------             --------------  -----    
 0   id_venda           1000 non-null   str      
 1   Filial             1000 non-null   str      
 2   Cidade             1000 non-null   str      
 3   tipo_cliente       1000 non-null   str      
 4   Gênero             1000 non-null   str      
 5   linha_produto      1000 non-null   str      
 6   preco_unitario     1000 non-null   float64  
 7   Quantidade         1000 non-null   int64    
 8   Imposto            1000 non-null   float64  
 9   valor_total        1000 non-null   float64  
 10  data_venda         1000 non-null   object   
 11  hora_venda         1000 non-null   object   
 12  forma_pagamento    1000 non-null   str      
 13  custo_mercadoria   1000 non-null   float64  
 14  margem_percentual  1000 non-null   float64  
 15  receita_bruta      1000 non-null   float64  
 16  Avaliacao          1000 non-null   float64  
 17  dia_semana         1000 non-null   str      
 18  ano_mes            1000 non-null   period[M]
dtypes: float64(7), int64(1), object(2), period[M](1), str(8)
memory usage: 148.6+ KB

'''

import pandas as pd

# ETAPA - Limpeza, tipagem, tratamento de nulos e colunas derivadas:

# Leitura do arquivo que será analisado
caminho_csv = r"data/raw/vendas_raw_01.csv" 
df_vendas = pd.read_csv(caminho_csv, sep=",", encoding="utf-8")

# Padronizando e renomeando as colunas
atualizando_colunas = {
    'Invoice ID': 'id_venda',
    'Branch': 'Filial',
    'City': 'Cidade',
    'Customer type': 'tipo_cliente',
    'Gender': 'Gênero',
    'Product line': 'linha_produto',
    'Unit price': 'preco_unitario',
    'Quantity': 'Quantidade',
    'Tax 5%': 'Imposto',
    'Sales': 'valor_total',
    'Date': 'data_venda',
    'Time': 'hora_venda',
    'Payment': 'forma_pagamento',
    'cogs': 'custo_mercadoria',
    'gross margin percentage': 'margem_percentual',
    'gross income': 'receita_bruta',
    'Rating': 'Avaliacao'
}

df_vendas = df_vendas.rename(columns=atualizando_colunas)


# Ajustando as casas decimais
colunas_financeiras = ['preco_unitario', 'Imposto', 'valor_total', 'custo_mercadoria', 'margem_percentual', 'receita_bruta', 'Avaliacao']
df_vendas[colunas_financeiras] = df_vendas[colunas_financeiras].round(2)

# Conversões de Tipo (Casting)
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])

# Convertendo coluna hora_venda para formato time
df_vendas['hora_venda'] = pd.to_datetime(df_vendas['hora_venda'], format='%I:%M:%S %p').dt.time


# CRIANDO COLUNAS DERIVADAS:

# Alterando o nome do dia da semana de inglês para português
dias_semana_pt = {
    'Monday': 'Segunda-feira',
    'Tuesday': 'Terça-feira',
    'Wednesday': 'Quarta-feira',
    'Thursday': 'Quinta-feira',
    'Friday': 'Sexta-feira',
    'Saturday': 'Sábado',
    'Sunday': 'Domingo'
}
df_vendas['dia_semana'] = df_vendas['data_venda'].dt.day_name().map(dias_semana_pt)


# Extraindo o mês e ano se necessário para análises futuras
df_vendas['ano_mes'] = df_vendas['data_venda'].dt.to_period('M')


# Convertendo coluna data_venda para formato date
df_vendas['data_venda'] = df_vendas['data_venda'].dt.date

# Tratamento de nulos/duplicadas (caso apareça algo futuramente)
df_vendas = df_vendas.drop_duplicates()


# Conferência após as transformações e limpeza dos dados
# Dimensão dos dados (linhas, colunas)
print("\n--- Dimensão dos dados transformados ---")
print(df_vendas.shape)

# Verificando os dados tratados
print("\n--- Estrutura das colunas transformadas ---")
print(df_vendas.dtypes)


# Salvando o csv processado

caminho_processed = r"data/processed/vendas_tratadas.csv"
df_vendas.to_csv(caminho_processed, index=False, sep=",", encoding="utf-8")

print(f"\nETL concluído com sucesso! Salvo em: {caminho_processed}\n")


