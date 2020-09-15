using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Facturacion.Entidades
{
    public class EFactura_Request
    {

        public int idp { get; set; }
        public string nom { get; set; }
        public int cnt { get; set; }
        public double dif { get; set; }
        public double cst { get; set; }
        public int dni { get; set; }
    }

    public class ListFactuta
    {
        public List<EFactura_Request> items { get; set; }
    }
}

