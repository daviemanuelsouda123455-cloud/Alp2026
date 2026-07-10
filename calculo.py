n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("1. Média ponderada")
print("2. Quadrado da soma")
print("3. Cubo do menor número")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    media = (n1 * 2 + n2 * 3) / 5
    print("A média é:", media)

elif opcao == "2":
    soma = n1 + n2
    resultado = soma * soma
    print("O quadrado da soma é:", resultado)

elif opcao == "3":
    if n1 < n2:
        menor = n1
    else:
        menor = n2
    resultado = menor * menor * menor
    print("O cubo do menor número é:", resultado)

else:
    print("Opção inválida")
