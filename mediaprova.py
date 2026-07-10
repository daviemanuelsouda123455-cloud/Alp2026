n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3
print(f"Média: {media:.1f}")

if media >= 7:
    print("Aprovado")
elif media >= 4:
    print("Prova final")
else:
    print("Reprovado")
