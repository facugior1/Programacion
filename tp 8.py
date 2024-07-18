aux_nombre = ""
aux_puntos = 0
i = 1
for i in range(5):
    print("Entrevista")
    puntos = 0
    nombre = str(input("Ingrese su nombre:"))
    edad = float(input("Ingrese su edad: "))
    if(edad <= 30):
        puntos = puntos + 1
    clientes = str(input("Tiene buen trato con los clientes? "))
    if(clientes == "Si"):
     puntos = puntos + 1
    xp = float(input("Cuantos años tiene de experiencia? "))
    if(xp >=2):
        puntos = puntos + 1
    redsocial = str(input("Tiene buen manejo de redes sociales? "))
    if(redsocial == "Si"):
        puntos = puntos + 1
    if(puntos > aux_puntos):
        aux_puntos = puntos
        aux_nombre = nombre
    i +=1
    
        
print("El candidato mas capacitado es ",(aux_nombre), "con",(aux_puntos), "puntos")
    
    
                