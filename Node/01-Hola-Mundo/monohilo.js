console.log('Hola a toda la cohorte 2022, bienvenidos a Node.js')

//Vamos a ejecutar algo con un delay de 3 segundos
/*setInterval(function() {
    console.log('Sigo activo');
}, 1000);*/
//Vemos que esto se ejecuta infinitas veces, lo comentamos y hacemos una variante
var i = 0;
setInterval(function() {
    console.log(i);
    i++;
    
    /*if(i === 5) {
        console.log('forzamos error');
        var a = 3 + z;//la variable z no está definida, el compilador no detecta el error porque se detecta en tiempo de ejecución

    }*/
}, 1000);
console.log('Segunda instrucción');
