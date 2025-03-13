# 5. verificação se um número inteiro dado é divisível por 2, 3 ou nenhum deles.

num = int(input("digite um numero inteiro:"))

if num % 2 == 0:
    print("divisivel por 2")

elif num % 3 == 0:
    print("divisivekl por 3")

else:
    print("não é divisível por 2 ou 3")
