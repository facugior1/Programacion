frase = str(input("Ingrese una frase: "))
cantidad = len(frase)
if(frase == "Aguante programacion"):
    print("Fin del programa")
elif(cantidad >= 15):
    while(frase != 0):
        print(frase)
elif(cantidad <= 15):
    print("Opcion invalida")