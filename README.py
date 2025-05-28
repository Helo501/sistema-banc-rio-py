# sistema-banc-rio-pysaldo = 0
extrato = ""

while True:
    print("\n=== MENU ===")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver extrato")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito feito com sucesso!")
        else:
            print("Valor inválido.")

    elif opcao == "2":
        valor = float(input("Valor do saque: R$ "))
        if valor > 0 and valor <= saldo:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            print("Saque feito com sucesso!")
        else:
            print("Saque inválido. Verifique o valor ou saldo.")

    elif opcao == "3":
        print("\n=== EXTRATO ===")
        if extrato == "":
            print("Nenhuma movimentação.")
        else:
            print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "4":
        print("Saindo do sistema. Até mais!")
        break

    else:
        print("Opção inválida. Tente novamente.")
