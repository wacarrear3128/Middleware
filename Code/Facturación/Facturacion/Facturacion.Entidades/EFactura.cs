using System;

namespace Facturacion.Entidades
{
    public class EFactura
    {
        public int id_fac { get; set; }
        public int id_cliente { get; set; }
        public double total_fac { get; set; }
        public double monto_pag { get; set; }
        public string estado_fac { get; set; }
    }
}
