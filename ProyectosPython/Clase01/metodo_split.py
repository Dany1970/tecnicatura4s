
#help(str.split)

cursos = 'Java Python Node JavaScript Django '
lista_cursos = cursos.split()
print(f'Lista de cursos: {lista_cursos}')
print(type(lista_cursos))

cursos_separados_comas = 'Java,Python,Node,JavaScript,Django'
lista_cursos = cursos_separados_comas.split(',',2)#se coloca el separador que debe buscar, y el número indica cuántos tiene que buscar
print(f'Lista de cursos: {lista_cursos}')
print(len(lista_cursos))