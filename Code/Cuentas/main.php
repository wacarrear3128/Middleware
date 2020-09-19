<?php

include 'Cuentas.php';

function getJsonFromString($jsonString) {
	print("Getting string... Returning json...\n");
	return json_decode($jsonString);
}

function getStringFromJson($jsonObject) {
	print("Getting json... Returning string...\n");
	return json_encode($jsonObject);
}

#############################################
##### ----- Esto se va a ejecutar ----- #####
#############################################

$dirOrdenes = "tcp://*:5051";

$ctxtOrd = new ZMQContext();
$scktOrd = new ZMQSocket($ctxtOrd, ZMQ::SOCKET_REP);
$scktOrd->bind($dirOrdenes);

echo "*** MÓDULO DE CUENTAS POR COBRAR ***\n";

while (true) {
	echo "Esperando solicitudes...\n";

	$jsonStr = $scktOrd->recv();
	/*echo $jsonStr . "\n";
	echo gettype($jsonStr) . "\n";*/

	$jsonObj = getJsonFromString($jsonStr);

	$vuelto = Cuentas::pagar($jsonObj);
	$jsonObj->vuelto = $vuelto;

	$resp = getStringFromJson($jsonObj);

	$scktOrd->send($resp);
}


?>