print("Sistema superseguro INCUYO")
email = input("Email:")
contraseña = input("Contraseña:")
print(email)
print(contraseña)
if(email != "" and contraseña != ""):
    if(email == "facuugior@gmail.com" and contraseña == "46327546"):
        print("Bienvenido")
    else:
         print("Usuario o contraseña incorrecto")
else:
    print("Por favor ingrese email y contraseña")
