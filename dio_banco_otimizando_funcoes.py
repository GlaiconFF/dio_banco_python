menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[u] Cadastrar Usuário
[c] Cadastrar Conta

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
agencia = "0001"
numero_conta = 1
contas = []

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:    R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def ver_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==============================")

    return

def cadastrar_usuario(nome, data_nasc, cpf, endereco, usuarios):
    for usuario in usuarios:
        if cpf == usuario[2]:
            print("CPF já cadastrado.")
            return usuarios

    usuarios.append([nome, data_nasc, cpf, endereco])

    return usuarios

def cadastrar_conta(agencia, numero_conta, cpf_usuario, usuarios, contas):

    for usuario in usuarios:
        if cpf_usuario == usuario[2]:
            contas.append([agencia, numero_conta, usuario])
            numero_conta += 1
            return contas, numero_conta
    print("CPF não cadastrado.")

    return contas, numero_conta

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

    elif opcao == "e":
        ver_extrato(saldo, extrato=extrato)

    elif opcao == "q":
        print("Obrigado por usar nosso sistema. Até logo!")
        break

    elif opcao == "u":
        nome = input("Informe o nome: ")
        data_nasc = input("Informe a data de nascimento: ")
        while True:
            cpf = input("Informe o CPF (apenas números): ")
            if cpf.isdigit():
                break
            print("CPF inválido. Digite apenas números.")
        logradouro = input("Informe o logradouro: ")
        nro = input("Informe o número: ")
        bairro = input("Informe o bairro: ")
        cidade = input("Informe a cidade: ")
        estado = input("Informa o estado (sigla): ")
        endereco = f"{logradouro} - {nro} - {bairro} - {cidade}/{estado}"
        usuarios = cadastrar_usuario(nome, data_nasc, cpf, endereco, usuarios)

    elif opcao == "c":
        while True:
            cpf_usuario = input("Informe o CPF (apenas números): ")
            if cpf_usuario.isdigit():
                break
            print("CPF inválido. Digite apenas números.")
        contas, numero_conta = cadastrar_conta(agencia, numero_conta, cpf_usuario, usuarios, contas)
        print(contas)

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")
