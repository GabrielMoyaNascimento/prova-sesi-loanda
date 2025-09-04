print("Bem-vindo ao Caixa Eletrônico!")

nome_usuario = input("Para começar, digite seu nome para 'cadastrar' a conta: ")
contas = 0.0
print(f"Olá, {nome_usuario}! Sua conta foi criada com sucesso, saldo inicial de R$ {contas:.2f}.")

def caixa_eletronico(nome_usuario, contas):

    opcao = ""
    while opcao != "sair":
        print(f"\nBem-vindo(a), {nome_usuario}!")
        print("--- Menu de Operações ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Listar Saldo")
        print("Sair")
        
        opcao = input("Digite a sua opção: ").strip().lower()

        match opcao:
            case "1":
                valor_deposito = float(input("Digite o valor do depósito: R$ "))
                if valor_deposito > 0:
                    contas += valor_deposito
                    print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
                else:
                    print("Valor de depósito inválido. Deve ser um número positivo.")
            
            case "2":
                valor_saque = float(input("Digite o valor do saque: R$ "))
                if valor_saque > 0 and valor_saque <= contas:
                    contas -= valor_saque
                    print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
                elif valor_saque > contas:
                    print("Saldo insuficiente.")
                else:
                    print("Valor de saque inválido. Deve ser um número positivo.")

            case "3":
                saldo_atual = contas
                print(f"Seu saldo atual é de R$ {saldo_atual:.2f}")
            
            case _:
                print("Opção inválida. Por favor, escolha uma das opções do menu.")

    print("\nEncerrando a sessão. Obrigado por usar nosso serviço!")


caixa_eletronico(nome_usuario, contas)