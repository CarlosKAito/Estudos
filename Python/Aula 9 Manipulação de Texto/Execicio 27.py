n = str(input("Escreva seu nome completo: ")).strip()
nome = n.split()
print("Muito prazer em te conhecer!")
print("Seu primeiro nome é {}".format(nome[0]))
print("Seu Ultimo nome e {}".format(nome[len(nome)-1]))

