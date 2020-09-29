using Facturacion.Entidades;
using System;
using MySql.Data.MySqlClient;
using System.Collections.Generic;
using System.Text;

namespace Facturacion.AccesoDatos
{
    public class FacturaDA : ConexionToMySQL
    {
        public void InsertarFactura (EFactura factura)
        {
            using (var conexion = GetConnection())
            {
                conexion.Open();

                MySqlCommand cmd = new MySqlCommand("insert into tb_facturas (FK_id_cli, est_fct, tot_fct, mnt_pgd) values (@dni, @estado, 0, 0)", conexion);
                cmd.Parameters.AddWithValue("@dni", factura.id_cliente);
                cmd.Parameters.AddWithValue("@estado", factura.estado_fac);
                cmd.ExecuteNonQuery();
            }
        }

        public int MaxFactura()
        {
            int id_max;
            using (var conexion = GetConnection())
            {
                conexion.Open();

                MySqlCommand cmd = new MySqlCommand("select MAX(id_fct) as max from tb_facturas", conexion);
                MySqlDataReader lector = cmd.ExecuteReader();
                if (lector.Read())
                {
                    id_max = Convert.ToInt32(lector["max"]);
                    return id_max;
                }
            }
            return 0;
        }

        public double MontobyId(int id)
        {
            double monto;
            using (var conexion = GetConnection())
            {
                conexion.Open();
                MySqlCommand cmd = new MySqlCommand("select tot_fct as total from tb_facturas where id_fct = "+id, conexion);
                MySqlDataReader lector = cmd.ExecuteReader();
                if (lector.Read())
                {
                    monto = Convert.ToDouble(lector["total"]);
                    return monto;
                }
            }
            return 0;
        }
    }
}
