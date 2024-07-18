print("El profesor tiene que comprar despensa, asi que fue al mini supermercado de la esquina")
pregunta1 = input("Tiene huevos?")
if(pregunta1== "Si"):
    huevos="12" 
    print("Deme una docena")
else:
    huevos="0"
pregunta2 = input("Tiene harina leudante?")
if(pregunta2== "Si"):
    harina="4 paquetes"
    print("Deme dos paquetes")
else:
    harina="0 paquetes"
pregunta3 = input("Tiene azucar?")
if(pregunta3== "Si"):
    azucar="3 paquetes"
    print("Deme un paquete")
else:
    azucar="0 paquetes"
print("*El profesor se revisa la billetera para ver si le alcanza algo mas*")
pregunta4 = input("Tiene leche?")
if(pregunta4== "Si"):
    leche="5 saches"
    print("Deme 2 saches")
else:
    leche="0 saches"
print("El profesor al final se fue feliz, no sin antes decir: \"Fua que caro esta todo loco\"")