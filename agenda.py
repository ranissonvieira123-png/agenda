#Menu da Agenda 


agenda = []

while True:
    menu = int(input(''' 
      ----Cadastro de Agenda----
    [1] Cadastrar agenda
    [2] Vizualizar
    [3] Atualizar
    [4] Remover
    [0] Sair                                                   
    opção: '''))

    if menu == 1:
        cadastro = dict(
            nome=input("Digite o nome do contato: "),
            telefone=input("Digite o telefone: "),
            email=input("Digite o Email: ")
        )
        agenda.append(cadastro)
        print("\nDados cadastrados com sucesso\n")

    elif menu == 2:
        nome = input("Digite o contato: ")
        for cadastro in agenda:
            if cadastro['nome'] == nome:
                print("Nome:", cadastro["nome"])
                print("Telefone:", cadastro["telefone"])
                print("Email:", cadastro["email"])
                break
        else:
            print("Contato não encontrado")

    elif menu == 3:
        nome = input("Digite o nome do contato: ")
        for cadastro in agenda:
            if cadastro["nome"] == nome:
                cadastro["telefone"] = input("Digite um novo telefone: ")
                cadastro["email"] = input("Digite um novo email: ")
                print("Dados atualizados com sucesso")
                break
        else:
            print("Cliente não encontrado")

    elif menu == 4:
        nome = input("Digite o nome para remover: ")
        for cadastro in agenda:
            if cadastro["nome"] == nome:
                agenda.remove(cadastro)
                print("Contato removido")
                break
        else:
            print("Contato não encontrado")

    elif menu == 0:
        print("Saindo do programa")
        break

    else:
        print("Opção inválida, escolha outra opção no menu")
