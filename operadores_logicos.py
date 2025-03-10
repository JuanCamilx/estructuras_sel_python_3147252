'''
operadores lógicos

Aquellos los que operan unicamente
con valores booleanos(V F)
Acorde a las tablas de verdad
'''

#Ejemplo 1: Operador not:
y = not True 
print("El resultado de operar con not es" ,y)

#ejemplo 2: Operador and
y = False and True
print("El resultado de operar con and es" ,y)


#ejemplo 3: operador or 
y = False or True
print("El resultado de operar con or es" ,y)


'''
jerarquia de predencia de operadores 
(logicos inclusive)
1. ()
2. **
3. *,/,%,
4. +,-
5. >, <, >=, <=, !=, ==
6. not
7. and
8. or
9. =
'''

#ejemplo 4: Jerarquia de operadores 
y = False and not True or False