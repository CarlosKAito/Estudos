import math

angulo = float(input("Informe um angulo qualquer: "))
an = math.radians(angulo)

seno = math.sin(an)
cosseno = math.cos(an)
tangente = math.tan(an)

print(f'Os angulos do seu angulo digitado são {seno} seno {cosseno} coseno e {tangente} tangente')