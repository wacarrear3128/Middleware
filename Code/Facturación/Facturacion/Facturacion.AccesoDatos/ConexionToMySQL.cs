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
            mysql_conexion = "Database= sd_db; Data Source=localhost; User Id=sdlocal; Password=sdlocal";
        }

        protected MySqlConnection GetConnection()
        {
            return new MySqlConnection(mysql_conexion);
        }
    }
}