def menu():
    menu = """\n
    =============== MENU ===================
        [1]Depositar
        [2] Sacar
        [3] Extrato
        [4] Nova conta
        [5] Listar contas
        [6] Novo usuário
        [0] Sair
        """

    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print("\nDeposito realizado com sucesso!")
    else:
        print("Operação inválida, tente novamente")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("Operação inválida! Saldo insuficiente")
    elif excedeu_limite:
        print("Operação inválida! O valor do saque excede o limite")
    elif excedeu_saques:
        print("Operação inválida! Número de saques excedido")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")
    else:
        print("Operação inválida! O valor do saque deve ser positivo")
        
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuarios = filtrar_usuarios(cpf, usuarios)

    if usuarios:
        print("Já existe usuário com este CPF!")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== USUÁRIO CADASTRADO COM SUCESSO ===")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuarios:
        print("\n=== CONTA CADASTRADA COM SUCESSO ===")
        return {"agencia": agencia, "numero": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, impossiível criar conta.")
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Agência: {conta['agencia']}
        C/C: {conta['numero']}
        Titular: {conta['usuario']['nome']}
        """
        print("="* 100)
        print(linha)
def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []
    

    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor que será depositado: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUE,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
    
        elif opcao == "4":
            criar_usuario(usuarios)
        
        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
                
            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break