print("Seja bem-vindo a nossa feira!\nSeuas compras estão sendo processadas...")
pagamento = input("A forma de pagamento será à vista?\nS - Sim\nN - Não\n").upper()
if(pagamento=="S"):
    anuidade = input("Sua anuidade de associação de produtor rural está em dia?\nS - Sim\nN - Não\n").upper()
    if(anuidade=="S"):
        print("Compra efetuada! Volte sempre.")
    else:
        print("Compra não efetuada. Sua anuidade não está em dia")
elif(pagamento=="N"):
    print("Compra não efetuada. Só aceitamos pagamentos à vista")
else:
    print("A forma de pagamento não foi identificada.")
