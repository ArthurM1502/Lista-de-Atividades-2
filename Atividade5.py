import json

ARQUIVO_CONTATOS = "contatos.json"

def carregar_contatos():
    try:
        with open(ARQUIVO_CONTATOS, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def salvar_contatos(contatos):
    with open(ARQUIVO_CONTATOS, "w") as arquivo:
        json.dump(contatos, arquivo, indent=4)

def adicionar_contato(contatos):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    
    if nome in contatos:
        print("Contato já existe!")
    else:
        contatos[nome] = {"telefone": telefone, "email": email}
        salvar_contatos(contatos)
        print("Contato adicionado com sucesso!")

def buscar_contato(contatos):
    nome = input("Digite o nome do contato que deseja buscar: ")
    if nome in contatos:
        print(f"Nome: {nome}")
        print(f"Telefone: {contatos[nome]['telefone']}")
        print(f"Email: {contatos[nome]['email']}")
    else:
        print("Contato não encontrado!")

def main():
    contatos = carregar_contatos()
    
    while True:
        print("\nGerenciador de Contatos")
        print("1. Adicionar Contato")
        print("2. Buscar Contato")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_contato(contatos)
        elif opcao == "2":
            buscar_contato(contatos)
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
