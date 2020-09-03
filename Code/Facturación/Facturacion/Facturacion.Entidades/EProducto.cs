using System;
using System.Collections.Generic;
using System.Text;

namespace Facturacion.Entidades
{
    public class EProducto
    {
        public int id_prod { get; set; }
        public string nombre_prod { get; set; }
        public string desc_prod { get; set; }
        public string marca_prod { get; set; }
        public double prec_prod { get; set; }
        public string und_prod { get; set; }
    }
}
