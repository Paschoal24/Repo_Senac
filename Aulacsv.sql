USE CARAMELO;

CREATE TABLE tb_clientes(
id INT PRIMARY KEY AUTO_INCREMENT,
nome_cliente VARCHAR(100),
data_nascimento DATE,
sexo VARCHAR(100),
email VARCHAR(100),
telefone VARCHAR(100),
cidade VARCHAR(50),
estado VARCHAR(2),
data_cadastro DATE);


CREATE TABLE tb_produtos(
id INT PRIMARY KEY AUTO_INCREMENT,
nome_produto VARCHAR(300),
categoria  VARCHAR(100),
subcategoria VARCHAR(100),
marca VARCHAR(100),
preco_unitario DECIMAL(10,2));


CREATE TABLE tb_vendas(
id_venda INT PRIMARY KEY,
data_venda DATE,
id_cliente INT,
id_produto INT,
quantidae INT,
forma_pagamento VARCHAR(40),
canal_vendas VARCHAR (40),
FOREIGN KEY (id_cliente) REFERENCES tb_clientes(id),
FOREIGN KEY (id_produto) REFERENCES tb_produtos(id));

SET GLOBAL local_infile = 1;

LOAD DATA INFILE '/Users/ana.paschoal/Downloads/tb_clientes.csv'
INTO TABLE tb_clientes
FIELDS TERMINATED BY','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/Users/ana.paschoal/Downloads/tb_produtos.csv'
INTO TABLE tb_produtos
FIELDS TERMINATED BY','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/Users/ana.paschoal/Downloads/tb_vendas.csv'
INTO TABLE tb_vendas
FIELDS TERMINATED BY','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

SELECT * FROM tb_clientes

SELECT * FROM tb_produtos

SELECT * FROM tb_vendas