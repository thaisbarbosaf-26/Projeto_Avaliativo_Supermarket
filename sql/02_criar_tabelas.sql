# Criando tabelas vendas_raw e vendas_with_constraints 

SELECT * FROM vendas_raw


CREATE TABLE public.vendas_with_constraints (
    id_venda VARCHAR(50) PRIMARY KEY NOT NULL,
    Filial VARCHAR(10) NOT NULL,
    Cidade VARCHAR(100) NOT NULL,
    tipo_cliente VARCHAR(50),
    Genero VARCHAR(20),
    linha_produto VARCHAR(150) NOT NULL,
    preco_unitario NUMERIC(10,2) CHECK (preco_unitario >= 0),
    Quantidade INTEGER CHECK (Quantidade > 0),
    Imposto NUMERIC(10,2) CHECK (Imposto >= 0),
    valor_total NUMERIC(12,2) CHECK (valor_total >= 0),
    data_venda DATE,
    hora_venda TIME,
    forma_pagamento VARCHAR(50) NOT NULL,
    custo_mercadoria NUMERIC(12,2) CHECK (custo_mercadoria >= 0),
    margem_percentual NUMERIC(10,2),
    receita_bruta NUMERIC(12,2) CHECK (receita_bruta >= 0),
    Avaliacao NUMERIC(4,2) CHECK (Avaliacao >= 0 AND Avaliacao <= 10)
);



INSERT INTO public.vendas_with_constraints (
    id_venda,
    Filial,
    Cidade,
    tipo_cliente,
    Genero,
    linha_produto,
    preco_unitario,
    Quantidade,
    Imposto,
    valor_total,
    data_venda,
    hora_venda,
    forma_pagamento,
    custo_mercadoria,
    margem_percentual,
    receita_bruta,
    Avaliacao
)
SELECT 
    "Invoice ID",
    "Branch",
    "City",
    "Customer type",
    "Gender",
    "Product line",
    "Unit price",
    "Quantity",
    "Tax 5%",
    "Sales",
    TO_DATE("Date", 'MM/DD/YYYY'),
    "Time"::TIME,
    "Payment",
    "cogs",
    "gross margin percentage",
    "gross income",
    "Rating"
FROM public.vendas_raw;
