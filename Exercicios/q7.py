# 7. verificar se um número de três dígitos é um palíndromo.

num = int(input("digite um numero de 3 digitos:"))


if 100 <= num <= 999:  
    primeiro_digito = num // 100
    ultimo_digito = num % 10
    
    if primeiro_digito == ultimo_digito:  
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")
else:
    print("Número fora do intervalo de três dígitos!")
