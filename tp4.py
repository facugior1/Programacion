edad = (float(input("ingrese su edad")))
if edad >= 25:
    titulo = input("Tiene titulo secundario?")
    if titulo == "no":
        print("Debe rendir un examen especial")
    else:
        print("No necesita rendir un examen especial")
        print("Bienvenido al instituto Nuevo Cuyo")
else: 
    print("No puede inscribirse al instituto por edad insufiente")