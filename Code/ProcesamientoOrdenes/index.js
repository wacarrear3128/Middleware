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

var procesamientoOrdenes = {
  origen:"Ordenes",
  destino:"Inventario",
  dni:"21436587",
  pedidos:[],
  reservar:false,
  monto:0,
  vuelto:0
}
var productos = [];
//routes 
app.get('/', function (req, res) {
  res.render('login')
})
app.post("/login",(req,res)=>{
  // res.render('productos',{success:''})
  let dni = req.body.username;
  procesamientoOrdenes.dni=dni;
  console.log("********************")
  console.log(procesamientoOrdenes);
  console.log("********************")
  res.redirect("/productos");
})
app.post("/acumular",(req,res)=>{
  console.log("entro a acumular los productos")
  productos = JSON.parse(req.body.prod);
  console.log(productos);
  res.render('productos',{success:''});


})
app.get('/productos',function(req,res){
  res.render('productos',{success:''})
})

app.post('/pagar',function(req,res){
  res.redirect('/pago');  
})
app.get('/pago',(req,res)=>{
  console.log("entro a pago");
  res.render('pago',{
    productos : productos
    });
})

// app.post("/comprar",(req,res)=>{
//   let monto = req.body.monto;
//   console.log("**********************************");
//   console.log(monto);
//   procesamientoOrdenes.pedidos=productos
//   let total = 0;
//   procesamientoOrdenes.monto=parseInt(monto);
//   console.log(procesamientoOrdenes);
//   res.redirect('/productos')
// })
app.post('/verificar',async (req,res)=>{
  console.log("*******Realizando la verificacion*********");
  procesamientoOrdenes.pedidos=productos
  // procesamientoOrdenes.monto=parseInt(monto);
  console.log(procesamientoOrdenes);

  console.log('Connecting to Inventario server…');

//  Socket to talk to server
const sock = new zmq.Request();
sock.connect('tcp://34.121.65.175:5050');
  await sock.send(JSON.stringify(procesamientoOrdenes));
  const [result] = await sock.receive();
  console.log("******************")
  console.log('Received ', result.toString());
  console.log("******************")
  let resultado = result.toString();
  // console.log(typeof(resultado));

  resultado2 = JSON.parse(resultado)
    
   let reservar= resultado2.reservar;
  res.send(reservar.toString());
})

app.post('/comprar',async (req,res)=>{
  let monto = req.body.monto;
  console.log("**************Realizando el pago***********");
  console.log(monto);
  procesamientoOrdenes.destino="Cuentas";
  procesamientoOrdenes.pedidos=productos
  procesamientoOrdenes.monto=parseFloat(monto);
  console.log(procesamientoOrdenes);
  const sock = new zmq.Request();
  sock.connect('tcp://34.121.240.130:5051');
    await sock.send(JSON.stringify(procesamientoOrdenes));
    const [result] = await sock.receive();
    console.log("******************")
    console.log('Received ', result.toString());
    console.log("******************")
    let resultado = result.toString();
    // console.log(typeof(resultado));

    let respuesta = JSON.parse(resultado);
    let vuelto = respuesta.vuelto;
    // resultado2 = JSON.parse(resultado)
    
    // console.log(resultado2.reservar);
  //aca enviare la informacion
  // comunicacion con los otros servidores
  res.send(vuelto.toString());

})
app.get("/datos",(req,res)=>{
  console.log("**aa**")
  let total=0;
  productos.forEach(producto=>{
    total+=producto.precio*producto.cantidad;
  })
  res.send(total.toString());
})

// ******************************
app.post('/pruebarest',function(req,res){
  var cuerpo =req.body.data;
  console.log("estoo ha llegado ",cuerpo);
  res.send("Hola mundo");
})
var productos = [
  {
    'nombre':'Prod001',
    'cantidad':0,
    'dni':"12345678"
  },
  {
    'nombre':'Prod002',
    'cantidad':0,
    'dni':"12345678"
  },
  {
    'nombre':'Prod003',
    'cantidad':0,
    'dni':"12345678"
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

  console.log('Connecting to Inventario server…');

//  Socket to talk to server
const sock = new zmq.Request();
sock.connect('tcp://34.123.133.9:9092');
  await sock.send(JSON.stringify(productos));
  const [result] = await sock.receive();
  console.log("******************")
  console.log('Received ', result.toString());
  console.log("******************")
  let resultado = result.toString();
  console.log(typeof(resultado));

  res.render('index', {success:'Gracias por su compra !! '})
})

app.listen(3000,()=>{
    console.log("Hola estoy corriendo en el puerto 3000")
})
