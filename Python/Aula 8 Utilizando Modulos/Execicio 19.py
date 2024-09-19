import random

a1 = str(input("Informe um nome: "))
a2 = str(input("Informe um nome: "))
a3 = str(input("Informe um nome: "))
a4 = str(input("Informe um nome: "))
lista = [a1, a2 , a3, a4]
sorteio = random.choice(lista)


print (sorteio)