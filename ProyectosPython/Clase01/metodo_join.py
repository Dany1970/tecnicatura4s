
# help(str.join)

tupla_str = ('hola', 'alumnos', 'Tecnicatura', 'Universitaria')
mensaje = ' '.join(tupla_str)
print(f'Mensaje: {mensaje}') #devuleve una sola cadena

lista_cursos = ['Java', 'Python', 'Angular', 'Spring']
mensaje = ', '.join(lista_cursos)
print(f'Mensaje: {mensaje}')

# También funciona con cadenas:
cadena = 'HolaMundo'
mensaje = '.'.join(cadena)
print(f'Mensaje: {mensaje}')

diccionario = {'nombre': 'Juan', 'apellido': 'Pérez', 'edad': '10'}#join no trabaja con tipos numéricos, colocarlos como str
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
print(f'Llaves: {llaves}, Tipo: {type(llaves)}')
print(f'Valores: {valores}, Tipo: {type(valores)}')

