import random   

minus = "abcdefghijlkmnopqrstuvwxyz"
mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "0123456789"
simbolos = "[]{}()*;/,._-"

passtam = int(input("Introduzca la longitud de la contraseña: "))

passsuma = minus + mayus + nums + simbolos

contraseña = "".join(random.sample(passsuma,passtam))

print ("La contraseña creada es: " + contraseña)

