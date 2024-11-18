def calcularDesconto (preco, categoria):
    if categoria == "A":
        precoFinal = preco - (0.1*preco)
        print(f"Preço final com desconto de 10% aplicado: R$ {precoFinal}")
    if categoria == "B":
        precoFinal = preco - (0.15*preco)
        print(f"Preço final com desconto de 15% aplicado: R$ {precoFinal}")
    if categoria == "C":
        precoFinal = preco - (0.2*preco)
        print(f"Preço final com desconto de 20% aplicado: R$ {precoFinal}")
    if (categoria != "A" and categoria != "B" and categoria != "C"):
        precoFinal = preco - (0.05*preco)
        print(f"Preço final com desconto de 5% aplicado: R$ {precoFinal}")

preco = float(input("Informe o preço do produto: "))
categoria = input('''Selecione a categoria:
[A] - 10% de Desconto
[B] - 15% de Desconto
[C] - 20% de Desconto
[Qualquer outra categoria] - 5% de Desconto
Categoria: ''').upper()

calcularDesconto(preco, categoria)
    
    