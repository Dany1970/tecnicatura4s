# dar formato a una cadena /string)

nombre = "Daniela"
edad = 53
mensaje_con_formato = "Mi nombre es %s y tengo %d años" %(nombre, edad)
# print(mensaje_con_formato)

#Si trabajamos directamente con una tupla
persona = ("Carla", "Gomez", 5000.00)
mensaje_con_formato = "Hola %s %s. Tu sueldo es %.2f" # % persona # Aquí le pasamos el objeto tupla
# print(mensaje_con_formato % persona)


nombre = "Jorge"
edad = 69
sueldo = 3000
#mensaje_con_formato = "Nombre {} Edad {} Sueldo {:.2f}".format(nombre, edad, sueldo)
#print(mensaje_con_formato)

# si lo manejamos con índices, podemos cambiar el orden (ojo con equivocarse!)
#mensaje = "Nombre {0} Edad {1} Sueldo {2:.2f}".format(nombre, edad, sueldo)
#print(mensaje)
#mensaje1 = "Edad {1} Sueldo {2:.2f} Nombre {0}".format(nombre, edad, sueldo)
#print(mensaje1)

#Asignando nombres a las variables
mensaje = "Nombre {n} Edad {e} Sueldo {s}".format(n=nombre, e=edad, s=sueldo)
#print(mensaje)

#Usando un diccionario
diccionario = {"nombre": "Ivan", "edad": 20, "sueldo": 8000.00}
mensaje = 'Nombre {dic[nombre]} Edad {dic[edad]} Sueldo {dic[sueldo]:.2f} '.format(dic=diccionario)
print(mensaje)