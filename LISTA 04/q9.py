acesso = int(input("Como deseja acessar nossa loja? Escolha uma das opções abaixo:\n1 - Anuidade\n2 - Pagar valor da entrada\n"))

if(acesso==1):
    anuidade = input("Está com a anuidade em dia?\nS - Sim\nN - Não\n").upper()
    if(anuidade=="S"):
        print("Seja bem-vindo(a) a nossa loja!")
    else:
        print("Entrada não permitida! Sua anuidade não está em dia.")
if(acesso==2):
    print("Pagamento efetuado! Seja bem-vindo(a) a nossa loja!")
else:
    print("Forma de acesso não identificada.")
