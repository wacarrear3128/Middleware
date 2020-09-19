using System;
using System.Collections.Generic;
using System.Text;
using Facturacion.AccesoDatos;
using Facturacion.Entidades;

namespace Facturacion.LogicaNegocio
{
    public class FacturaLN
    {
        readonly FacturaDA facturaDA = new FacturaDA();
        public void InsertarFactura(EFactura_Request factreq)
        {
            EFactura factura = new EFactura
            {
                id_cliente = factreq.dni,
                estado_fac = "Sin Cancelar"
            };
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
