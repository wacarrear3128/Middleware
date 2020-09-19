var frutas = [];
let id=1;
function agregar(cantidad,nombre,precio){
    producto = {} ;
    producto.idp = id
    producto.nombre = nombre;
    producto.cantidad= parseInt(cantidad);
    producto.diferencia=0;
    producto.precio = parseFloat(precio)
    frutas.push(producto);
    Swal.fire(
        'Felicidades!',
        `ha agregado! ${cantidad} ${nombre} al carrito`,
        'success'
      )
      console.log(frutas);

     $.post("/acumular",{prod:JSON.stringify(frutas)})
     id++;
}

function enviarProductos(){
    console.log("se ha enviado",frutas);
    $.post('/comprar',{'monto':JSON.stringify(frutas)})
        .done(resp=>{
            alert(resp);
        });   
}
function asignarValor(){
    $.get("/datos").done(resp => {
        let total= resp;
        document.getElementById("total-pagar").value=total;
    });
    verificarCantidad();
    let total=0;
    // frutas.forEach(fruta=>{
    //     total= totalfruta.cantidad*fruta.precio;
    // })
}
function enviarPago() {
    let monto = $('#ingresar-pago').val();
    $.post("/comprar", { monto: monto }).done(resp => {
        let valor = parseFloat(resp);
        if(valor<0){
            valor = -1*valor
            Swal.fire(
                'Error',
                `No ha ingresado un monto suficiente, le falta ${valor} dolares`,
                'info'
              )
              document.getElementById("por-pagar").value=valor; 
        }else{
            Swal.fire(
                'Felicidades',
                `La compra se realizo con exito , gracias!!!`,
                'success'
              )
        }
    });
}
function enviarPagoCuentasXCobrar(){
    console.log("enviando pago...");
}
function verificarCantidad(){
    $.post("/verificar", null).done(resp => {
        let respuesta =resp;
        if(respuesta=="false"){
            Swal.fire(
                'Error',
                `No hay sufuciente stock`,
                'error'
              )

              
        }else{
            Swal.fire(
                'OK',
                `Todo ok`,
                'success'
              )

            document.getElementById("pagarMonto").disabled=false;
            document.getElementById("verificarStock").disabled=true;
        }
        
        
    });
}



