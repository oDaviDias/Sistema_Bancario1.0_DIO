menu = '''
########## MENU ##########

     [1] Depositar
     [2] Sacar
     [3] Extrato
     [4] Sair

Escolha uma das opções acima: '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("Depósito")
        valor = float(input("Informe o valor de seu depósito:"))

        if valor >= 0:
            saldo += valor
            extrato += f"Deposito no valor de R${valor}"
            print(f"O saldo atual é de {saldo}")

        else:
            print("O valor informado é inválido")

    elif opcao == "2":
        print("Opção de saque")
        saque = float(input("Informe o valor a ser sacado:"))

        if saque > saldo:
            print("Operação não realizada, o valor solicitado é maior que o saldo disponível!")

        elif saque > limite:
            print("Operação não realizada, o valor solicitado excede o limite!")

        elif numero_saques >= LIMITE_SAQUES:
            print("Operação não realizada, você excedeu o limite de saques diários!")

        else:
            saldo -= saque
            extrato += f"\nSaque no valor de R${saque}"
            numero_saques += 1
            print(f"Saque realizado com sucesso! Saldo atual: {saldo}")


    elif opcao == "3":

        if extrato == "":
            print("\nNão foram realizadas nenhuma movimentação hoje.")

        else:
            print(f''' 
##########################

{extrato}

##########################

            ''')


    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
