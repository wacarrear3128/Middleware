using Facturacion.AccesoDatos;
using Facturacion.Entidades;
using System;
using System.Collections.Generic;
using System.Text;

namespace Facturacion.LogicaNegocio
{
    public class DetalleFacturaLN
    {
        DetalleFacturaDA detalleDA = new DetalleFacturaDA();

        public List<EDetalleFactura> Todos(int dni, int idFac)
        {
            return detalleDA.GetAll(dni, idFac);
        }
    }
}
