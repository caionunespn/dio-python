saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

index_conta = 1
usuarios = []
contas = []

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

        return (saldo, extrato)

    else:
        print("Operação falhou! O valor informado é inválido.")

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

        return (saldo, extrato)

    else:
        print("Operação falhou! O valor informado é inválido.")

def gerar_extrato(saldo, /, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuario):
    cpf = usuario["cpf"]

    usuario_ja_cadastrado = False

    for usuario_cadastrado in usuarios:
        if usuario_cadastrado["cpf"] == cpf:
            usuario_ja_cadastrado = True
            break
    
    if usuario_ja_cadastrado:
        print("Usuário já cadastrado")
    else:
        usuarios.append(usuario)

def criar_conta(conta):
    usuario_ja_cadastrado = False

    for usuario_cadastrado in usuarios:
        if usuario_cadastrado["cpf"] == cpf:
            usuario_ja_cadastrado = True
            break
    
    if usuario_ja_cadastrado:
        contas.append(conta)
    else:
        print("Usuário não cadastrado")

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar cliente
[c] Criar conta
[q] Sair

=> """

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        (novo_saldo, novo_extrato) = deposito(saldo, valor, extrato)

        if novo_saldo is not None and novo_extrato is not None:
            saldo = novo_saldo
            extrato = novo_extrato

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        (novo_saldo, novo_extratao) = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        
        if novo_saldo is not None and novo_extratao is not None:
            saldo = novo_saldo
            extrato = novo_extrato

    elif opcao == "e":
        gerar_extrato(saldo, extrato=extrato)

    elif opcao == "u":
        nome = input("Informe o nome do cliente: ")
        data_nascimento = input("Informe a data de nascimento: ")
        cpf = input("Informe o CPF do cliente: ").strip().replace("-", "").replace(".", "")
        endereco = input("Informe o endereço do cliente: ")

        usuario = {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco
        }

        criar_usuario(usuario)

    elif opcao == "c":
        cpf = input("Informe o CPF do cliente: ").strip().replace("-", "").replace(".", "")

        conta = {
            "usuario": cpf,
            "agencia": "0001",
            "conta": index_conta
        }

        criar_conta(conta)
        index_conta += 1

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")