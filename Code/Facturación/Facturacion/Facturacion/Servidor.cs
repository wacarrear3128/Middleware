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
    public class Servidor
    {
        Cliente client = new Cliente();
        FacturaLN facturaBL = new FacturaLN();
        OrdenLN ordenBL = new OrdenLN();
        DetalleFacturaLN dfacturaBL = new DetalleFacturaLN();
        public void Recibir()
        {
            using (var responder = new ResponseSocket())
            {
                responder.Bind("tcp://*:5555");

                while (true)
                {
                    Console.WriteLine("Esperando conexion");
                    string str = responder.ReceiveFrameString();
                    //Console.WriteLine(str);

                    List<EFactura_Request> obj1 = JsonConvert.DeserializeObject<List<EFactura_Request>>(str);

                    facturaBL.InsertarFactura(obj1);
                    int id_factura = facturaBL.MaxFactura();
                    ordenBL.insertarOrden(obj1, id_factura);


                    List<EDetalleFactura> dfactura = dfacturaBL.Todos(obj1[1].dni, id_factura);

                    Console.WriteLine("---------------------------------------------------------------------------");
                    Console.WriteLine("Cliente: "+dfactura[1].cliente);
                    Console.WriteLine("\t\tProducto" + "\tPrecio" + "\tCantidad" + "\tMonto");
                    Console.WriteLine("---------------------------------------------------------------------------");
                    foreach (var item in dfactura)
                    {
                        Console.WriteLine("\t\t" + item.nom_prod + "\t\t" + string.Format("{0:0.00}", item.prec_prod) + "\t" + item.cantidad + "\t\t" + item.monto);
                    }


                    Console.WriteLine("---------------------------------------------------------------------------");
                    client.Enviar();
                }
            }
        }
    }
}
