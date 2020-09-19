//using Echovoice.JSON;
using Facturacion.Entidades;
using Facturacion.LogicaNegocio;
using NetMQ;
using NetMQ.Sockets;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;

namespace Facturacion
{
    static class Program
    {
        static Pruebas_facturacion pruebasf = new Pruebas_facturacion();
        static Servidor server = new Servidor();
        static Cliente client = new Cliente();
        static void Main(string[] args)
        {
            server.Recibir();
        }
    }
}