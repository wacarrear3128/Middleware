<?php

include 'CuentasConnection.php';
include 'CuentasDA.php';

class Cuentas {

	public static function getSuficiente($idFct) {
		try {
			$cnx = Connection::getConnection();
			$deuda = CuentasDA::getDeuda($cnx, $idFct);
			echo $deuda . "\n";
			return $deuda;
		} catch (Exception $e) {
			echo "Excepción: ", $e->getMessage(), "\n";
		}
	}

	/*public static function pagar($reqJson) {
		try {
			$cnx = Connection::getConnection();
			$objJson = json_decode($reqJson);

			$idFct = CuentasDA::getIdFacturaPorNombreCliente($cnx, $objJson[0]->nom);
			$mnt = $objJson[0]->mnt;

			$vuelto = CuentasDA::agregarPago($cnx, $idFct, $mnt);

			return $vuelto;
		} catch (Exception $e) {
			echo "Excepción: ", $e->getMessage(), "\n";
		}
	}*/

	public static function pagar($jsonObj) {
		try {
			$cnx = Connection::getConnection();

			echo "Cliente: " . $jsonObj->dni . "\n";
			$idFct = CuentasDA::getIdFacturaPorIdCliente($cnx, $jsonObj->dni);
			$mnt = $jsonObj->monto;

			$vuelto = CuentasDA::agregarPago($cnx, $idFct, $mnt);

			return $vuelto;
		} catch (Exception $e) {
			echo "Excepción: ", $e->getMessage(), "\n";
		}
	}

	public static function prueba($idFct, $parametro) {
		try {
			$cnx = Connection::getConnection();
			//CuentasDA::agregarPago($cnx, $idFct, $parametro);
			CuentasDA::getIdFactura($cnx, $parametro);
		} catch (Exception $e) {
			echo "Excepción: ", $e->getMessage(), "\n";
		}
	}

}

/*
#############################################
##### ----- Esto se va a ejecutar ----- #####
#############################################

$dirOrdenes = "tcp://*:1051";

$ctxtOrd = new ZMQContext();
$scktOrd = new ZMQSocket($ctxtOrd, ZMQ::SOCKET_REP);
$scktOrd->bind($dirOrdenes);

echo "*** MÓDULO DE CUENTAS POR COBRAR ***\n";

while (true) {
	echo "Esperando solicitudes...\n";

	$jsonStr = $scktOrd->recv();
	echo $jsonStr . "\n";

	$vuelto = pagar($jsonStr);

	$scktOrd->send($vuelto);
}
*/
?>