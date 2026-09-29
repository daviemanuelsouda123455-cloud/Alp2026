import random

def jogar_adivinhacao():
    print("--- BEM-VINDO AO JOGO DE ADIVINHAÇÃO ---")
    
    # Escolha do nível de dificuldade
    print("Escolha o nível de dificuldade:")
    print("1 - Adivinhar entre 1 e 10")
    print("2 - Adivinhar entre 1 e 20")
    print("3 - Adivinhar entre 1 e 30")
    
    opcao = input("Digite o número correspondente à dificuldade (1, 2 ou 3): ")
    
    if opcao == '2':
        limite_max = 20
    elif opcao == '3':
        limite_max = 30
    else:
        limite_max = 10  # Padrão

    # Sorteio do número
    numero_secreto = random.randint(1, limite_max)
    tentativas_maximas = 3
    
    print(f"\nTente adivinhar o número entre 1 e {limite_max}. Você tem {tentativas_maximas} tentativas.")
    
    acertou = False
    for tentativa in range(1, tentativas_maximas + 1):
        print(f"\nTentativa {tentativa} de {tentativas_maximas}")
        try:
            palpite = int(input("Digite o seu palpite: "))
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
            continue
            
        if palpite == numero_secreto:
            print("Parabéns, você acertou!")
            acertou = True
            break
        elif palpite < numero_secreto:
            print("Você errou! Tente um número maior.")
        else:
            print("Você errou! Tente um número menor.")
            
    if not acertou:
        print(f"\nVocê perdeu! Fim de jogo. O número sorteado era: {numero_secreto}.")
        
    # Pergunta se quer jogar novamente
    reiniciar = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
    if reiniciar == 's':
        print("\n" * 2)
        jogar_adivinhacao()
    else:
        print("Obrigado por jogar!")

# Iniciar o jogo
jogar_adivinhacao()
