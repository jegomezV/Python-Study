#asi lo hice yo:
#frase_us = input("Ingrese una frase: ")
#res = len(frase_us.split())
#tiempo = res / 2
#if tiempo > 60:
    #print("tampoco te pedi un testamento")
#print(f"se tardaria en decir frase {tiempo} segundos")
#print(f"dijo un total de {res} palabras")
#dalto = float(*1000 (tiempo  / 10)) 


#la idea de este algoritmo es definir cantidad de palabras dichas en una frase,
#definir el tiempo teniendo presente que 2 palabras * 1 segundo.
#asi queda mejor:
frase_us = input("Ingrese una frase: ")
palabras = len(frase_us.split())
print(f"Dijiste {palabras} palabras, y tardaste {palabras/2} en decirlo")
print(f"Dalto hubiese tardado {palabras * 100 // 2 *1.3 / 100}")