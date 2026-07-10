preco = float(input("Digite o valor da venda: "))

print("1. À vista em espécie")
print("2. Cartão de débito")
print("3. Cartão de crédito")

codigo = input("Digite o código da forma de pagamento: ")

if codigo == "1":
    desconto = preco * 0.15
    valor_final = preco - desconto
    print("O valor com desconto é:", valor_final)

elif codigo == "2":
    desconto = preco * 0.10
    valor_final = preco - desconto
    print("O valor com desconto é:", valor_final)

elif codigo == "3":
    desconto = preco * 0.05
    valor_final = preco - desconto
    print("O valor com desconto é:", valor_final)

else:
    print("Opção inválida")
