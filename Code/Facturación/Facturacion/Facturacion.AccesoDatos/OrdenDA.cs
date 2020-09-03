using Facturacion.Entidades;
using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Text;

namespace Facturacion.AccesoDatos
{
    public class OrdenDA : ConexionToMySQL
    {
        public void insertarOrden(List<EFactura_Request> facreq, int id)
        {
            using (var conexion = GetConnection())
            {
                conexion.Open();
                foreach(var item in facreq)
                {
                    MySqlCommand cmd = new MySqlCommand("insert into tb_ordenes (FK_id_fct,FK_id_prd, cant, cost) values (@fac, @prod, @cant, @cost)", conexion);
                    cmd.Parameters.AddWithValue("@fac", id);
                    cmd.Parameters.AddWithValue("@prod", item.idp);
                    cmd.Parameters.AddWithValue("@cant", item.cnt);
                    cmd.Parameters.AddWithValue("@cost", item.cst);
                    cmd.ExecuteNonQuery();
                }
            }
        }
    }
}
