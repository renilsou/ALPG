import random

def exibirMenu():
    print('''\n=== SELECIONE UMA DAS OPÇÕES ABAIXO: ===
[1] - Sete Chutes
[2] - Cinco Chutes
[3] - Três Chutes
[4] - Sair''')
    
def solicitarChute(nChutes):
    for i in range(0,nChutes):
        chute = int(input(f"\nChute {i+1}: "))
        if validarChute(chute):
            break
    mostrarChutes()

def validarChute(chute):
    while (chute < 1 or chute > 100):
        print("Chute dado está fora do intervalo de 1 a 100.")
        chute = int(input(f"Chute novamente: "))
    
    while chute in chutes:
            print("Você já chutou esse número.")
            chute = int(input(f"Chute novamente: "))
    
    if chute == numero:
        print("Você acertou!")
        chutes.append(chute)
        print(f"Quantidade de chutes: {len(chutes)}")
        return True
       
    if (chute < numero and chute > 0):
        print("Você errou! Chute foi menor que o número secreto!")
        chutes.append(chute)
        return False

    if (chute > numero and chute < 100):
        print("Você errou! Chute foi maior que o número secreto!")
        chutes.append(chute)
        return False

def mostrarChutes():
    print(f"\nSeu(s) chute(s) foi(ram): {chutes} e o número era {numero}.")

while True:

    numero = random.randint(1,100)
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