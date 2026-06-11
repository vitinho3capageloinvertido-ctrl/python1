nome = input("DIgite seu nome:")
saldo_inicial = float(input("Digite seu saldo inicial:"))
valor_do_saque = float(input("DIgite o valor que voce deseja sacar:"))
saques_aprovados = 0
total_sacado = 0

while saldo_inicial > 0:
    valor_do_saque = float(input("Digite o valor do saque: "))

    if valor_do_saque == 0:
        print("Atendimento encerrado" )
        break

    elif valor_do_saque < 0:
        print("Valor invalido")

    else:
     saldo_inicial = saldo_inicial - valor_do_saque
     saques_aprovados += 1
     total_sacado += valor_do_saque

    print("Saque aprovado.")
    print("Saldo atual:", saldo_inicial)

    print("RELATÓRIO FINAL")
    print("Nome:", nome)
    print("Saques aprovados:", saques_aprovados)
    print("Total sacado:", total_sacado)
    print("Saldo final:", saldo_inicial)