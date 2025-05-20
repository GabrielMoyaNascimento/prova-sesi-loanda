# 06 - Desafios

# Verifica se um número é primo
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Conta vogais em uma palavra
def contar_vogais(palavra):
    vogais = "aeiouAEIOU"
    return sum(1 for letra in palavra if letra in vogais)

# Retorna a categoria de idade
def categoria_idade(idade):
    if idade <= 12:
        return "Criança"
    elif idade <= 17:
        return "Adolescente"
    else:
        return "Adulto"

# Calcula média de uma lista
def media(lista):
    return sum(lista) / len(lista) if lista else 0

# Testes
print("7 é primo?", eh_primo(7))
print("Vogais em 'Programar':", contar_vogais("Programar"))
print("Categoria idade 15:", categoria_idade(15))
print("Média da lista [1, 2, 3, 4]:", media([1, 2, 3, 4]))
