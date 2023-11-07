let nombre = process.env.NOMBRE || 'Sin nombre';//Si no existe el nombre, se le asigna 'Sin nombre'
let web = process.env.WEB || 'No tengo web';//||es or
console.log('Hola ' + nombre);
console.log('Mi web es ' + web);

/*buenas prácticas
recordar la documentación de node.js
Por qué utilizamos mayúsculas para estas variables?
Porque proviene de antiguas formas de programar, en las que se utilizaban variables globales, y para diferenciarlas de las locales, se utilizaban mayúsculas.
También si tiene dos nombres, se coloca guion bajo
*/
console.log('Ultima instruccion');
/*vamos a usar nodemon, como en el e-commerce*/
