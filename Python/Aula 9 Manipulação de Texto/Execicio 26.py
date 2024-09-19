frase = str(input("Forme uma frase: ")).upper().strip()

print ("a letra a aparece {} vezes na frase ".format(frase.count("A")))
print("A primeira letra a pareceu na posição {}".format(frase.find("A")+1))
print("A ultima letra a apareceu na posição {}".format(frase.rfind("A")+1))
