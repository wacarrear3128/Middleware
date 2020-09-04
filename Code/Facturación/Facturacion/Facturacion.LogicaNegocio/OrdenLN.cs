using Facturacion.AccesoDatos;
using Facturacion.Entidades;
using System;
using System.Collections.Generic;
using System.Text;

namespace Facturacion.LogicaNegocio
{
    public class OrdenLN
    {
        OrdenDA orden = new OrdenDA();
        public void insertarOrden(List<EFactura_Request> factura, int id)
        {
            orden.insertarOrden(factura, id);
        }
    }
}
