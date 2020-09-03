

var trs = document.querySelectorAll('tbody tr');
console.log(trs)
trs.forEach(tr => {
     tr.addEventListener('change',()=>{
     console.log("Hola desde javascript ")
 })    
});
