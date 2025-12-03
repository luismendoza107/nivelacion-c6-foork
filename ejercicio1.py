def verifique_su_contraseña():
    system_password = "admin123" 
    user_password = input("Ingresa la contraseña, por favor: ")

#Paso 4:
    if system_password == user_password:
        print("Contraseña correcta, bienvenido :D")
    else:
        print("Contraseña incorrecta")

verifique_su_contraseña()
   

