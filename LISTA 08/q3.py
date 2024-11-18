import random

def exibirMenu():
    print('''=== SELECIONE UMA DAS OPÇÕES ABAIXO: ===
[1] - Sete Chutes
[2] - Cinco Chutes
[3] - Três Chutes
[4] - Sair''')
    
def solicitarChute(nChutes):
    for i in range(0,nChutes):
        chute = int(input(f"Chute {i+1}: "))
        validarChute(chute)

def validarChute(chute):
    if (chute < 1 or chute > 100):
        print("Chute dado está fora do intervalo de 1 a 100.")
    
    for item in chutes:
        if chute == item:
            print("Você já chutou esse número.")
    
    if chute == numero:
        print("Você acertou!")
        print(f"Quantidade de chutes: {len(chutes)}")
        chutes.append(chute)
    
    if (chute < numero and chute > 0):
        print("Você errou! Chute foi menor que o número secreto!")
        chutes.append(chute)

    if (chute > numero and chute < 100):
        print("Você errou! Chute foi maior que o número secreto!")
        chutes.append(chute)

while True:

    numero = random.randint(1,100)
    print(numero)
    chutes = []

    exibirMenu()

    opcao = int(input("Opção: "))

    match opcao:
        case 1:
            solicitarChute(7)
        case 2:
            solicitarChute(5)
        case 3:
            solicitarChute(3)
        case 4:
            break
        case _:
            print("Opção Inválida.")
            continue