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
        static readonly Servidor server = new Servidor();
        static void Main(string[] args)
        {
            Console.WriteLine("*** MODULO DE FACTURACION ***");
            server.Recibir();
        }
    }
}