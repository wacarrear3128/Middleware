DELIMITER //
CREATE TRIGGER tg_calc_precio
BEFORE INSERT ON tb_ordenes FOR EACH ROW
BEGIN
	DECLARE punit FLOAT;
	DECLARE ctot FLOAT;
	SET punit := (SELECT prc_prd FROM tb_productos WHERE id_prd = NEW.FK_id_prd);
    SET ctot := punit * NEW.cant;
    SET NEW.cost = ctot;
END; //

DELIMITER //
CREATE TRIGGER tg_calc_factura
AFTER INSERT ON tb_ordenes FOR EACH ROW
BEGIN
	UPDATE tb_facturas SET tot_fct = tot_fct + NEW.cost WHERE id_fct = NEW.FK_id_fct;
END; //

DROP procedure IF EXISTS sp_detalle_factura_list;
DELIMITER $$
create procedure sp_detalle_factura_list(p_dni int, p_fac int)
	begin
		select f.id_fct as FACTURA, c.id_cli as DNI, concat(c.nom_cli, ' ', c.app_cli, ' ', c.apm_cli) as CLIENTE, 
			p.nom_prd as PRODUCTO, p.prc_prd as PRECIO, o.cant as CANTIDAD, o.cost as COSTO, f.tot_fct as TOTAL
			from tb_facturas f
			inner join tb_clientes c on f.fk_id_cli = c.id_cli
			inner join tb_ordenes o on f.id_fct = o.fk_id_fct
			inner join tb_productos p on o.fk_id_prd = p.id_prd
			where c.id_cli = p_dni and f.id_fct = p_fac;
	end$$
DELIMITER ;

INSERT INTO tb_productos (nom_prd, dsc_prd, mrc_prd, prc_prd, und_prd) VALUES
	('Prod001', 'Primer producto', 'Marca01', 20.0, 'und'),
    ('Prod002', 'Segundo producto', 'Marca01', 20.0, 'und'),
    ('Prod003', 'Tercer producto', 'Marca01', 50.0, 'und'),
    ('Prod004', 'Cuarto producto', 'Marca02', 15.5, 'kg'),
    ('Prod005', 'Quinto producto', 'Marca03', 17.0, 'L'),
    ('Prod006', 'Sexto producto', 'Marca03', 29.9, 'kg'),
    ('Prod007', 'Setimo producto', 'Marca03', 40.0, 'und'),
    ('Prod008', 'Octavo producto', 'Marca03', 20.0, 'kg'),
    ('Prod009', 'Noveno producto', 'Marca04', 20.0, 'L'),
    ('Prod010', 'Decimo producto', 'Marca04', 17.5, 'kg');
    
INSERT INTO tb_productos (nom_prd, dsc_prd, mrc_prd, prc_prd, und_prd) VALUES
	('platano', 'Platano', '-', 2.0, 'kg'),
    ('chirimoya', 'Chirimoya', '-', 3.5, 'kg'),
    ('uva', 'Uva', '-', 1.5, 'kg'),
    ('manzana', 'Manzana', '-', 1.5, 'kg'),
    ('mango', 'Mango', '-', 3.5, 'kg'),
    ('pera', 'Pera', '-', 1.5, 'kg');

INSERT INTO tb_clientes (id_cli, nom_cli, app_cli, apm_cli) VALUES
	(12345678, 'Yordi', 'Caushi', 'Cueva'),
    (13254768, 'Rolando', 'Ramos', 'Vargas'),
    (21436587, 'Joel', 'Trujillo', 'Cruz'),
    (13245768, 'Miguel', 'Velasquez', 'Yzquierdo');

INSERT INTO tb_clientes (id_cli, nom_cli, app_cli, apm_cli) VALUES
	(12457823, 'Martin', 'Ochoa', 'Cueva'),
    (23568945, 'Javier', 'Lozada', 'Ordonez'),
    (14253685, 'Chupetín', 'Trujillo', ' '),
    (14853652, 'Susana', 'Diaz', ' '),
    (95482615, 'Kimberly', 'Loayza', 'Cabello'),
    (62518475, 'Raul', 'De la Torre', 'Soto'),
    (23654815, 'Raquel', 'Torres', 'Blanco'),
    (95846231, 'Irma', 'Diaz', 'Diaz');

INSERT INTO tb_stock (FK_id_prd, stock) VALUES
	(1, 15), (2, 15), (3, 15), (4, 15), (5, 15), (6, 15), (7, 15),
    (8, 15), (9, 15), (10, 15);
    
INSERT INTO tb_stock (FK_id_prd, stock) VALUES
	(11, 30), (12, 30), (13, 30), (14, 30), (15, 30), (16, 30);

INSERT INTO tb_facturas (FK_id_cli, tot_fct, est_fct, mnt_pgd) VALUES
	(12345678, 0.0, 'Sin cancelar', 0.0),
    (13254768, 0.0, 'Sin cancelar', 0.0),
    (12345678, 0.0, 'Sin cancelar', 0.0),
    (13254768, 0.0, 'Sin cancelar', 0.0);

INSERT INTO tb_ordenes (FK_id_fct, FK_id_prd, cant, cost) VALUES
	(1, 1, 2.0, 0.0), (1, 2, 1.0, 0.0), (1, 3, 1.0, 0.0), (1, 4, 20.0, 0.0),
	(3, 1, 2.0, 0.0), (2, 2, 1.0, 0.0), (3, 3, 1.0, 0.0), (3, 4, 20.0, 0.0);
/*
SELECT * FROM tb_productos;
SELECT * FROM tb_clientes;
SELECT * FROM tb_facturas;
SELECT * FROM tb_ordenes;
SELECT * FROM tb_stock;

SELECT ord.FK_id_fct, prd.prc_prd, ord.cant, ord.cost
FROM tb_ordenes AS ord
INNER JOIN tb_productos AS prd ON ord.FK_id_prd = prd.id_prd;

DROP TRIGGER tg_calc_precio;
DROP TRIGGER tg_calc_factura;

SELECT stock FROM tb_stock AS s
JOIN tb_productos AS p ON p.id_prd = s.FK_id_prd
WHERE p.nom_prd = 'Prod001';

SELECT stock FROM tb_stock AS s JOIN tb_productos AS p ON p.id_prd = s.FK_id_prd WHERE p.nom_prd = 'Prod001'

UPDATE tb_stock SET stock = stock - 12 WHERE FK_id_prd = 1;*/