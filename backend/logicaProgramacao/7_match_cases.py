letra_da_cor = input("Digite a primeira letra de uma cor (V, A, P, L): ").upper()

match letra_da_cor:
    case 'V':
        resultado = "A cor é Verde."
    case 'A':
        resultado = "A cor é Amarelo."
    case 'P':
        resultado = "A cor é Preto."
    case 'L':
        resultado = "A cor é Laranja."
    case _:
        resultado = "Cor não identificada."

print(resultado)



nota = int(input("Digite uma nota de 0 a 10: "))
    
match nota:
    case 10:
        avaliacao = "Parabéns! Nota máxima!"
    case 7 | 8 | 9:
        avaliacao = "Aprovado."
    case 5 | 6:
        avaliacao = "Recuperação."
    case 0 | 1 | 2 | 3 | 4:
        avaliacao = "Reprovado."
    case _:
        avaliacao = "Nota inválida."



def traduzir_dia(abreviacao):
    """
    Traduz uma abreviação de 3 letras de um dia da semana para o nome completo.
    """
    match abreviacao:
        case "Seg":
            return "Segunda-feira"
        case "Ter":
            return "Terça-feira"
        case "Qua":
            return "Quarta-feira"
        case "Qui":
            return "Quinta-feira"
        case "Sex":
            return "Sexta-feira"
        case "Sab":
            return "Sábado"
        case "Dom":
            return "Domingo"
        case _:
            return "Abreviação inválida."
        
print(f"A tradução de 'Seg' é: {traduzir_dia('Seg')}")
print(f"A tradução de 'Sab' é: {traduzir_dia('Sab')}")
print(f"A tradução de 'Xyz' é: {traduzir_dia('Xyz')}")