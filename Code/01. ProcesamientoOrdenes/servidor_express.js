const express = require('express')
const path = require('path')
const app = express()

//configuracion
// app.use(express.static(__dirname));
app.use(express.static(__dirname + '/views'));
app.set('view engine','ejs');


// asignacion de datos
let nombre = "Minimarket"
let productos = [
  {
    'id': 1,
    'nombre': 'Panasonic Pantalla LCD',
    'precio': 25070,
    'cantidad' : 0,
    'total' : 0
  },
  {
    'id': 2,
    'nombre': 'Mica Comoda 5 Cajones',
    'precio': 30240,
    'cantidad' : 0,
    'total' : 0
  },
  {
    'id': 3,
    'nombre': 'Hewlett Packard Multifuncional F2208',
    'precio': 60230,
    'cantidad' : 0,
    'total' : 0
  }
]
 

app.get('/', function (req, res) {
  res.render('index',{nombre:"MiniMarket",productos:productos})
})
 
app.listen(3000,()=>{
    console.log("Hola estoy corriendo en el puerto 3000")
})
