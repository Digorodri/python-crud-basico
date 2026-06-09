# Menu principal
# Fluxo do programa
# Interação com usuário

from funcoes import cadastrar, mostrar_nome, editar, remover

while True:
    print("""Menu --------
    1 - Cadastrar
    2 - Mostrar
    3 - Editar
    4 - Remover
    5 - Sair
    -------------""")

    try:
        opcao = int(input("Digite uma opção: "))
        
        if opcao == 1:
            cadastrar()
        
        elif opcao == 2:
            mostrar_nome()
        
        elif opcao == 3:
            editar()
        
        elif opcao == 4:
            remover()
        
        elif opcao == 5:
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida!")
            
    except Exception as erro:
        print(erro)