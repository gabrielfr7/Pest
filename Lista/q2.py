# 2. comando para chegar ate o numero dado pelo o usuario

num = int(input("digite um numero positivo:"))
cont = 1 

while num < 0:
    print("tente novamente. Digite um numero positivo")
    num = int(input("digite um numero positivo:"))

while num >= cont:
    print(cont)
    cont = cont + 1 

print('fim')
