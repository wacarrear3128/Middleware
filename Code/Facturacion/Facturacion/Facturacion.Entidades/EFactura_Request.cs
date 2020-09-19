using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Facturacion.Entidades
{
    public class EFactura_Request
    {

        public string origen { get; set; }
        public string destino { get; set; }
        public int dni { get; set; }
        public double dif { get; set; }
        public List<EPedido> pedidos {get;set;}
        public bool reservar { get; set; }
    }

    public class EPedido
    {
        public int idp { get; set; }
        public string nombre { get; set; }
        public int cantidad { get; set; }
        public double diferencia { get; set; }
        public double costo { get; set; }
    }
    public class ListFactuta
    {
        public List<EFactura_Request> items { get; set; }
    }
}

