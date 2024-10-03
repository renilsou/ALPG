nome = input("Informe seu nome: ")
senha = input("Insira sua senha: ")
confirmaSenha = input("Confirme sua senha: ")

if(senha==confirmaSenha):
    print("O cadastro realizado!")
else:
    print("Cadastro não realizado! As senhas não coincidem")