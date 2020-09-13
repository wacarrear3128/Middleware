<?php 
class Comunicado {
	private $idp;
	private $nom;
	private $cnt;
	private $dif;
	private $cst;
	private $dni;

	public function __construct($idp, $nom, $cnt, $dif, $cst, $dni) {
		$this->idp = $idp;
		$this->nom = $nom;
		$this->cnt = $cnt;
		$this->dif = $dif;
		$this->cst = $cst;
		$this->dni = $dni;
		echo "Constructed: " . $nom . "\n";
	}
}

class Objeto {
	public $name;
	public $lname;
	public $dni;

	public function __construct($name, $lname, $dni) {
		$this->name = $name;
		$this->lname = $lname;
		$this->dni = $dni;
		echo "Constructed: " . $name . "\n";
	}
}
?>