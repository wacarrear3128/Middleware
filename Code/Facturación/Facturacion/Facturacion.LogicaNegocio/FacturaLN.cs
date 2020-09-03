using System;
using System.Collections.Generic;
using System.Text;
using Facturacion.AccesoDatos;
using Facturacion.Entidades;

namespace Facturacion.LogicaNegocio
{
    public class FacturaLN
    {
        FacturaDA facturaDA = new FacturaDA();
        public void InsertarFactura(List<EFactura_Request> factreq)
        {
            EFactura factura = new EFactura();
            factura.id_cliente = factreq[1].dni;
            factura.estado_fac = "Sin Cancelar";
            facturaDA.InsertarFactura(factura);
        }

        public int MaxFactura()
        {
            return facturaDA.MaxFactura();
        }

        public double MontobyId(int id)
        {
            return facturaDA.MontobyId(id);
        }
    }
}
