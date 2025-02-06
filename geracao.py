from os import system as sys; sys('cls')
import time 
import random

sequencia = []
numbers = [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]
geracoes = int(input("digite o numero de geracoes desejadas (cada uma possui dez mil digitos aleatorios): "))


#numero da sequencia
x = 1

#numero da geracao
y = 1


def gerar():
  x = 1
  while x <= 10000:
    nx = random.choice(numbers)
    sequencia.append(nx)
    x += 1
  print(*sequencia, sep="")
  


sys('cls')
while y <= geracoes:
  print(f"geracao {y}:")
  print("")
  gerar()
  print("")
  sequencia = []
  y += 1 