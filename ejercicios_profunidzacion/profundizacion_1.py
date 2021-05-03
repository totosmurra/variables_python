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

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio

print("primer numero =")
nmr1 = int(input())

print("segundo numero =")
nmr2 = int(input())

print ("si queres sumar escribi 1")
print ("si queres restar escribi 2")
print ("si queres multiplicar escribi 3")
print ("si queres dividir escribi 4")
print ("si queres potenciar escribi 5")


operacion = int(input())


if operacion == 1:
  print (nmr1 + nmr2)

elif operacion == 2:
  print (nmr1 - nmr2)

elif operacion == 3:
  print (nmr1 * nmr2)

elif operacion == 4:
  print (nmr1 / nmr2)

elif operacion == 5:
  print (nmr1 ** nmr2)

