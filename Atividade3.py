import json
import os

SEAT_FILE = "assentos.json"

def initialize_seat_map():
    if not os.path.exists(SEAT_FILE):
        assentos = [["Livre" for _ in range(10)] for _ in range(10)]
        with open(SEAT_FILE, "w") as file:
            json.dump(assentos, file)

def load_seat_map():
    with open(SEAT_FILE, "r") as file:
        return json.load(file)

def save_seat_map(assentos):
    with open(SEAT_FILE, "w") as file:
        json.dump(assentos, file)

def exibir_mapa():
    assentos = load_seat_map()
    for i, linha in enumerate(assentos):
        print(f"Linha {i + 1}: {linha}")

def reservar_assento():
    assentos = load_seat_map()
    try:
        linha = int(input()) - 1
        coluna = int(input()) - 1
        if assentos[linha][coluna] == "Livre":
            assentos[linha][coluna] = "Reservado"
            save_seat_map(assentos)
            print("Reservado")
        else:
            print("Já reservado")
    except (ValueError, IndexError):
        print("Inválido")

def cancelar_reserva():
    assentos = load_seat_map()
    try:
        linha = int(input()) - 1
        coluna = int(input()) - 1
        if assentos[linha][coluna] == "Reservado":
            assentos[linha][coluna] = "Livre"
            save_seat_map(assentos)
            print("Cancelado")
        else:
            print("Já livre")
    except (ValueError, IndexError):
        print("Inválido")

def menu():
    initialize_seat_map()
    while True:
        print("1")
        print("2")
        print("3")
        print("4")
        opcao = input()

        if opcao == "1":
            exibir_mapa()
        elif opcao == "2":
            reservar_assento()
        elif opcao == "3":
            cancelar_reserva()
        elif opcao == "4":
            break

if __name__ == "__main__":
    menu()
