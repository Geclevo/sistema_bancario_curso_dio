menu = """
 ======= MENU =======
 [d] - Depositar
 [s] - Sacar
 [e] - Extrato
 [q] - Sair

=> """

saldo = 1000
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        while True:
            deposito = float(input("Digite o valor do depósito: "))
            if deposito > 0:
                saldo += deposito
                extrato.append("Depósito + ")
                extrato.append(deposito)
                print(f"Depositanto o valor de R${deposito:.2f}...")
                break
            else:
                print("Digite um valor maior que zero para depósito")
    
    elif opcao =="s":
        while True:
            saque = float(input("Digite o valor do Saque: "))
            if saque <= limite and saldo >= saque and numero_saques < LIMITE_SAQUES and saque > 0 :
                saldo -= saque
                extrato.append("Saque - ")
                extrato.append(saque)
                numero_saques += 1
                print(f"Sacando o valor de R${saque:.2f}...")
                break
            elif numero_saques >= LIMITE_SAQUES:
                print("Já atingiu o limite de 3 saques diários")
                break
            elif saldo < saque:
                print("Não será possível sacar por falta de saldo")
                break
            elif saque > limite:
                print("Limite de saque é R$500,00, digite um valor dentro do limite")
                break
            else:
                print("Valor inválido")
                break
    
    elif opcao == "e":
        print("\n============ EXTRATO ============")
        if not extrato:
            print("\nNão foram realizadas movimentações")
        else:
            coluna_extrato = extrato[1::2]
            coluna_deb_cred = extrato[0::2]
            for item in range(len(coluna_deb_cred)):
                print(f"{coluna_deb_cred[item]}{coluna_extrato[item]:.2f}")
            print(f"\nSaldo Total: R$ {saldo:.2f}")
        print("\n=================================")       
    elif opcao == "q":
        print("Saindo")
        break
    else:
        print("Digite uma opção válida")

    
