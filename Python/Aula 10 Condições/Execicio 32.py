ano = int(input("Que ano quer Analisa: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("È Bissexto")
else:
    print("Nao e bissexto")
    