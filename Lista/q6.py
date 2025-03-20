 # 6. Programa para adivinhar o numero dado pelo o usuario

import random

# Gera um número aleatório entre 1 e 9
numero_aleatorio = random.randint(1, 9)

tentativa = int(input("digite sua tentativa:"))

while True:
    if numero_aleatorio == "sair":
     print("o jogo acabou!")
    elif tentativa < numero_aleatorio:
       print("muito baixo!")
       tentativa = int(input("digite sua tentativa:"))
    elif tentativa > numero_aleatorio:
       print("muito alto!")
       tentativa = int(input("digite sua tentativa:"))
    else:
       print("parabens, você acertou")
       break     

