-- Criando tabelas para responder as perguntas de negócio:


-- Qual filial apresentou o maior faturamento?

CREATE TABLE tab_faturamento_filial AS
SELECT filial,
    SUM(valor_total) AS faturamento_total
FROM vendas_with_constraints
GROUP BY filial
ORDER BY faturamento_total DESC;


-- Qual filial realizou a maior quantidade de vendas?

CREATE TABLE tab_quantidade_vendas_filial AS
SELECT filial,
    COUNT(id_venda) AS quantidade_vendas,
    SUM(quantidade) AS total_itens_vendidos
FROM vendas_with_constraints
GROUP BY filial
ORDER BY quantidade_vendas DESC;


-- Qual linha de produto apresentou o maior faturamento?

CREATE TABLE tab_faturamento_linha_produto AS
SELECT linha_produto,
    SUM(valor_total) AS faturamento_total
FROM vendas_with_constraints
GROUP BY linha_produto
ORDER BY faturamento_total DESC;


-- Qual linha de produto recebeu a melhor avaliação média?

CREATE TABLE tab_avaliacao_media_linha_produto AS
SELECT linha_produto,
    AVG(avaliacao) AS avaliacao_media
FROM vendas_with_constraints
GROUP BY linha_produto
ORDER BY avaliacao_media DESC;


-- Qual foi a forma de pagamento mais utilizada?

CREATE TABLE tab_forma_pagamento_mais_utilizada AS
SELECT forma_pagamento,
    COUNT(id_venda) AS tipo_forma_pgto_total
FROM vendas_with_constraints
GROUP BY forma_pagamento
ORDER BY tipo_forma_pgto_total DESC;


-- Qual foi o valor médio das vendas?

CREATE TABLE tab_valor_medio_venda AS
SELECT 
    AVG(valor_total) AS valor_medio_venda
FROM vendas_with_constraints;


-- Qual foi a maior venda registrada?

CREATE TABLE tab_maior_venda AS
SELECT 
    id_venda,
    filial,
    cidade,
    linha_produto,
    valor_total,
    data_venda
FROM vendas_with_constraints
ORDER BY valor_total DESC
LIMIT 1;


-- Em qual dia da semana ocorreu a maior quantidade de vendas?

CREATE TABLE tab_qntd_vendas_por_dia_semana AS
SELECT 
    TO_CHAR(data_venda, 'Day') AS dia_semana,
    COUNT(id_venda) AS total_vendas
FROM vendas_with_constraints
GROUP BY dia_semana
ORDER BY total_vendas DESC;