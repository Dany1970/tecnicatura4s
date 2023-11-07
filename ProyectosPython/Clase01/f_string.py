nombre = "Pepe"
edad = 30
sueldo = 3000
#con interpolación como hemos visto antes
# las llaves en interpolación se les llama placeholder
#es la forma más utilizada y más recomendada
mensaje = f'Nombre {nombre} Edad {edad} Sueldo {sueldo:.2f}'
print(mensaje)

#El método print tb puede usarse para dar formato pero es muy limitado
print(nombre, edad, sueldo, sep=', ') #por ej acá se separan las variables por coma