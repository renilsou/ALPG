bolsaFamilia = input("Possui Bolsa Família?\nS - Sim\nN - Não\n").upper()
filhos = input("Possui mais de três filhos?\nS - Sim\nN - Não\n").upper()

if(bolsaFamilia=="S" and filhos=="S"):
    print("Você tem acesso à vaga de cotista!")
else:
    print("Você não tem acesso à vaga de cotista.")