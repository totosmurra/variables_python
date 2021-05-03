# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con cadenas
'''
Enunciado:
Realice un programa que determine si una persona_2
es pariente de la persona_1
Para facilitar el ejercicio solo ingresar un nombre
y un apellido por persona
Ingresar dichos datos como Nombre Apellido, es decir,
primero el nombre y luego el apellido, separado por un espacio.
- El programa debe consultar primero el nombre completo de la persona_1
- Luego debe consultar el nombre completo de la persona_2
- Debe extraer el apellido de la persona_2
- Luego preguntar si apellido de la persona_2 está contenido
  en el nombre completo de la persona_1
- En caso de contenerlo, son parientes
- Imprimir en pantalla el resultado

NOTA: Para extraer el apellido del nombre recomendamos
usar el método "split"
Mostraremos un ejemplo:

direccion_completa = 'Monroe 2716'
calle, altura = direccion_completa.split(' ')

Les dejo por su cuenta a que busquen un poco más acerca
de este método que seguramente utilizarán mucho de acá en adelante.
Les dejamos un link con algunos ejemplos más:
https://www.pythonforbeginners.com/dictionary/python-split

Cualquier duda con el método split pueden consultarla por el campus
'''

print('Comencemos a ponernos serios')
# Empezar aquí la resolución del ejercicio

print ("Nombre Persona 1:")
prsn1 = input()

print ("Nombre Persona 2:")
prsn2 = input()

prsn1a = prsn1.split(" ") [1]

prsn2a = prsn2.split(" ") [1]

if prsn1a == prsn2a:
  print ("Persona 1 y Persona 2 son parientes")

elif prsn1a != prsn2a:
  print ("Persona 1 y Persona 2 no son parientes")