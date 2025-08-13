
# Funções:
def funcao_deposito(valor_dep, saldo, extrato):
    saldo += valor_dep
    extrato.append(f"Depósito: R$ {valor_dep:.2f}")
    return saldo, extrato

def funcao_sacar(**kwargs):   #saldo, extrato, limite, numero_saques, limite_saques):
    valor_saque = kwargs['valor_saque']
    saldo = kwargs.get('saldo')
    extrato = kwargs.get('extrato')
    limite = kwargs.get('limite')
    numero_saques = kwargs.get('numero_saques')
    limite_saques = kwargs.get('limite_saques')

    if valor_saque > limite:
        print("Limite de saque é R$500,00, digite um valor dentro do limite")
    elif numero_saques >= limite_saques:
        print("Já atingiu o limite de 3 saques diários")
    elif valor_saque > saldo:
        print("Não será possível sacar por falta de saldo")
    elif valor_saque > 0:
        saldo -= valor_saque
        numero_saques += 1
        extrato.append(f"Saque: R$ {valor_saque:.2f}")
    else:
        print("Digite um número positivo")
    return saldo, extrato, numero_saques

def funcao_extrato(saldo, **kwargs):
    print("\n============ EXTRATO ============")
    extrato = kwargs.get("extrato")  #extrato = kwargs['extrato']
    if not extrato:
        print("\nNão foram realizadas movimentações")
    else:
        for item in range(len(extrato)):
            print(f"{extrato[item]}")
        print(f"\nSaldo: R$ {saldo:.2f}")
    print("=================================")      


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
                saldo, extrato = funcao_deposito(deposito,saldo,extrato)
                print(f"Depositanto o valor de R${deposito:.2f}...")
                break
            else:
                print("Digite um valor maior que zero para depósito")
                break
    elif opcao =="s":
        saque = float(input("Digite o valor do Saque: "))
        if saque > 0:
            saldo, extrato, numero_saques = funcao_sacar(valor_saque=saque, saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques =LIMITE_SAQUES)
        else:
            print(f"{saque:.2f} não é um valor válido")
    elif opcao == "e":
        funcao_extrato(saldo, extrato=extrato)
             
    elif opcao == "q":
        print("Saindo")
        break
    else:
        print("Digite uma opção válida")

    
