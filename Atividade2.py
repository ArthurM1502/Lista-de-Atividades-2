import json

ARQUIVO_ESTOQUE = "estoque.json"

def carregar_estoque():
    try:
        with open(ARQUIVO_ESTOQUE, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def salvar_estoque(estoque):
    with open(ARQUIVO_ESTOQUE, "w") as arquivo:
        json.dump(estoque, arquivo, indent=4)

def adicionar_produto(estoque):
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("Digite o preço: "))
    estoque.append({"nome": nome, "quantidade": quantidade, "preco": preco})
    salvar_estoque(estoque)
    print("Produto adicionado com sucesso!")

def exibir_estoque(estoque):
    if not estoque:
        print("O estoque está vazio.")
        return

    valor_total = 0
    print("\nProdutos cadastrados:")
    for produto in estoque:
        print(f"Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: R${produto['preco']:.2f}")
        valor_total += produto['quantidade'] * produto['preco']
    print(f"\nValor total do estoque: R${valor_total:.2f}")

def main():
    estoque = carregar_estoque()
    while True:
        print("\nControle de Estoque Inteligente")
        print("1. Adicionar produto")
        print("2. Exibir estoque")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto(estoque)
        elif opcao == "2":
            exibir_estoque(estoque)
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
