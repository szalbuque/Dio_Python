MENU = """
Digite a opcao desejada:
1: Deposito
2: Saque
3: Extrato
4: Sair
"""
extrato = ""
saldo = 0
numero_de_saques = 0
limite_por_saque = 500
maximo_saques = 3

while True:
    opcao = input(MENU)
    if opcao == "1":
        valor_deposito = float(input("\nDigite o valor para deposito:"))
        if valor_deposito < 0:
            print ("\nO valor deve ser maior que zero.\n")
        else:
            saldo += valor_deposito
            extrato = extrato+f"Deposito R$ {valor_deposito:.2f}\n"
            extrato = extrato+f"Saldo atual: R$ {saldo:.2f}\n"
    elif opcao == "2":
        if numero_de_saques < maximo_saques:
                valor_saque = float(input("\nDigite o valor para saque:\n"))
                if valor_saque <= saldo:
                    if valor_saque <= limite_por_saque:
                        saldo -= valor_saque
                        numero_de_saques += 1
                        print(numero_de_saques)
                        extrato = extrato + f"Saque R$ {valor_saque:.2f}\n"
                        extrato = extrato+f"Saldo atual: R$ {saldo:.2f}\n"
                    else:
                        print (f"\n O valor maximo por saque é de R$ {limite_por_saque:.2f}.\n")
                else:
                    print ("\nO saldo eh insuficiente para o saque.")
        else:
            print ("\n Foi atingido o maximo de saques permitido. \n")
    elif opcao == "3":
        if extrato == "":
            print("\nNao houve movimentacoes.\n")
        else:
            print("\nEXTRATO:")
            print(extrato)
    elif opcao == "4":
        break
    else:
        print("\nOpcao incorreta, favor digitar novamente.\n")

print("Saida solicitada pelo usuario.") 
