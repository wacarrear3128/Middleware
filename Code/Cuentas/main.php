<?php

include 'Cuentas.php';

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

	$vuelto = Cuentas::pagar($jsonStr);

	$scktOrd->send($vuelto);
}


?>