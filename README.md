
# 🛒 Projeto Avaliativo - Análise de Vendas Supermarket

Este projeto apresenta uma análise de uma base de dados de vendas de um supermercado ( **Supermarket Sales** ), contemplando etapas de leitura, tratamento, análise estatística, geração de resultados e utilização de banco de dados PostgreSQL.

A base de dados utilizada foi extraída do Kaggle:

**Fonte:** [Supermarket Sales - Kaggle](https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales)

O projeto foi desenvolvido por  **Thais Barbosa** , durante o curso  **SC TEC - Análise de Dados Python / SQL** , como parte da avaliação proposta no  **Módulo 1** .

---

## 📁 Arquitetura do Repositório

```
ProjetoAvaliativo_ThaisBarbosa_T4/
│
├── data/
│   ├── raw/                            # Dados brutos recebidos
│   └── processed/                      # Dados processados, consultas SQL e exportações CSV
│       └── vendas_tratadas.csv
│
├── sql/                                # Scripts de banco de dados PostgreSQL
│   ├── 01_criar_bco_dados.sql          # Script de criação da base de dados
│   ├── 02_criar_tabelas.sql            # DDL das tabelas e restrições
│   └── 03_consultas.sql                # Consultas e validações analíticas em SQL
│
├── src/                                # Códigos-fonte da pipeline em Python
│   ├── 01_leitura_dados.py             # Inspeção e validação inicial das bases
│   ├── 02_etl_vendas.py                # Tratamento e limpeza dos dados
│   ├── 03_estatistica.py               # Análise estatística, respostas de negócio e gráficos
│   ├── conexao.py                      # Conexão com PostgreSQL (SQLAlchemy + dotenv)
│   ├── extracao.py                     # Script de extração e suporte de dados
│   ├── load_tabela_consultas.py        # Carga dos dados tratados no banco de dados
│   └── load_tabela_withconstraints.py  # Carga com aplicação de restrições relacionais
│
├── resultados/                         # Resultados das análises
│   ├── relatorio_estatistico.csv       # Estatística descritiva das variáveis numéricas
│   ├── respostas_negocio.md            # Respostas às perguntas de negócio
│   ├── grafico_faturamento_filial.png
│   ├── grafico_faturamento_linha_produto.png
│   ├── grafico_formas_pagamento.png
│   └── grafico_vendas_dia_semana.png
│
├── .env.example                        # Modelo para variáveis de ambiente (credenciais)
├── .gitignore                           # Proteção de arquivos sensíveis e temporários
├── requirements.txt                     # Dependências do projeto Python
└── README.md                            # Documentação do projeto
```

---

## 📊 Principais Respostas de Negócio

A análise dos dados permitiu responder questões relacionadas ao desempenho das vendas, comportamento dos clientes e características do faturamento.

Entre os principais resultados, destacam-se:

* **Filial Campeã de Faturamento:** apresentação da filial com maior volume de faturamento bruto.
* **Filial Líder em Transações:** identificação da unidade com maior quantidade de vendas.
* **Linha de Produto Mais Rentável:** identificação da categoria de produto com maior faturamento.
* **Avaliação dos Clientes:** identificação da linha de produto com melhor nota média de satisfação.
* **Comportamento de Pagamento:** identificação da forma de pagamento mais utilizada.
* **Métricas Financeiras:** cálculo do ticket médio e identificação da maior transação registrada.
* **Sazonalidade Semanal:** identificação do dia da semana com maior volume de vendas.

Os resultados detalhados estão disponíveis na pasta `resultados/`, incluindo os relatórios estatísticos, respostas de negócio e gráficos gerados durante a análise.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.11+** — desenvolvimento da análise e pipeline de dados.
* **Pandas** — manipulação e tratamento dos dados.
* **Matplotlib** — criação dos gráficos.
* **Seaborn** — visualização e análise gráfica.
* **PostgreSQL** — armazenamento e consultas dos dados.
* **SQLAlchemy** — integração entre Python e PostgreSQL.
* **psycopg2-binary** — conexão com PostgreSQL.
* **python-dotenv** — gerenciamento das variáveis de ambiente.

---

## ▶️ Execução do Projeto

Para executar o projeto, é necessário ter **Python 3.11+** e **PostgreSQL** instalados.

### Instalação das dependências

```
pip install -r requirements.txt
```

### Configuração do banco de dados

Utilize o arquivo `.env.example` como modelo para criar o arquivo `.env` na raiz do projeto, preenchendo as informações de acesso ao PostgreSQL.

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=supermarket_db
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
```

Os scripts SQL disponíveis na pasta `sql/` podem ser utilizados para criação da base, tabelas e execução das consultas.

Os scripts Python da pasta `src/` realizam as etapas de leitura, tratamento, análise e carga dos dados.

---

## 📈 Resultados

Os principais resultados do projeto estão disponíveis na pasta `resultados/`, contendo:

* Relatório estatístico das variáveis numéricas;
* Respostas das perguntas de negócio;
* Gráficos de faturamento por filial;
* Gráficos de faturamento por linha de produto;
* Distribuição das formas de pagamento;
* Vendas por dia da semana.

Dessa forma, o projeto apresenta o processo de tratamento e análise dos dados, as tecnologias utilizadas e os resultados obtidos a partir da base  **Supermarket Sales** .

---

**Projeto desenvolvido por Thais Barbosa**
**Curso: SC TEC - Análise de Dados Python / SQL**
**Avaliação - Módulo 1**
