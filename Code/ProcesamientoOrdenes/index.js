const express = require('express')
const path = require('path')
const app = express()
var body_parser = require('body-parser');
const zmq = require('zeromq');

//configuracion
// app.use(express.static(__dirname));
app.use(express.static(__dirname + '/views'));
app.set('view engine','ejs');
app.use(require('./routes/send'));
app.use(body_parser.urlencoded({extended:true}));

//routes 
app.get('/', function (req, res) {
  res.render('index',{success:''})
})

var productos = [
  {
    'codigo':'prod-001',
    'nombre':'Panasonic Pantalla LCD',
    'precio':'25070',
    'cantidad':0
  },
  {
    'codigo':'prod-002',
    'nombre':'Mica Comoda 5 Cajones',
    'precio':'30240',
    'cantidad':0
  },
  {
    'codigo':'prod-003',
    'nombre':'Hewlett Packard Multifuncional F2208',
    'precio':'60230',
    'cantidad':0
  }
]

app.post('/cuerpo',async(req,res)=>{
  var cuerpo =req.body
  let {panasonic,mica,packard} =  cuerpo;
  console.log("cuerpo",cuerpo);
  
  productos[0].cantidad=panasonic
  productos[1].cantidad=mica;
  productos[2].cantidad=packard;

  console.log("Productos " ,productos);

  console.log('Connecting to hello world server…');

//  Socket to talk to server
const sock = new zmq.Request();
sock.connect('tcp://localhost:5555');

for (let i = 0; i < 10; i++) {
  
  console.log('Sending cuerpo', i);

  await sock.send(JSON.stringify(productos));
  const [result] = await sock.receive();
  console.log('Received ', result.toString(), i);
  }
  console.log("Hola mundo");
  res.render('index', {success:'Felicidades'})
})

app.listen(3000,()=>{
    console.log("Hola estoy corriendo en el puerto 3000")
})
