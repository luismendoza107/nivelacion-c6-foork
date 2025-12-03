'''
Un técnico de soporte necesita ingresar a una consola protegida por contraseña. Escribe un programa que:

1.Guarde la contraseña correcta en una variable ("admin123").
2. Pida al usuario ingresar una contraseña.
3. Verifique si la contraseña ingresada es correcta o no

'''
#Paso 1
system_password = "admin123"

#paso 2
user_password = input("Ingresa la contraseña, por favor: ")

#Paso 3:
if system_password == user_password:
    print("Contraseña correcta, bienvenido :D")
else:
    print("Contraseña incorrecta")

