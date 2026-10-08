import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Carregamento da base tratada da camada processed
caminho_tratado = r"data/processed/vendas_tratadas.csv"
df = pd.read_csv(caminho_tratado)

print("\n" + "=" * 120)
print("                              RESPOSTAS DE NEGÓCIO")
print("=" * 120)


# --- Filial com maior faturamento ---
faturamento_filial = df.groupby('Filial')['valor_total'].sum().sort_values(ascending=False) #sort_values ordena os dados numéricos ou alfabéticos
top_filial_fat = faturamento_filial.index[0]
val_filial_fat = faturamento_filial.iloc[0]
print(f"\n1) A filial com maior faturamento foi: \033[1m{top_filial_fat.upper()}\033[0m com R$ \033[1m{val_filial_fat:,.2f}\033[0m.")

# --- Filial com maior quantidade de vendas ---
qtd_vendas_filial = df['Filial'].value_counts() #conta e ordena o valor único de cada filial
top_filial_qtd = qtd_vendas_filial.index[0]
val_filial_qtd = qtd_vendas_filial.iloc[0]
print(f"\n2) A filial com maior quantidade de vendas foi: \033[1m{top_filial_qtd.upper()}\033[0m com \033[1m{val_filial_qtd}\033[0m vendas registradas.")

# --- Linha de produto com maior faturamento ---
fat_linha = df.groupby('linha_produto')['valor_total'].sum().sort_values(ascending=False)
top_linha_fat = fat_linha.index[0]
val_linha_fat = fat_linha.iloc[0]
print(f"\n3) A linha de produto com maior faturamento foi: \033[1m{top_linha_fat.upper()}\033[0m com R$ \033[1m{val_linha_fat:,.2f}\033[0m.")

# --- Linha de produto com melhor avaliação média ---
avaliacao_linha = df.groupby('linha_produto')['Avaliacao'].mean().sort_values(ascending=False)
top_linha_aval = avaliacao_linha.index[0]
val_linha_aval = avaliacao_linha.iloc[0]
print(f"\n4) O produto com melhor avaliação média foi: \033[1m{top_linha_aval.upper()}\033[0m com nota média de: \033[1m{val_linha_aval:.2f}\033[0m.")

# --- Forma de pagamento mais utilizada ---
pagamento_mais_usado = df['forma_pagamento'].value_counts()
top_pagamento = pagamento_mais_usado.index[0]
val_pagamento = pagamento_mais_usado.iloc[0]
print(f"\n5) A forma de pagamento mais utilizada foi: \033[1m{top_pagamento.upper()}\033[0m com \033[1m{val_pagamento}\033[0m utilizações.")

# --- Valor médio das vendas ---
valor_medio = df['valor_total'].mean()
print(f"\n6) O valor médio das vendas foi de: R$ \033[1m{valor_medio:,.2f}\033[0m.")

# --- Maior venda registrada ---
maior_venda = df['valor_total'].max()
print(f"\n7) A maior venda única registrada foi de: R$ \033[1m{maior_venda:,.2f}\033[0m.")

# --- Dia da semana com maior quantidade de vendas ---
vendas_dia_semana = df['dia_semana'].value_counts()
top_dia = vendas_dia_semana.index[0]
val_dia = vendas_dia_semana.iloc[0]
print(f"\n8) O dia da semana com maior quantidade de vendas foi: \033[1m{top_dia.upper()}\033[0m com \033[1m{val_dia}\033[0m vendas.")


# Gerando e salvando o arquivo Markdown (.md) na pasta resultados/
caminho_md_resultados = "resultados/respostas_negocio.md"

