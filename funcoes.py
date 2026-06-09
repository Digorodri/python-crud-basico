# Validações

def cadastrar():
    nome = input("Digite um nome: ").strip()
    
    while nome == "" or nome.isdigit():
        nome = nome = input("Digite um nome: ").strip()
        
    with open("nomes.txt", "a") as arquivo:
        arquivo.write(f"{nome}\n")
        
def mostrar_nome():
    with open("nomes.txt", "r") as arquivo:
        conteudo = arquivo.readlines()
        
    for nome in conteudo:
        print(f"Usuário: {nome.strip()}")

def editar():
    with open("nomes.txt", "r") as arquivo:
        conteudo = arquivo.readlines()
    
    for indice, nome in enumerate(conteudo, start=1):
        print(f"{indice} - {nome.strip()}")
        
    indice_editar = int(input("Qual usuário deseja editar? "))
    
    if indice_editar < 1 or indice_editar > len(conteudo):
        print("Erro! Não existe esse índice.")
    else:
        novo_nome = input("Digite o novo nome: ")
        
        conteudo[indice_editar -1] = novo_nome + "\n"
            
        with open("nomes.txt", "w") as arquivo:
            arquivo.writelines(conteudo)
        
def remover():
    with open("nomes.txt", "r") as arquivo:
        conteudo = arquivo.readlines()
        
    for indice, nome in enumerate(conteudo, start=1):
        print(f"Usuário {indice}: {nome.strip()}")
        
    indice_remover = int(input("Qual usuário deseja remover? "))
    
    if indice_remover < 1 or indice_remover > len(conteudo):
        print("Erro! Não existe esse índice.")
    else:
    
        del conteudo[indice_remover -1]
        
        with open("nomes.txt", "w") as arquivo:
            arquivo.writelines(conteudo)