movimentacao = []
saldoAtual = 0

def exibirMenu():
    print('''=== SELECIONE UMA DAS OPÇÕES ABAIXO: ===
[1] - VER SALDO
[2] - DEPOSITAR
[3] - SACAR
[4] - EXTRATO
[5] - SAIR''')

def validarValor(valor):
    if valor <= 0:
        return False
    return True
    
def exibirSaldo(saldo):
    print(f"SALDO ATUAL: R$ {saldo:.2f}")
    
def depositarValor(saldo):
    deposito = float(input("INFORME O VALOR A SER DEPOSITADO:"))
    if validarValor(deposito):
        print(f"\nO VALOR DE R$ {deposito:.2f} FOI DEPOSITADO EM SUA CONTA.\n")
        saldo += deposito
        exibirSaldo(saldo)
        movimentacao.append(deposito)
    else:
        print("VALOR INVÁLIDO PARA DEPÓSITO!")

def sacarValor(saldo):
    saque = float(input("INFORME O VALOR A SER SACADO: "))
    if validarValor(saque):
        print(f"O VALOR DE R$ {saque:.2f} FOI SACADO DE SUA CONTA.")
        saldo -= saque
        exibirSaldo(saldo)
        movimentacao.append(-saque)
    else:
        print("VALOR INVÁLIDO PARA SAQUE!")

def exibirMovimentacao(saldo):
    for movimento in movimentacao:
        print(movimento)
    exibirSaldo(saldo)

while True:
    exibirMenu()

    opcao = int(input("INFORME A OPÇÃO: "))

    match opcao:

        case 1:
            exibirSaldo(saldoAtual)
        case 2:
            depositarValor(saldoAtual)
        case 3:
            sacarValor(saldoAtual)
        case 4:
            exibirMovimentacao(saldoAtual)
        case 5:
            break
        case _:
            print("\nOPÇÃO INVÁLIDA!\n")