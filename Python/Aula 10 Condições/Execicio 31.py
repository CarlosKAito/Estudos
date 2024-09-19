km = int(input("Quantos km teve sua viagem?: "))

if km <= 200:
    soma = km + 50
    print("sua viagem e abaixo de 200 km entao pagara: ",soma)
elif km >= 200:
    soma = km + 45
    print("sua viagem e acima de 200 km entao pagara: ",soma)
