const express=require('express');
const  router=express.Router();
const zmq = require('zeromq');

router.post('/send', async (req,res)=>{
    var cuerpo =req.body
    console.log("cuerpo",cuerpo);
    
    console.log('Connecting to hello world server…');

  //  Socket to talk to server
  const sock = new zmq.Request();
  sock.connect('tcp://localhost:5555');

  for (let i = 0; i < 10; i++) {
    
    console.log('Sending cuerpo', i);

    await sock.send("Hello word");
    const [result] = await sock.receive();
    console.log('Received ', result.toString(), i);
    }
    console.log("Hola mundo");
    res.redirect('/')
 })
 module.exports = router;