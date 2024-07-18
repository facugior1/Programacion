import os
print("Menu")
print("1. Calcular aumento de sueldo")
print("2. Ingreso a mi programa")
print("3. Salir")
opcion = int(input(""))
if(opcion == 1):
    os.system("cls")
    numero1 = float(input("Ingrese un su sueldo"))
    numero2 = float(input("Ingrese su porcentaje de aumento deseado"))
    porcentaje = float(100)
    aumento = ((numero1) * (numero2) / (porcentaje))
    print("Su sueldo nuevo es ",(numero1) + (aumento))
elif(opcion == 2):
    nombre = input("Ingrese su nombre: ")
    if(nombre == "Facundo"):
        print("Bienvenido al programa loco")
    else:
        print("No podes ingresar a mi cuenta amigo")
elif(opcion == 3):
    print("Menu finalizado")
else: 
    print("Opcion invalida capo")
    
    