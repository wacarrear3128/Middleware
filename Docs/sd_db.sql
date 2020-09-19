DROP DATABASE sd_db;
CREATE DATABASE sd_db;
USE sd_db;

-- select User from mysql.user;
/*
CREATE USER 'us_cat' IDENTIFIED BY 'pass_cat';
CREATE USER 'us_alm' IDENTIFIED BY 'pass_alm';
CREATE USER 'us_fct' IDENTIFIED BY 'pass_fct';

GRANT ALL PRIVILEGES ON sd_db.tb_productos TO 'us_cat';
GRANT ALL PRIVILEGES ON sd_db.tb_productos TO 'us_cat'@'%' IDENTIFIED BY 'pass_cat';
*/

CREATE TABLE tb_clientes (
	id_cli INT(8) NOT NULL,
    nom_cli VARCHAR(50) NOT NULL,
    app_cli VARCHAR(50),
    apm_cli VARCHAR(50),
    PRIMARY KEY (id_cli)
);

CREATE TABLE tb_productos (
	id_prd INT(8) NOT NULL AUTO_INCREMENT,
    nom_prd VARCHAR(30) NOT NULL,
    dsc_prd VARCHAR(50),
    mrc_prd VARCHAR(30),
    prc_prd FLOAT NOT NULL,
    und_prd VARCHAR(5),
    PRIMARY KEY (id_prd)
);

CREATE TABLE tb_stock (
	FK_id_prd INT(8) NOT NULL,
    stock FLOAT,
    PRIMARY KEY (FK_id_prd),
    FOREIGN KEY (FK_id_prd) REFERENCES tb_productos(id_prd)
);

CREATE TABLE tb_facturas (
	id_fct INT(8) NOT NULL AUTO_INCREMENT,
    FK_id_cli INT(8) NOT NULL,
    tot_fct FLOAT,
    est_fct VARCHAR(15),
    mnt_pgd FLOAT DEFAULT 0,
    PRIMARY KEY (id_fct),
    FOREIGN KEY (FK_id_cli) REFERENCES tb_clientes(id_cli)
);

CREATE TABLE tb_ordenes (
	id_ord INT(8) NOT NULL AUTO_INCREMENT,
	FK_id_fct INT(8) NOT NULL,
    FK_id_prd INT(8) NOT NULL,
    cant FLOAT,
    cost FLOAT,
    PRIMARY KEY (id_ord),
    FOREIGN KEY (FK_id_fct) REFERENCES tb_facturas(id_fct),
    FOREIGN KEY (FK_id_prd) REFERENCES tb_productos(id_prd)
);

/*
DROP TABLE tb_ordenes;
DROP TABLE tb_facturas;
DROP TABLE tb_stock;
DROP TABLE tb_productos;
DROP TABLE tb_clientes;
DROP DATABASE sd_db;
*/