<?php

class CuentasDA {
	// Consulta la deuda por pagar de cierta factura en la base de datos
	// Recibe la conexión con la bd y el ID de la factura en cuestión
	// Retorna el valor de la deuda
	public static function getDeuda($conn, $idFact) {
		$query = "SELECT (tot_fct - mnt_pgd) AS deuda, est_fct FROM tb_facturas WHERE id_fct = " . $idFact;
		$result = $conn->query($query);
		$ret = -1;

		// Si el resultado de la consulta no está vacío
		if ($result != false) {
			// Devolver los resultados de la consulta
			if ($result->num_rows > 0) {
				echo ">> Filas: " . $result->num_rows . "\n";
				// output data of each row
				while($row = $result->fetch_assoc()) {
				    echo "Deuda: " . $row["deuda"] . " - Estado: " . $row["est_fct"] . "\n";
				    $ret = (float) $row["deuda"];
				    echo gettype($ret) . " -> " . $ret . "\n";
				}
			} else {
				echo ">> Consulta vacía. No hay deuda.\n";
			}
		} else {
			echo ">> Error de consulta.";
		}

		return $ret;
	}

	// Para pagar a factura dejando parte de la deuda pendiente
	// Recibe la conexión, ID de factura y mmonto a pagar
	// Retorna 1 si todo sale bien y 0 si no.
	public static function pagarFactura($conn, $idFact, $pago) {
		$query = "UPDATE tb_facturas SET mnt_pgd = mnt_pgd + " . $pago . " WHERE id_fct = " . $idFact;
		$result = $conn->query($query);
		echo "Resultado: " . $result . "\n";
		return $result;
	}

	// Para pagar a factura totalmente
	// Recibe la conexión, ID de factura y mmonto a pagar
	// Retorna 1 si todo sale bien y 0 si no.
	public static function pagarFacturaTotal($conn, $idFact, $pago) {
		$query = "UPDATE tb_facturas SET mnt_pgd = mnt_pgd + " . $pago . ", est_fct = 'Cancelado' WHERE id_fct = " . $idFact;
		$result = $conn->query($query);
		echo "Resultado: " . $result . "\n";
		return $result;
	}

	// Este método va a llamar a los anteriores, controla los pagos en base a la deuda y el monto a pagar
	// Recibe la conexión, ID de factura y mmonto a pagar
	// Retorna el vuelto de la operación (positivo si sobra, negativo si falta o cero si es exacto)
	public static function agregarPago($conn, $idFact, $mntPag) {
		$deuda = self::getDeuda($conn, $idFact);
		$vuelto = $mntPag - $deuda;

		if ($vuelto > 0) {
			// Devolver con nueva deuda
			self::pagarFacturaTotal($conn, $idFact, $deuda);
		} else {
			// Devolver con vuelto
			self::pagarFactura($conn, $idFact, $mntPag);
		}

		// Retorna lo que falta para cancelar la deuda totalmente
		echo "Vuelto: " . $vuelto . "\n";
		return $vuelto;
	}

	public static function getIdFacturaPorNombreCliente($conn, $nomCli) {
		//$query = "SELECT * FROM tb_facturas AS fac INNER JOIN tb_clientes AS cli ON fac.FK_id_cli = cli.id_cli WHERE CONCAT(cli.nom_cli, ' ', cli.app_cli, ' ', cli.apm_cli) = '" . $nomCli . "' AND est_fct != 'Sin cancelar' ORDER BY id_fct DESC LIMIT 1";
		$query = "SELECT * FROM tb_facturas AS fac INNER JOIN tb_clientes AS cli ON fac.FK_id_cli = cli.id_cli WHERE CONCAT(cli.nom_cli, ' ', cli.app_cli, ' ', cli.apm_cli) = '" . $nomCli . "' AND est_fct = 'Sin cancelar'";
		$result = $conn->query($query);
		$ret = -1;

		// Si el resultado de la consulta no está vacío
		if ($result != false) {
			// Devolver los resultados de la consulta
			if ($result->num_rows > 0) {
				echo ">> Filas: " . $result->num_rows . "\n";
				// output data of each row
				while($row = $result->fetch_assoc()) {
					$cliente = $row["nom_cli"] . " " . $row["app_cli"] . " " . $row["apm_cli"];
				    echo "Cliente: " . $cliente . " - ID: " . $row["id_cli"] . "\n";
				    $ret = (int) $row["id_fct"];
				}
			} else {
				echo ">> El cliente no tiene facturas pendientes. Revise ortografía.\n";
			}
		} else {
			echo ">> Error de consulta.\n";
		}

		return $ret;
	}

	public static function getIdFacturaPorIdCliente($conn, $idCli) {
		//$query = "SELECT * FROM tb_facturas AS fac INNER JOIN tb_clientes AS cli ON fac.FK_id_cli = cli.id_cli WHERE CONCAT(cli.nom_cli, ' ', cli.app_cli, ' ', cli.apm_cli) = '" . $nomCli . "' AND est_fct != 'Sin cancelar' ORDER BY id_fct DESC LIMIT 1";
		$query = "SELECT * FROM tb_facturas AS fac INNER JOIN tb_clientes AS cli ON fac.FK_id_cli = cli.id_cli WHERE id_cli = '" . $idCli . "' AND est_fct = 'Sin cancelar'";
		$result = $conn->query($query);
		$ret = -1;

		// Si el resultado de la consulta no está vacío
		if ($result != false) {
			// Devolver los resultados de la consulta
			if ($result->num_rows > 0) {
				echo ">> Filas: " . $result->num_rows . "\n";
				// output data of each row
				while($row = $result->fetch_assoc()) {
					$cliente = $row["nom_cli"] . " " . $row["app_cli"] . " " . $row["apm_cli"];
				    echo "Cliente: " . $cliente . " - ID: " . $row["id_cli"] . "\n";
				    $ret = (int) $row["id_fct"];
				}
			} else {
				echo ">> El cliente no tiene facturas pendientes. Revise ortografía.\n";
			}
		} else {
			echo ">> Error de consulta.\n";
		}

		return $ret;
	}
}

?>