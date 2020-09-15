using MySql.Data.MySqlClient;
using System;

namespace Facturacion.AccesoDatos
{
    public abstract class ConexionToMySQL
    {
        private readonly string mysql_conexion;

        //Crearemos la cadena de conexión concatenando las variables
        public ConexionToMySQL()
        {
            mysql_conexion = "Database= sd_db; Data Source=34.121.240.130; User Id=root; Password=root123";
        }

        protected MySqlConnection GetConnection()
        {
            return new MySqlConnection(mysql_conexion);
        }
    }
}