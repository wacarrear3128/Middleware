using Facturacion.AccesoDatos;
using Facturacion.Entidades;
using System;
using System.Collections.Generic;
using System.Text;

namespace Facturacion.LogicaNegocio
{
    public class OrdenLN
    {
        readonly OrdenDA orden = new OrdenDA();
        public void InsertarOrden(EFactura_Request factura, int id)
        {
            orden.InsertarOrden(factura, id);
        }
    }
}
