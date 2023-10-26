#help(str.capitalize)

mensaje1 = "hola mundo"
mensaje2 = mensaje1.capitalize()
print(f'Mensaje1: {mensaje1}, id: {id(mensaje1)}')
print(f'Mensaje2: {mensaje2}, id: {id(mensaje2)}')

mensaje1 += ' Adiós'
print(f'Mensaje1: {mensaje1}, id: {id(mensaje1)}')

'''
Conclusión: las cadenas son inmutables, cada vez que se modifica una cadena
se genera un nuevo objeto, una nueva cadena
'''

