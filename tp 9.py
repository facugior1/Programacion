import random 
i = 1
puntos = 0
puntos2 = 0
nombre1 = input("Ingrese el nombre del P1: ")
nombre2 = input("Ingrese el nombre del P2: ")
for i in range (3):
 numero = random.randint (1,3)
 numero2 = random.randint (1,3)
 piedra = 1
 papel = 2
 tijera = 3
 jugador1 = numero
 jugador2 = numero2
 print(jugador1)
 print(jugador2)
 if(jugador1 == 1 and jugador2 == 3) or \
   (jugador1 == 2 and jugador2 == 1) or \
   (jugador1 == 3 and jugador2 == 2):
      print("gana jugador 1")
      puntos += 1
 elif(jugador1 == jugador2):
     print("empate")
 else:
    print("gana jugador 2")
    puntos2 += 1
i + 1
if(puntos >= puntos2):
    print(f" Gana ", (nombre1), "con", (puntos), "puntos")
else:
    print(f"Gana ", (nombre2), "con", (puntos2), "puntos")
    
       