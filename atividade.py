logado = False
usuario_logado = ""
usuarios = []

while True:
    print("\033c", end="") # comando para limpar a tela
    print("#########################################")
    print("SISTEMA DE CADASTRO DE USUÁRIOS")
    print("#########################################\n")

    if not logado:
        print("===LOGIN===")
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")

        if login == "admin" and senha == "123":
            print(f"Login realizado com sucesso! Bem-vindo, {login}!\n")
            input("ENTER para continuar...")
            logado = True
            usuario_logado = login 
        else:
            input("\nLogin ou senha incorretos! ENTER para tentar novamente.")

    else:
        print("===MENU PRINCIPAL===")
        print(f"Usuário logado: {usuario_logado}")
        print("1 - Inserir usuário")
        print("2 - Pesquisar usuário")
        print("3 - Remover usuário")
        print("4 - Listar todos os usuários")
        print("5 - Logout")
        print("6 - Encerrar")

        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Digite o nome do usuário: ")
            usuarios.append(nome)
            input("Usuário cadastrado! ENTER para continuar...")

        elif opcao == "2":
            nome = input("Digite o nome para pesquisar: ")
            if nome in usuarios:
                print("Usuário encontrado!")
            else:
                print("Usuário não encontrado!")
            input("ENTER para continuar...")

        elif opcao == "3":
            nome = input("Digite o nome para remover: ")
            if nome in usuarios:
                usuarios.remove(nome)
                print("Usuário removido!")
            else:
                print("Usuário não encontrado!")
            input("ENTER para continuar...")

        elif opcao == "4":
            print("=== LISTA DE USUÁRIOS ===")
            for u in usuarios:
                print(u)
            input("ENTER para continuar...")

        elif opcao == "5":
            print("Fazendo logout...")
            input("ENTER para voltar para o login.")
            usuario_logado = ""
            logado = False
            
        elif opcao == "6":
            print("Encerrando o sistema... Até logo!")
            break

        else:
            input("Opção inválida! ENTER para continuar...")
