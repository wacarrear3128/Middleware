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
    'nombre':'Prod001',
    'cantidad':0,
    'dni':"876534521"
  },
  {
    'nombre':'Prod002',
    'cantidad':0,
    'dni':"876534521"
  },
  {
    'nombre':'Prod003',
    'cantidad':0,
    'dni':"876534521"
  }
]

app.post('/cuerpo',async(req,res)=>{
  var cuerpo =req.body
  let {panasonic,mica,packard} =  cuerpo;
  panasonic = parseInt(panasonic);
  mica = parseInt(mica);
  packard = parseInt(packard);
  console.log(panasonic,mica,packard);
  
  productos[0].cantidad=panasonic
  productos[1].cantidad=mica;
  productos[2].cantidad=packard;

  console.log("Productos " ,productos);

  console.log('Connecting to hello world server…');

//  Socket to talk to server
const sock = new zmq.Request();
sock.connect('tcp://34.123.133.9:9092');


  

  await sock.send(JSON.stringify(productos));
  const [result] = await sock.receive();
  console.log('Received ', result.toString());
  let resultado = result.toString();
  console.log(typeof(resultado));
  console.log("Hola mundo");

  res.render('index', {success:'Felicidades'})
})

app.listen(3000,()=>{
    console.log("Hola estoy corriendo en el puerto 3000")
})
