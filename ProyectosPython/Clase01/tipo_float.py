# Profundizando en el tipo float
a = 3.0
print(f'a:{a:.2f}')

# Constructor de tipo float -> puede recibir int y str y transformarlo en float
a = float(10) #Le pasamos un tipo entero
a = float('10')
print(f'a:{a:.2f}') #el constructor de tipo float lo transforma a float

# Notación científica (exponentes positivos o negativos)
a =3e5
print(f'a: {a:.2f}')
a =3e-5
print(f'a: {a:.5f}')

# Cualquier cáclulo que incluye un float, cambia todo a float

a = 4.0 + 5
print(a)
print(type(a))
