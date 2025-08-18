
# FUNÇÕES:
# Função Depositar
def funcao_deposito(valor_dep, saldo, extrato):
    saldo += valor_dep
    extrato.append(f"Depósito: R$ {valor_dep:.2f}")
    return saldo, extrato

#Função Saque
def funcao_sacar(**kwargs):   # Função que passa parâmetros Keyword only: saldo, extrato, limite, numero_saques, limite_saques
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

#Função Exibir Extrato
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

# Função Novo Usuário
def funcao_novo_usuario(cpf, nome, endereco):
    novo_user = {
        cpf: {
        'Nome': nome, 'Endereco': endereco
        }
    }
    return novo_user

# Função Cadastro de Conta Corrente
def funcao_conta_corrente(cpf, usuario, cont_conta):
    nova_conta = {
        cont_conta: {
            'cpf':cpf,
            'usuario': usuario
        }
    }
    return nova_conta

#Função Listar Usuários
def funcao_listar_usuarios(user):
    for chave, conteudo in user.items():
        print(f"Nome: {conteudo["Nome"]}, CPF {chave}, Endereço: {conteudo["Endereco"]}")

#Função Lista Contas Correntes
def funcao_listar_contas(contas, AG):
    for chave, conteudo in contas.items():
        print(f"-----------------\nAgencia: {AG}\nConta Número: {chave:2.0f}\nNome: {conteudo["usuario"]}\nCPF {conteudo['cpf']}")

#Função Deletar Usuário
def funcao_del_user(cpf):
    del usuarios[cpf]

#Função Deletar Conta
def funcao_del_conta(n_conta):
    del contas_correntes[n_conta]


menu = """
 ======= MENU =======
 [d] - Depositar
 [s] - Sacar
 [e] - Extrato
 [u] - Usuários
 [c] - Contas
 [q] - Sair

=> """

menu_listar_usuarios = """

======= MENU =======
[l] - Listar Usuários
[c] - Cadastrar Novo Usuário
[a] - Apagar Usuário

=> """

menu_listar_contas ="""

======= MENU =======
[l] - Listar Contas
[c] - Cadastra Nova Conta-Corrente
[a] - Apagar Conta-Corrente

=> """


saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
contador_contas = 1 #Dígito da conta
AGENCIA = '0001' #Agência

usuarios = {}
contas_correntes = {}

while True:
    
    opcao = input(menu)

    if opcao == "d": #DEPÓSITO
        while True:
            deposito = float(input("Digite o valor do depósito: "))
            if deposito > 0:
                saldo, extrato = funcao_deposito(deposito,saldo,extrato)
                print(f"Depositanto o valor de R${deposito:.2f}...")
                break
            else:
                print("Digite um valor maior que zero para depósito")
                break
    elif opcao =="s": #SAQUE
        saque = float(input("Digite o valor do Saque: "))
        if saque > 0:
            saldo, extrato, numero_saques = funcao_sacar(valor_saque=saque, saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques =LIMITE_SAQUES)
        else:
            print(f"{saque:.2f} não é um valor válido")
    elif opcao == "e": #EXTRATO
        funcao_extrato(saldo, extrato=extrato)
    elif opcao == "u": #USUÁRIOS
        opcao_user = input(menu_listar_usuarios)
        while True:
          
            if opcao_user == 'l':
                if usuarios != {}:
                    funcao_listar_usuarios(usuarios)
                    break
                else:
                    print("Não há usuários cadastrados ainda.")
                    break
            elif opcao_user == 'c':                
                nome = input("Digite o nome do novo usuário: ")
                cpf = input("Digite o CPF do novo usuário: ")
                #Testando se o CPF já existe:
                while usuarios.get(cpf): 
                    cpf = input(f"CPF {cpf} já cadastrado, tente outro:")
                endereco = input("Digite o endereco do novo usuário: ")
                
                #Incluindo novo cadastro em Usuários
                usuarios.update(funcao_novo_usuario(cpf, nome, endereco))
                print('Usuário Cadastrado!')
                break
            # Apagando Usuário
            elif opcao_user == 'a':
                cpf = input("Digite o CPF do do usuário que deseja excluir: ")
                if cpf in usuarios:
                    print(f"Usuário {usuarios[cpf]['Nome']}, CPF {cpf} - Removido")
                    funcao_del_user(cpf)
                    break
                else:
                    print(f"Não encontramos o CPF: {cpf} cadastrado.")
                    break
                    
    elif opcao == "c": #CONTAS
        opcao_contas = input(menu_listar_contas)
        while True:
            # Listar Contas
            if opcao_contas == 'l':
                funcao_listar_contas(contas_correntes, AGENCIA)
                break
            # Cadastrar Contas
            elif opcao_contas == 'c':
                while True:
                    cpf = input("Digite o CPF do usuário que deseja criar a conta corrente: ")
                    #Testa se há usuários
                    if usuarios == {}:
                        print("Não há usuários cadastrados para vincular a conta")
                        break
                    #Testa se o CPF corresponde a um usuário
                    elif not usuarios.get(cpf):
                        print("CPF não encontrado na cadastro de usuários.")
                        break
                    elif usuarios.get(cpf):
                        contas_correntes.update(funcao_conta_corrente(cpf,usuarios[cpf]["Nome"],contador_contas))
                        contador_contas += 1
                        print(f"Conta do cliente {usuarios[cpf]["Nome"]}, CPF {cpf} cadastrado com sucesso! ")
                        print(f"Dados da sua conta:\n Agência: {AGENCIA} \n Conta-Corrente: {contador_contas-1:2.0f}")
                        break
            # Deleta Conta
            elif opcao_contas == 'a':
                n_conta = int(input("Digite o número da Conta Corrente que deseja excluir: ")) #converte para int pois a chave do dicináiro é int
                if n_conta in contas_correntes:
                    print(f"AG {AGENCIA} - Conta Corrente {n_conta} - Removido com sucesso!")
                    funcao_del_conta(n_conta)
                    break
                else:
                    print(f"Não encontramos a conta número: {n_conta} cadastrado.") 
                    break
            break

    # Sair do Programa
    elif opcao == "q":
        print("Saindo...")
        break
    else:
        print("Digite uma opção válida")

    
