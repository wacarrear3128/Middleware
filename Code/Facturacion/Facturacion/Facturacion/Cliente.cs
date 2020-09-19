using Facturacion.Entidades;
using Facturacion.LogicaNegocio;
using NetMQ;
using NetMQ.Sockets;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Text;

namespace Facturacion
{
    public class Cliente
    {
        readonly FacturaLN facturaBL = new FacturaLN();
        int id;
        double monto;
        public void Enviar()
        {
            Console.WriteLine("Conectando con cuentas server…");
            id = facturaBL.MaxFactura();
            monto = facturaBL.MontobyId(id);
            var cuenta = new ECuenta
            {
                id_factura = id,
                total = monto
            };

            string json = JsonConvert.SerializeObject(cuenta);

            using (var requester = new RequestSocket())
            {
                requester.Connect("tcp://localhost:2104");
                Console.WriteLine("Conexion realizada");

                requester.SendFrame(json);
                string str = requester.ReceiveFrameString();
                Console.WriteLine(str);
            }
        }
    }
}
