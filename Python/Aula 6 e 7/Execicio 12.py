produto = float(input("Informe o valor do seu produto: "))

desconto = produto * 5 / 100
preco_final = produto - desconto 

print(f"O seu produto com valor {produto} com o desconto de 5% fica {preco_final} ")