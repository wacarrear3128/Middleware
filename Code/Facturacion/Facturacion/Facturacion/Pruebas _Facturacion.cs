using Facturacion.Entidades;
using Facturacion.LogicaNegocio;
using System;
using System.Collections.Generic;
using System.Text;

namespace Facturacion
{
    public class Pruebas_facturacion
    {
        readonly DetalleFacturaLN dfacturaBL = new DetalleFacturaLN();
        readonly FacturaLN facturaBL = new FacturaLN();

        public void ListarFactura(int dni, int idFac)
        {
            List<EDetalleFactura> dfactura = dfacturaBL.Todos(dni, idFac);

            foreach (var item in dfactura)
            {
                Console.WriteLine("----------------------------------------------------");
                Console.WriteLine(item.nom_prod + "\t\t" + item.prec_prod + "\t" + item.cantidad + "\t" + item.monto);
                Console.WriteLine("---------------------------------------------------- \n");
            }
        }

        public void InsertarFactura()
        {

            //facturaBL.InsertarFactura(12345678);
            Console.WriteLine("Se insertó nueva factura");
        }

        public void MaxFactura()
        {
            Console.WriteLine(facturaBL.MaxFactura());
        }
    }
}
