#Crie um código em Python que use o comando "while" para ler números inteiros inseridos pelo usuário até que o número inserido seja zero 
#e imprima a soma de todos os números inseridos.

num = int(input("digite um numero inteiro:"))
soma = 0 

while num != 0:
    soma = num + soma 
    num = int(input("digite um numero inteiro"))

print("Fim")
print(f"A soma dos numeros é: {soma}")
