# Importando bibliotecas

import os
from dotenv import load_dotenv # carrega a variável informada em .env
from sqlalchemy import create_engine

import pandas as pd


# Criando conexão com o banco de dados supermarket
load_dotenv()
 
CONN_URL = os.getenv("CONN_URL")
engine = create_engine(CONN_URL)

print("Conexão realizada com sucesso!!")

      


# Leitura das tabelas de negócio geradas no PostgreSQL

df_tab_avaliacao_media_linha_produto = pd.read_sql_table('tab_avaliacao_media_linha_produto', engine)
df_tab_faturamento_filial = pd.read_sql_table('tab_faturamento_filial', engine)
df_tab_faturamento_linha_produto = pd.read_sql_table('tab_faturamento_linha_produto', engine)
df_tab_forma_pagamento_mais_utilizada = pd.read_sql_table('tab_forma_pagamento_mais_utilizada', engine)
df_tab_maior_venda = pd.read_sql_table('tab_maior_venda', engine)
df_tab_qntd_vendas_por_dia_semana = pd.read_sql_table('tab_qntd_vendas_por_dia_semana', engine)
df_tab_qntd_vendas_filial = pd.read_sql_table('tab_qntd_vendas_filial', engine)
df_tab_valor_medio_venda = pd.read_sql_table('tab_valor_medio_venda', engine)


# Exportação das tabelas tratadas para arquivos CSV, conforme leitura acima

df_tab_avaliacao_media_linha_produto.to_csv(r'data\processed\avaliacao_media_linha_produto.csv', index=False, encoding="utf-8")
df_tab_faturamento_filial.to_csv(r'data\processed\faturamento_filial.csv', index=False, encoding="utf-8")
df_tab_faturamento_linha_produto.to_csv(r'data\processed\faturamento_linha_produto.csv', index=False, encoding="utf-8")
df_tab_forma_pagamento_mais_utilizada.to_csv(r'data\processed\forma_pagamento_mais_utilizada.csv', index=False, encoding="utf-8")
df_tab_maior_venda.to_csv(r'data\processed\maior_venda.csv', index=False, encoding="utf-8")
df_tab_qntd_vendas_por_dia_semana.to_csv(r'data\processed\qntd_vendas_por_dia_semana.csv', index=False, encoding="utf-8")
df_tab_qntd_vendas_filial.to_csv(r'data\processed\qntd_vendas_por_filial.csv', index=False, encoding="utf-8")
df_tab_valor_medio_venda.to_csv(r'data\processed\valor_medio_venda.csv', index=False, encoding="utf-8")


total_registros = sum([
    len(df_tab_avaliacao_media_linha_produto),
    len(df_tab_faturamento_filial),
    len(df_tab_faturamento_linha_produto),
    len(df_tab_forma_pagamento_mais_utilizada),
    len(df_tab_maior_venda),
    len(df_tab_qntd_vendas_por_dia_semana),
    len(df_tab_qntd_vendas_filial),
    len(df_tab_valor_medio_venda)
])


print(f"Dados gerados com sucesso! Total de registros: {total_registros}")


# Encerrando a conexão com o banco de dados
engine.dispose()