with open(caminho_md_resultados, "w", encoding="utf-8") as f:
    f.write("# Respostas de Negócio\n\n")
    f.write(f"1. A filial com maior faturamento foi: **{top_filial_fat.upper()}** com R$ **{val_filial_fat:,.2f}**.\n")
    f.write(f"2. A filial com maior quantidade de vendas foi: **{top_filial_qtd.upper()}** com **{val_filial_qtd}** vendas registradas.\n")
    f.write(f"3. A linha de produto com maior faturamento foi: **{top_linha_fat.upper()}** com R$ **{val_linha_fat:,.2f}**.\n")
    f.write(f"4. O produto com melhor avaliação média foi: **{top_linha_aval.upper()}** com nota média de **{val_linha_aval:.2f}**.\n")
    f.write(f"5. A forma de pagamento mais utilizada foi: **{top_pagamento.upper()}** com **{val_pagamento}** utilizações.\n")
    f.write(f"6. O valor médio das vendas foi de: R$ **{valor_medio:,.2f}**.\n")
    f.write(f"7. A maior venda única registrada foi de: R$ **{maior_venda:,.2f}**.\n")
    f.write(f"8. O dia da semana com maior quantidade de vendas foi: **{top_dia.upper()}** com **{val_dia}** vendas.\n")

print(f"\n\n[OK] - Respostas de negócio - GERADO COM SUCESSO!\n")


#################################################################################################################################


print("\n" + "=" * 120)
print("                              ESTATÍSTICA DESCRITIVA")
print("=" * 120 + "\n")

# Selecionando colunas para verificar estatísticas descritivas
colunas_metricas = ['preco_unitario', 'Quantidade', 'Imposto', 'valor_total', 'custo_mercadoria', 'receita_bruta', 'Avaliacao']

estatistica_descritiva = df[colunas_metricas].describe().round(2)
print(estatistica_descritiva)

# Gerando e salvando o arquivo CSV na pasta resultados/
caminho_csv_resultados = "resultados/relatorio_estatistico.csv"
estatistica_descritiva.to_csv(caminho_csv_resultados, encoding="utf-8")
print(f"\n\n[OK] - Estatística descritiva - GERADO COM SUCESSO!")


print("\n" + "=" * 120 + "\n")


#################################################################################################################################


print("\n" + "=" * 120)
print("                              GRÁFICOS")
print("=" * 120 + "\n")

sns.set_theme(style="whitegrid")

# Gráfico 1: Faturamento por Filial
plt.figure(figsize=(8, 5))
sns.barplot(x=faturamento_filial.index, y=faturamento_filial.values, palette="Blues_d")
plt.title("Faturamento Total por Filial (R$)", fontsize=14, fontweight='bold')
plt.xlabel("Filial")
plt.ylabel("Faturamento (R$)")
plt.tight_layout()
plt.savefig("resultados/grafico_faturamento_filial.png", dpi=300)
plt.close()

# Gráfico 2: Vendas por Dia da Semana
plt.figure(figsize=(9, 5))
ordem_dias = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
sns.countplot(data=df, x='dia_semana', order=ordem_dias, palette="viridis")
plt.title("Quantidade de Vendas por Dia da Semana", fontsize=14, fontweight='bold')
plt.xlabel("Dia da Semana")
plt.ylabel("Quantidade de Vendas")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("resultados/grafico_vendas_dia_semana.png", dpi=300)
plt.close()

# Gráfico 3: Faturamento por Linha de Produto
plt.figure(figsize=(10, 5))
sns.barplot(x=fat_linha.values, y=fat_linha.index, palette="magma")
plt.title("Faturamento Total por Linha de Produto (R$)", fontsize=14, fontweight='bold')
plt.xlabel("Faturamento (R$)")
plt.ylabel("Linha de Produto")
plt.tight_layout()
plt.savefig("resultados/grafico_faturamento_linha_produto.png", dpi=300)
plt.close()

# Gráfico 4: Formas de Pagamento (Gráfico de Rosca)
plt.figure(figsize=(7, 7))
pagamento_counts = df['forma_pagamento'].value_counts()
plt.pie(
    pagamento_counts.values, 
    labels=pagamento_counts.index, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=sns.color_palette("Set2"),
    wedgeprops=dict(width=0.4, edgecolor='w')
)
plt.title("Proporção das Formas de Pagamento Utilizadas", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig("resultados/grafico_formas_pagamento.png", dpi=300)
plt.close()

print("\n\n[OK] - Gráficos - GERADOS COM SUCESSO!")
print("\n" + "=" * 120)

