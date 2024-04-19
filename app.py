menu = """
    Bem vindo ao seu sistema bancário,
    escolha uma opção abaixo para prosseguir!!!!
    
                [d] Depositar
                [s] Sacar
                [e] Extrato
                [q] Sair
>>>
"""

saldo = 0
limite = 500
numero_de_saques = 0
LIMITE_SAQUES = 3
valor = 0
quant_saque = 0
lista_deposito = []
lista_saque = []



while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Valor do deposito R$: "))
        if valor >0:
            saldo += valor
            lista_deposito.append(valor)
            print(f'O valor de R${valor:.2f}, foi depositado com sucesso na sua conta')

        else:
            print("Insira o valor correto para depósito")

    elif opcao == "s":
        saque = float(input("Insira o valor a ser sacado R$: "))
        if quant_saque == LIMITE_SAQUES:
            print("Voce atingiu seu limite de saque diário")

        elif saque < limite and saque < saldo:
                saldo -= saque
                quant_saque += 1
                lista_saque.append(saque)
                print(f"O valor de R${saque:.2f}, foi sacado com sucesso de sua conta")
        else:
                print("Voce nao tem limite ou o valor do saque excedeu o maximo permitido pela agencia!!!")

    elif opcao  == "e":
        for itens in lista_deposito:
            print(f"Voce realizou um deposito de R$:{itens:.2f}")
        for itens in lista_saque:
            print(f"Voce realizou um saque no valor de R$:{itens:.2f}")
        print(f"Seu saldo é de {saldo:.2f}")


    elif opcao == "q":
        break
    else:
        print('Digite uma opção válida')



