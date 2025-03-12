# 3. verifição de numero inteiro 

num = int(input("digite um numero inteiro:"))


if 10 < num < 20:
    print("maior que 10 e menor que 20")
elif num > 30 or num < 5:
    print("maior que 30 ou menor que 5")
else:
    print("não é maior que 10 e menor que 20 e não é maior que 30 ou menor que 5")
