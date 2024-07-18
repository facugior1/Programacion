jugador = 0
lista = ""
while(True):
    nombre = input("Nombre:")
    lista = lista + nombre + ","
    print(lista)
    pregunta = input(f"Viene {nombre}?")
    if(pregunta == "Si"):
        jugador +=1
        fin = input("Quiere terminar (Si/No)")
        if(fin == "Si"):
            break
    if(jugador >= 5 and jugador <7):
        print("Cancha unica")