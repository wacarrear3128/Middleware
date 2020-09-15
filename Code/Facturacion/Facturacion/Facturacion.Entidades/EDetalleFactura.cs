using System;
using System.Collections.Generic;
using System.Text;

namespace Facturacion.Entidades
{
    public class EDetalleFactura
    {
        public int id_fac { get; set; }
        public int id_cli { get; set; }
        public string cliente { get; set; }
        public string nom_prod { get; set; }
        public double prec_prod { get; set; }
        public double cantidad { get; set; }
        public double monto { get; set; }
        public double total { get; set; }
        public double abonado { get; set; }
        public double cuenta { get; set; }
    }
}
