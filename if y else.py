nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
estatura = float(input("Ingrese su estatura: "))
print("nombre",nombre)
print("edad",edad)
print("estatura", estatura)
if(estatura <= 1.7):
    print("es bajito")
else:
    print("es alto")
pesoideal = (estatura*100) - 100 + (edad) / 10 * 0.9
print("tu peso ideal es: ",pesoideal)
peso = float(input("Peso: "))
if(peso < pesoideal):
    print("estoy flaco")
elif(peso > pesoideal):
    print("estoy gordito")
elif(peso == pesoideal):
    print("estoy en mi peso ideal")
