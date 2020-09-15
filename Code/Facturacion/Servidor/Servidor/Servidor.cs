using NetMQ;
using NetMQ.Sockets;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Text.Json;
using System.Threading;

namespace ServidorCuentas
{
    static class Servidor
    {
        public static void Main()
        {
            var obj = new RootObject();
            /*obj.items = new List<Factura>
                          {
                             new Factura {id_producto = 1, id_cliente = 12345678, nombre = "Joel", cantidad = 2, diferencia = 5 },
                             new Factura {id_producto = 2, id_cliente = 12345678, nombre = "Joel", cantidad = 2, diferencia = 5 }
                          };
            */
            /*var jeison = new Json
            {
                id_producto = 1,
                id_cliente = 12345678,
                nombre = "Joel",
                cantidad = 2,
                diferencia = 5
            };*/

            // string json = JsonConvert.SerializeObject(obj);

            using (var responder = new ResponseSocket())
            {
                responder.Bind("tcp://*:2104");

                while (true)
                {
                    string str = responder.ReceiveFrameString();
                    Console.WriteLine(str);
                    //Console.WriteLine("Received Hello");
                    Thread.Sleep(1000);  //  Do some 'work'
                    responder.SendFrame("Recibido por CuentasxCobrar");
                }
            }
        }
    }
}
