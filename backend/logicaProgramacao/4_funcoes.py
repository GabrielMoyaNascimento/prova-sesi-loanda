
def saudacao(nome):
    return f"Olá {nome}"

def dobro(valor):
    return valor * 2

print(saudacao("João"))
print("Dobro de 4 é", dobro(4))


def media(num1, num2):
    return print((num1+num2)/2)

media(100, 80)

def parOuImpar(num):
    if(num % 2 == 0):
        return print("O numero é par")
    else:
        return print("O valor é impar")

parOuImpar(9)