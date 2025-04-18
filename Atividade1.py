import json
from datetime import datetime

ARQUIVO_TAREFAS = "tarefas.json"

def carregar_tarefas():
    try:
        with open(ARQUIVO_TAREFAS, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w") as arquivo:
        json.dump(tarefas, arquivo, indent=4)

def adicionar_tarefa(tarefas):
    descricao = input("Descrição da tarefa: ")
    prazo = input("Prazo (YYYY-MM-DD): ")
    try:
        datetime.strptime(prazo, "%Y-%m-%d")
        tarefas.append({"descricao": descricao, "prazo": prazo, "concluida": False})
        salvar_tarefas(tarefas)
        print("Tarefa adicionada com sucesso!")
    except ValueError:
        print("Formato de data inválido. Tente novamente.")

def listar_tarefas(tarefas):
    tarefas_ordenadas = sorted(tarefas, key=lambda x: x["prazo"])
    for i, tarefa in enumerate(tarefas_ordenadas, 1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i}. {tarefa['descricao']} - Prazo: {tarefa['prazo']} - Status: {status}")

def marcar_tarefa_concluida(tarefas):
    listar_tarefas(tarefas)
    try:
        numero_tarefa = int(input("Número da tarefa para marcar como concluída: "))
        if 1 <= numero_tarefa <= len(tarefas):
            tarefas[numero_tarefa - 1]["concluida"] = True
            salvar_tarefas(tarefas)
            print("Tarefa marcada como concluída!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Tente novamente.")

def principal():
    tarefas = carregar_tarefas()
    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            adicionar_tarefa(tarefas)
        elif escolha == "2":
            listar_tarefas(tarefas)
        elif escolha == "3":
            marcar_tarefa_concluida(tarefas)
        elif escolha == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    principal()
