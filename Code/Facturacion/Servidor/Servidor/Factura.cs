using System;
using System.Collections.Generic;
using System.Text;

namespace ServidorCuentas
{
    public class Factura
    {
        public int id_producto { get; set; }
        public int id_cliente { get; set; }
        public string nombre { get; set; }
        public int cantidad { get; set; }
        public int diferencia { get; set; }
    }
    public class RootObject
    {
        public List<Factura> items { get; set; }
    }
}
