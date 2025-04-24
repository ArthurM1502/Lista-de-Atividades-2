import os
import json

DATA_FILE = "usuarios.json"

def carregar_dados():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

def salvar_dados():
    with open(DATA_FILE, "w") as file:
        json.dump(usuarios, file, indent=4)

usuarios = carregar_dados()

def saque(usuario):
    valor = float(input("Digite o valor para saque: "))
    if valor > 0 and valor <= usuarios[usuario]["saldo"]:
        usuarios[usuario]["saldo"] -= valor
        usuarios[usuario]["transacoes"].append(f"Saque: -R${valor:.2f}")
        salvar_dados()
        print(f"Saque de R${valor:.2f} realizado com sucesso!")
    elif valor > usuarios[usuario]["saldo"]:
        print("Saldo insuficiente para realizar o saque.")
    else:
        print("Valor inválido para saque.")

def exibir_extrato(usuario):
    print(f"Saldo atual: R${usuarios[usuario]['saldo']:.2f}")
    for transacao in usuarios[usuario]["transacoes"]:
        print(f" - {transacao}")

def deposito(usuario):
    valor = float(input("Digite o valor para depósito: "))
    if valor > 0:
        usuarios[usuario]["saldo"] += valor
        main()
    
    def main():
        print("Função main ainda não implementada.")
        salvar_dados()
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    main()
