# For
for i in range(5):
    print("Contando:", i)


# While
senha = ""
while senha != "Moya":
    senha = input("Digite a senha: ")
    print("Senha Incorreta.")

print("Acesso liberado.")

# For
for i in range(1, 11):
    print("Contando:", i)

# Diga quantos números pares tem na lista  

# numeros = [10, 15, 22, 33, 42, 55, 60, 73, 88, 91, 100] 

numeros = [10, 15, 22, 33, 42, 55, 60, 73, 88, 91, 100]
pares = 0

for x in numeros:
    if( x % 2 == 0 ): 
        pares+=1
print("Quantidade de números pares:", pares)


# Somar números até o usuário digitar 0. 

soma = 0

while valor != 0:
    valor = int(input("Digite um valor:"))
    soma+=valor

print("Valor total da soma: ", soma)
