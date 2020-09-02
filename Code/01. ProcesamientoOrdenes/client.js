//  Hello World client
const zmq = require('zeromq');

async function runClient() {
  console.log('Connecting to hello world server…');

  //  Socket to talk to server
  const sock = new zmq.Request();
  sock.connect('tcp://localhost:5555');

  for (let i = 0; i < 10; i++) {
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
    //console.log('Sending Hello ', i);

    await sock.send(JSON.stringify(productos));
    const [result] = await sock.receive();
    console.log('Received ', result.toString(), i);
  }
}

runClient();